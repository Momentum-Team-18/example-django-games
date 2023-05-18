from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=200)
    number_of_players = models.IntegerField()
    age_range = models.CharField(max_length=200, blank=True, null=True)
    # fields are required by default, make optional with blank=True, null=True

    def __str__(self):
        return self.name
