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
            print(fixture.id,fixture.hometeamid)
            url = Teams.objects.filter(id=fixture.hometeamid)
            if url :
                print(url[0].cresturl)
                fixture.url = url[0].cresturl
            fixtures.append(fixture)
        fixturesList.append({'competition':competition.caption,'fixtures':fixtures})

    # print(fixturesList)

    # fixtures = Fixtures.objects.filter(my_filter_qs)
    return render(request, 'myapp/fixtures.html', {'fixtures': fixturesList})
