from django.db import models

# Create your models here.

class Team(models.Model):
    Game=models.CharField(max_length=20,primary_key=True)

class Player(models.Model):
    Game=models.ForeignKey(Team,on_delete=Team)
    Name=models.CharField(max_length=25)
    url=models.URLField()
class Access(models.Model):
    name=models.ForeignKey(Player,on_delete=Player)
    author=models.CharField(max_length=100)
    date=models.DateField()