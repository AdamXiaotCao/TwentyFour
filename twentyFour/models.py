from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    # value is actually an entry in the table which contains 4 numbers that are
    # able to be used to get 24
    CHOICES = [(i,i) for i in range(11)]
    value = models.IntegerField(max_length=10, default=0, choices=CHOICES)

class Cardset(models.Model):
    cards = models.ManyToManyField(Card)

    # create your models here.
class Player(models.Model):
    user = models.OneToOneField(User)
    total_games_played = models.IntegerField(default=0)
    total_games_won = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="user-photos", default='/media/user-photos/default.jpg')
    total_points = models.IntegerField(default=0)
class Game(models.Model):
    card_sets = models.ManyToManyField(Cardset)
    participants = models.ManyToManyField(Player)
    CHOICES = [('WAIT','WAIT'),('ONGOING','ONGOING'),('END','END')]
    status = models.CharField(choices=CHOICES,default='WAIT',max_length=8)
    date = models.DateTimeField(auto_now_add=True)

class Record(models.Model):
    game_played = models.OneToOneField(Game)
    date = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField(default=False)
    player =  models.ForeignKey(Player)

class GameState(models.Model):
    game = models.OneToOneField(Game)

class PlayerState(models.Model):
    # this model is used to keep track each player's progess in a game
    progress = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    player = models.OneToOneField(Player)
    gamestate = models.ForeignKey(GameState)
