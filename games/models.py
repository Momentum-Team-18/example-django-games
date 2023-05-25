from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=200)
    number_of_players = models.IntegerField()
    age_range = models.CharField(max_length=200, blank=True, null=True)
    # fields are required by default, make optional with blank=True, null=True
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(
        to='Company', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(to='Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    player = models.ForeignKey(to='Player', on_delete=models.CASCADE)
    game = models.ForeignKey(to='Game', on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
