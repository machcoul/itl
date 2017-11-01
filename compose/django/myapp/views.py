from django.shortcuts import render
from .models import *
from django.db.models import Q



# Create your views here.

def fixtures_view(request):
    # my_leagues = League.objects.filter(player__in=Player.objects.filter(player=request.user))
    # print "home"
    # download_teams()
    fixturesList =[]
    my_filter_qs = Q()
    for creator in ['IN_PLAY','TIMED','SCHEDULED','POSTPONED']:
        my_filter_qs = my_filter_qs | Q(status=creator)

    competitions = Competitions.objects.filter()
    for competition in competitions :
        fixtures =[]
        f = Fixtures.objects.filter(my_filter_qs,competitionid=competition.id).order_by('date')
        for fixture in f :
            homeurl = Teams.objects.filter(id=fixture.hometeamid)
            if homeurl :
                fixture.homeurl = homeurl[0].cresturl
                fixture.homename = homeurl[0].name
            awayurl = Teams.objects.filter(id=fixture.awayteamid)
            if awayurl :
                fixture.awayurl = awayurl[0].cresturl
                fixture.awayname = awayurl[0].name
            fixtures.append(fixture)
        fixturesList.append({'competition':competition.caption,'fixtures':fixtures})

    # print(fixturesList)

    # fixtures = Fixtures.objects.filter(my_filter_qs)
    return render(request, 'myapp/fixtures.html', {'fixtures': fixturesList})
