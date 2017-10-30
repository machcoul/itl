from django.db import models

# Create your models here.


class Competitions(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    caption = models.CharField(max_length=100)
    league = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    logo = models.CharField(max_length=100,null=True)

class Fixtures(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    status = models.CharField(max_length=30,null=True)
    hometeamname = models.CharField(max_length=100,null=True)
    matchday = models.PositiveIntegerField(null=True)
    hometeamid = models.PositiveIntegerField(null=True)
    goalsawayteam = models.PositiveIntegerField(null=True)
    goalshometeam = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(null=True)
    competitionid = models.PositiveIntegerField(null=True)
    awayteamname = models.CharField(max_length=100,null=True)
    halftimegoalsawayteam = models.PositiveIntegerField(null=True)
    halftimegoalshometeam = models.PositiveIntegerField(null=True)

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
