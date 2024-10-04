from django.db import models

# Create your models here.

class Team(models.Model):
    Game=models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.Game

class Player(models.Model):
    Game=models.ForeignKey(Team,on_delete=models.CASCADE)
    Name=models.CharField(max_length=25)
    url=models.URLField()

    def __str__(self):
        return self.Name
    
class Access(models.Model):
    name=models.ForeignKey(Player,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()