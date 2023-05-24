from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'number_of_players', 'age_range', 'is_active')
