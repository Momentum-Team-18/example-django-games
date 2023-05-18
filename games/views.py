from django.shortcuts import render
from .models import Game

# Create your views here.


def list_games(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})
    # the last argument is context, which is data from the database
