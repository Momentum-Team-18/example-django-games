from django.contrib import admin
from .models import Game, Company, Player, Favorite

# Register your models here.
admin.site.register(Game)
# telling the Django admin that we have a new model
admin.site.register(Company)
admin.site.register(Player)
admin.site.register(Favorite)
