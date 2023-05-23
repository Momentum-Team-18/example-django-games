from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm
from .models import Game

# Create your views here.


def list_games(request):
    games = Game.objects.all()
    # Django ORM translates Python to SQL to interact with db
    return render(request, 'index.html', {'games': games})
    # the last argument is context, which is data from the database


def game_detail(request, pk):
    # game = Game.objects.get(pk=pk)
    # use get_object_or_404 to handle pks that are not in db without breaking
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game_detail.html', {'game': game})


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
    return render(request, 'new_game.html', {'form': form})
