from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def Game(request):
    Game=input("Enter the Game Name:")
    obj1=Team.objects.create(Game=Game)
    return HttpResponse("Game inserted Successfully")

def Insert_Player(request):
    Game=input("Enter the Game Name")
    Name=input("Enter te Player Name:")
    Url=input("Enter the url:")
    if Team.objects.filter(Game=Game).exists():
        obj2=Team.objects.get(Game=Game)
        obj3=Player.objects.create(Game=obj2,Name=Name,url=Url)
        return HttpResponse("Player Inserted Successfully")
    else:
        obj1=Team.objects.create(Game=Game)
        obj3=Player.objects.create(Game=obj1,Name=Name,url=Url)
        return HttpResponse("Player Inserted Successfully")

def Insert_Access(request):
    Game=input('Enter Game:')
    Name=input("Enter the Player Name:")
    url=input("Enter Url:")
    Author=input("Ente the Author Name:")
    Date=input("Enter the Date:")
    obj1=Team.objects.get_or_create(Game=Game)[0]
    ob2=Player.objects.get_or_create(Game=obj1,Name=Name,url=url)[0]
    obj=Access.objects.get_or_create(name=ob2,author=Author,date=Date)[0]
    return HttpResponse("Access Inserted Successfully")









