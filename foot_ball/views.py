from django.shortcuts import render
from foot_ball.models import Teams,Games


def league_table(request):
    teams = Teams.objects.all().order_by('-points')
    zmienna = ""
    if request.method == "POST":
        zmienna = "sadfadsfasdf"

    return render(request, 'teams.html', {'teams':teams})


def games_played(request):
    t = Teams.objects.get(pk=1)
    hgames = Games.objects.filter(team_home=t)
    agames = Games.objects.filter(team_away=t)
    return render(request, 'team.html', {'hgames':hgames, 'agames':agames, 'title':'dupa'})

def witaj(request):
   return render(request, 'base.html', {'title':'eryk'})
