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


def create_game(request):
    # create new game
    form = GameForm()
    return render(request, 'new_game.html', {'form': form})

    # return redirect('home')
