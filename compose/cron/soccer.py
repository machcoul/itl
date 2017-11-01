# coding: utf-8

#
#
# # toutes les chaines sont en unicode (même les docstrings)
# from __future__ import unicode_literals
# #
# #
# # import http.client
from datetime import datetime
import json
import os

start = datetime.now()
print start.strftime("%Y-%m-%d %H:%M:%S"),__file__,'starting'




API_TOKEN = '743292b6b4f041c380822cccafd92c8a'
# connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': API_TOKEN, 'X-Response-Control': 'minified' }
# connection.request('GET', '/v1/competitions', None, headers )
# response = json.loads(connection.getresponse().read().decode('UTF-8','ignore'))
# # r=connection.getresponse().read().decode('ASCII')
# print (response)

# import urllib.request

#
# request = urllib.request.Request(url,headers=headers)
# response = urllib.request.urlopen(request)
#
# print (response.read().decode('ascii','ignore'))


# import urllib2
# req = urllib2.Request(url)
# # req.add_header('Referer', 'http://www.python.org/')
# r = urllib2.urlopen(req)
# print(r.read().decode('ascii'))

import requests
import sqlite3
import psycopg2

url_competitions = "http://api.football-data.org/v1/competitions"
url_nextfixtures = "http://api.football-data.org/v1/fixtures?timeFrame=n30"
url_pastfixtures = "http://api.football-data.org/v1/fixtures?timeFrame=p30"


r = requests.get(url_competitions, headers= headers)
r.encoding = 'utf-8'
leagues = r.json()

r = requests.get(url_nextfixtures, headers = headers)
r.encoding = 'utf-8'
nextfixtures = r.json()

r = requests.get(url_pastfixtures, headers = headers)
r.encoding = 'utf-8'
pastfixtures = r.json()

fixtures = pastfixtures['fixtures'] + nextfixtures['fixtures']
# print(type(fixtures['fixtures']))
# print(fixtures['count'])
# print(fixtures['timeFrameStart'])
# print(fixtures['timeFrameEnd'])
#
#
# fixture=fixtures[0]
# for key, value in fixture.iteritems() :
#     print ( key, value )
# # _links = fixture['_links']
# # print(_links['awayTeam'])

# conn = sqlite3.connect('db.sqlite3')
conn = psycopg2.connect("host=db dbname=postgres user=postgres password=postgres")
c = conn.cursor()

for league in leagues :
    # c.execute("""INSERT OR IGNORE  INTO app_competitions(id, caption,league,year) VALUES(:id, :caption, :league, :year)""", league)
    sql = """
        INSERT INTO myapp_competitions(id, caption,league,year)
        VALUES(%(id)s, %(caption)s, %(league)s, %(year)s)
        ON CONFLICT (id) do
        UPDATE SET
            caption = %(caption)s,
            league = %(league)s,
            year = %(year)s"""
    c.execute(sql, league)
    conn.commit()

    url_teams = "http://api.football-data.org/v1/competitions/" + str(league['id']) + "/teams"
    r = requests.get(url_teams, headers= headers)
    r.encoding = 'utf-8'
    teams = r.json()
    if 'teams' in teams :
        for team in teams['teams'] :
            # print(league['id'],team)
            sql = """
                INSERT INTO myapp_teams(id,shortname,cresturl,name)
                VALUES(%(id)s, %(shortName)s, %(crestUrl)s,%(name)s)
                ON CONFLICT (id) do
                UPDATE SET
                    shortname = %(shortName)s,
                    cresturl = %(crestUrl)s,
                    name = %(name)s"""
            c.execute(sql, team)
        conn.commit()

# for fixture in fixtures['fixtures'] :
for fixture in fixtures :

    fixture['goalsAwayTeam'] = fixture['result']['goalsAwayTeam']
    fixture['goalsHomeTeam'] = fixture['result']['goalsHomeTeam']
    if 'halfTime' in fixture['result']:
        fixture['halfTimeGoalsAwayTeam'] = fixture['result']['halfTime']['goalsAwayTeam']
        fixture['halfTimeGoalsHomeTeam'] = fixture['result']['halfTime']['goalsHomeTeam']
    else :
        fixture['halfTimeGoalsAwayTeam'] = None
        fixture['halfTimeGoalsHomeTeam'] = None

    sql = """
        INSERT INTO myapp_fixtures(id, status,matchday,hometeamid,awayteamid,date,competitionid,goalsawayteam,goalshometeam,halftimegoalshometeam,halftimegoalsawayteam)
        VALUES(%(id)s, %(status)s, %(matchday)s,%(homeTeamId)s,%(awayTeamId)s,%(date)s,%(competitionId)s,%(goalsAwayTeam)s,%(goalsHomeTeam)s,%(halfTimeGoalsHomeTeam)s,%(halfTimeGoalsAwayTeam)s)
        ON CONFLICT (id) do
        UPDATE SET
            status = %(status)s,
            matchday = %(matchday)s,
            hometeamid = %(homeTeamId)s,
            awayteamid = %(awayTeamId)s,
            date = %(date)s,
            competitionid = %(competitionId)s,
            goalsawayteam = %(goalsAwayTeam)s,
            goalshometeam = %(goalsHomeTeam)s,
            halftimegoalshometeam = %(halfTimeGoalsHomeTeam)s,
            halftimegoalsawayteam = %(halfTimeGoalsAwayTeam)s"""
    c.execute(sql, fixture)
conn.commit()
conn.close()

#
#
# conn = sqlite3.connect('example.db')
# # conn.row_factory = sqlite3.Row#
# c = conn.cursor()
# c.execute("SELECT id FROM leagues")
# ids = c.fetchall()
# conn.close()
# for id in ids :
#     league_id =id[0]
#     print league_id

end = datetime.now()
delay = end-start
print end.strftime("%Y-%m-%d %H:%M:%S"),__file__,'terminated in',delay.total_seconds(),'s.'
