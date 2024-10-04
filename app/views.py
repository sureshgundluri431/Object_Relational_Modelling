from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_Team(request):
    G1=input('Enter the Game Name:')
    # Gam=Team.objects.get_or_create(Game=G1)[0]
    obj1=Team(Game=G1)
    obj1.save()
    return HttpResponse('Game Inserted Successfully')

def insert_player(request):
    g1=input('enter the game Name:')
    p1=input('Enter the player Name:')
    u=input('enter the url:')
    # G=Team.objects.get_or_create(Game=g1)[0]
    G=Team(Game=g1)
    G.save()
    P=Player(Game = G, Name=p1,url = u)
    P.save()
    return HttpResponse("Player page is inserted")

def Insert_Access(request):
    g1=input('Enter the Game Name:')
    p1=input("Enter Player Name:")
    u=input("Enter the URL:")
    A=input("Enter Author:")
    D=input("Enter Date:")
    G=Team(Game=g1)
    G.save()
    na=Player(Game=G,Name=p1,url=u)
    na.save()
    Au=Access(name=na,author=A,date=D)
    Au.save()
    return HttpResponse('Access page is inserted')






