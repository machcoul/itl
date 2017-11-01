# coding: utf8

#### modules

import json
import requests
import psycopg2
import csv

#### Settings

######## DB

conn = psycopg2.connect("host=db dbname=postgres user=postgres password=postgres")

######## files

dir = '/cron/data/'
competitions_file =  dir+'accastats_competitions.csv'
teams_file = dir+'accastats_teams.csv'

######## URL

URL='https://www.accastats.com/wp-admin/admin-ajax.php'

######## headers

headers ={}
headers['HOST']= 'www.accastats.com'
headers['User-Agent']= 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
headers['Accept']= '*/*'
headers['Accept-Language']= 'en-US,en;q=0.5'
headers['Accept-Encoding']= 'gzip, deflate, br'
headers['Referer']= 'https://www.accastats.com/'
headers['Content-Type']= 'application/x-www-form-urlencoded; charset=UTF-8'
headers['X-Requested-With']= 'XMLHttpRequest'
# headers['Content-Length']= '110'
# headers['Cookie']= '__cfduid=d9d8d6322c1a5e82e362a823200b77ac91509436188; _ga=GA1.2.385467669.1509436189; _gid=GA1.2.588452500.1509436189; bp-activity-oldestpage=1'

######## Post data
post = {'action':'get_bets','teams[]':'','favteamsonly':'false','rating':'0','date':'today'}

############ Leagues

#     0 -
#     1 -
#     2 - Belgium: Jupiler Pro League
#     3 - Croatia: 1. HNL
#     4 - Czech Republic: Synot Liga
#     5 - England: Championship
#     6 - England: Conference Premier
#     7 - England: League One
#     8 -
#     9 - England: Premier League
#     10 -
#     11 - France: Ligue 1
#     12 - Germany: Bundesliga
#     13 - Holland: Eredivisie
#     14 - Holland: Eerste Divisie
#     15 -
#     16 - Italy: Serie A
#     17 - Norway: Eliteserien
#     18 - Portugal: Primeira Liga
#     1 -
#     9 - England: Premier League
#     20 - Scotland: Championship
#     21 - Scotland: League One
#     22 - Scotland: League Two
#     23 - Scotland: Premiership
#     24 - Spain: Primera División
#     25 -
#     26 -
#     27 -
#     28 -
#     29 - Wales: Premier League
leagues = [11]

############ Market and bets

#     0 - Match Result : 0 - Home Win
#     0 - Match Result : 1 - Draw
#     0 - Match Result : 2 - Away Win
#     0 - Match Result : 3 - Home Win or Draw
#     0 - Match Result : 4 - Away Win or Draw
#     0 - Match Result : 5 - Home Win or Away Win
#     0 - Match Goals : 6 - Over 1.5 Goals
#     0 - Match Goals : 7 - Over 2.5 Goals
#     0 - Match Goals : 8 - Over 3.5 Goals
#     0 - Match Goals : 9 - Under 1.5 Goals
#     0 - Match Goals : 10 - Under 2.5 Goals
#     0 - Match Goals : 11 - Under 3.5 Goals
#     0 - Match Goals : 12 - Both Teams To Score - Yes
#     0 - Match Goals : 13 - Both Teams To Score - No
#     0 - Team Goals : 14 - Over 0.5 Home Goals
#     0 - Team Goals : 15 - Over 1.5 Home Goals
#     0 - Team Goals : 16 - Over 2.5 Home Goals
#     0 - Team Goals : 17 - Under 0.5 Home Goals
#     0 - Team Goals : 18 - Under 1.5 Home Goals
#     0 - Team Goals : 19 - Under 2.5 Home Goals
#     0 - Team Goals : 20 - Over 0.5 Away Goals
#     0 - Team Goals : 21 - Over 1.5 Away Goals
#     0 - Team Goals : 22 - Over 2.5 Away Goals
#     0 - Team Goals : 23 - Under 0.5 Away Goals
#     0 - Team Goals : 24 - Under 1.5 Away Goals
#     0 - Team Goals : 25 - Under 2.5 Away Goals
#     0 - Half Time Result : 26 - Half Time Home Win
#     0 - Half Time Result : 27 - Half Time Draw
#     0 - Half Time Result : 28 - Half Time Away Win
#     0 - Half Time Result : 29 - Half Time Home Win or Draw
#     0 - Half Time Result : 30 - Half Time Away Win or Draw
#     0 - Half Time Result : 31 - Half Time Home Win or Away Win
#     0 - Specials : 32 - Home Clean Sheet - Yes
#     0 - Specials : 33 - Home Clean Sheet - No
#     0 - Specials : 34 - Home To Win Both Halves
#     0 - Specials : 35 - Home To Score Both Halves
#     0 - Specials : 36 - Home Win & BTS
#     0 - Specials : 37 - Home Win To Nil
#     0 - Specials : 38 - Away Clean Sheet - Yes
#     0 - Specials : 39 - Away Clean Sheet - No
#     0 - Specials : 40 - Away To Win Both Halves
#     0 - Specials : 41 - Away To Score Both Halves
#     0 - Specials : 42 - Away Win & BTS
#     0 - Specials : 43 - Away Win To Nil
#     0 - Specials : 44 - No Match Goals
markets = [0]
bettypes = [0]

