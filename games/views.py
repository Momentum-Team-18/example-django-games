from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm
from .models import Game, Company

# Create your views here.


def list_games(request):
    games = Game.objects.all()
    # Django ORM translates Python to SQL to interact with db
    return render(request, 'games/index.html', {'games': games})
    # the last argument is context, which is data from the database


def game_detail(request, pk):
    # game = Game.objects.get(pk=pk)
    # use get_object_or_404 to handle pks that are not in db without breaking
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})


def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.delete()
    return redirect('home')


def create_game(request):
    # create new game
    if request.method == 'GET':
        form = GameForm()
        # when the user visits the page, render a blank form
    else:
        # Django forms only handle GET and POST, so submitting the form will be a POST request
        form = GameForm(request.POST)
        form.save()
        # Saves the new instance of Game in the database
        return redirect('home')
    return render(request, 'games/new_game.html', {'form': form})


def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'GET':
        form = GameForm(instance=game)
        # passing the instance argument puts the existing data in the form
    else:
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            # this will update the instance in the db
            return redirect('game-detail', pk=pk)
    return render(request, 'games/edit_game.html', {'form': form})


def games_by_company(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    games = Game.objects.filter(company_id=company_pk)
    # django ORM filters data
    context = {
        'company': company,
        'games': games
    }

    return render(request, 'games/games_by_company.html', context)
