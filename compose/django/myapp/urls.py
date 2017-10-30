from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.MyLoginView, name='index'),
    # url(r'^$', views.home, name='home'),
    # url(r'^league/create/$', views.create_league, name="create_league"),
    url(r'^fixtures/$', views.fixtures_view, name="fixtures"),
    # # url(r'^league/(?P<key>[a-z0-9]*)/$', views.view_league, name="view_league"),
    # url(r'^league/(?P<key>[a-z0-9]*)/latest/$', views.latest, name="latest"),
    # url(r'^league/(?P<key>[a-z0-9]*)/ranking/$', views.ranking, name="ranking"),
    # url(r'^league/(?P<key>[a-z0-9]*)/upcoming/$', views.upcoming, name="upcoming"),
    # url(r'^league/(?P<key>[a-z0-9]*)/invite/$', views.invite_player, name="invite_player"),
    # url(r'^league/(?P<key>[a-z0-9]*)/join/$', views.join_league, name="join_league"),
    # url(r'^league/(?P<key>[a-z0-9]*)/fixture/add/$', views.add_fixture, name="add_fixture"),
    # url(r'^league/(?P<key>[a-z0-9]*)/fixture/bet/(?P<fixture>[0-9]*)/$', views.bet_fixture, name="bet_fixture"),
    # url(r'^league/(?P<key>[a-z0-9]*)/upcoming/fixture/bet/(?P<fixture>[0-9]*)/$', views.bet_fixture, name="bet_fixture"),
    # url(r'^league/(?P<key>[a-z0-9]*)/fixture/results/(?P<fixture>[0-9]*)/$', views.results_fixture, name="results_fixture"),
    # url(r'^league/(?P<key>[a-z0-9]*)/latest/fixture/results/(?P<fixture>[0-9]*)/$', views.results_fixture, name="results_fixture"),

]