#### Processing

######## Getting data

data =[]

for league in leagues :

    for market in markets :

        for bettype in bettypes :

            post['market'] = market
            post['bettypes[]'] = bettype
            post['leagues[]'] = league

            r = requests.post(URL, headers=headers,data = post)
            fixtures = r.json()

            # print fixtures
            if len(fixtures) > 0 :
                for fixture in fixtures :
                    f ={}
                    f['id'] = fixture['Add To Basket Details'][1]
                    f['date']  = fixture['Date Sort']
                    f['competition'] = league
                    f['home'] = fixture['Home Short Name']
                    f['away'] = fixture['Away Short Name']
                    f['market'] = market
                    f['bettype'] = bettype
                    f['pred'] = float(fixture['Pred Stat'])
                    f['odd'] = fixture['Add To Basket Details'][6]
                    data.append(f)
                    # print fixture
                    # print date,league,competition_name,fixture['Home Short Name'],fixture['Away Short Name'],fixture['Pred Stat'],market_name,bettype_name,odd
            print str(league)+";"+fixture['Add To Basket Details'][2]
            # print league,bettype

######## load data

c = conn.cursor()

############ load Competitions

with open(competitions_file) as f:
    reader = csv.DictReader(f, delimiter=';')
    competitions = [row for row in reader]

for competition in competitions :
    sql = """
        INSERT INTO myapp_competitions(id,accastats_id)
        VALUES(%(id)s,%(accastats_id)s)
        ON CONFLICT (id) do
        UPDATE SET
            accastats_id = %(accastats_id)s"""
    c.execute(sql, competition)
conn.commit()

############ load teams

with open(teams_file) as f:
    reader = csv.DictReader(f, delimiter=';')
    teams = [row for row in reader]

for team in teams :
    sql = """
        INSERT INTO myapp_teams(id,accastats_name)
        VALUES(%(id)s,%(accastats_name)s)
        ON CONFLICT (id) do
        UPDATE SET
            accastats_name = %(accastats_name)s"""
    c.execute(sql, team)
conn.commit()

############ load odds

for odd in data :
    # print odd['id']
    sql = """
        INSERT INTO myapp_accastats(id,date,competition,home,away,market,bettype,pred,odd)
        VALUES(%(id)s,%(date)s,%(competition)s,%(home)s,%(away)s,%(market)s,%(bettype)s,%(pred)s,%(odd)s)
        ON CONFLICT (id) do
        UPDATE SET
            date = %(date)s,
            competition = %(competition)s,
            home = %(home)s,
            away = %(away)s,
            market = %(market)s,
            bettype = %(bettype)s,
            pred = %(pred)s,
            odd = %(odd)s"""
    c.execute(sql, odd)
conn.commit()

# print fixtures[0]
