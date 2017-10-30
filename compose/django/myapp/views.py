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
        fixtures = Fixtures.objects.filter(my_filter_qs,competitionid=competition.id).order_by('date')
        fixturesList.append({'competition':competition.caption,'fixtures':fixtures})

    print(fixturesList)

    fixtures = Fixtures.objects.filter(my_filter_qs)
    return render(request, 'myapp/fixtures.html', {'fixtures': fixturesList})
