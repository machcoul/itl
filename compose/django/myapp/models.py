from django.db import models

# Create your models here.


class Competitions(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    caption = models.CharField(max_length=100,null=True)
    league = models.CharField(max_length=30,null=True)
    year = models.CharField(max_length=30,null=True)
    logo = models.CharField(max_length=100,null=True)
    oddsurl = models.CharField(max_length=200,null=True)
    accastats_id = models.PositiveIntegerField(null=True)


class Fixtures(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    status = models.CharField(max_length=30,null=True)
    # hometeamname = models.CharField(max_length=100,null=True)
    matchday = models.PositiveIntegerField(null=True)
    hometeamid = models.PositiveIntegerField(null=True)
    goalsawayteam = models.PositiveIntegerField(null=True)
    goalshometeam = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(null=True)
    competitionid = models.PositiveIntegerField(null=True)
    awayteamid = models.PositiveIntegerField(null=True)
    # awayteamname = models.CharField(max_length=100,null=True)
    halftimegoalsawayteam = models.PositiveIntegerField(null=True)
    halftimegoalshometeam = models.PositiveIntegerField(null=True)
    oddshome = models.FloatField(null=True)
    oddsdraw = models.FloatField(null=True)
    oddsaway = models.FloatField(null=True)

class Teams(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    shortname = models.CharField(max_length=30,null=True)
    cresturl = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=100,null=True)
    oddsname = models.CharField(max_length=30,null=True)
    accastats_name = models.CharField(max_length=30,null=True)

class Odds(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    date = models.DateTimeField(null=True)
    hometeam = models.CharField(max_length=100,null=True)
    awayteam = models.CharField(max_length=100,null=True)
    home = models.FloatField(null=True)
    draw = models.FloatField(null=True)
    away = models.FloatField(null=True)

class Accastats(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    date = models.DateTimeField(null=True)
    competition = models.PositiveIntegerField(null=True)
    home= models.CharField(max_length=30,null=True)
    away = models.CharField(max_length=30,null=True)
    market = models.PositiveIntegerField(null=True)
    bettype = models.PositiveIntegerField(null=True)
    pred = models.PositiveIntegerField(null=True)
    odd = models.FloatField(null=True)


# class OddsMapping(models.Model):
#     id =
#
# class Odds(models.Model):
#     date = models.DateTimeField(null=True)
#     hometeamname = models.CharField(max_length=100,null=True)
#     awayteamname = models.CharField(max_length=100,null=True)
#     homeodd = models.CharField(null=True)
#     drawodd = models.CharField(null=True)
#     awayodd = models.CharField(null=True)
