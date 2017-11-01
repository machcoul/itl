from urllib2 import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import psycopg2
import csv

start = datetime.now()
print start.strftime("%Y-%m-%d %H:%M:%S"),__file__,'starting'

conn = psycopg2.connect("host=db dbname=postgres user=postgres password=postgres")
c = conn.cursor()



with open('/cron/data/competitions.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    competitions = [row for row in reader]

for competition in competitions :
    sql = """
        INSERT INTO myapp_competitions(id,oddsurl)
        VALUES(%(id)s,%(url)s)
        ON CONFLICT (id) do
        UPDATE SET
            oddsurl = %(url)s"""
    c.execute(sql, competition)
conn.commit()

with open('/cron/data/teams.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    teams = [row for row in reader]

for team in teams :
    sql = """
        INSERT INTO myapp_teams(id,oddsname)
        VALUES(%(id)s,%(name)s)
        ON CONFLICT (id) do
        UPDATE SET
            oddsname = %(name)s"""
    c.execute(sql, team)
conn.commit()

sql = "SELECT id,oddsurl FROM myapp_competitions WHERE oddsurl IS NOT NULL"
c.execute(sql)
competitions = c.fetchall()

for competition in competitions :
    competitionid = competition[0]
    url = competition[1]

    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    liste=[]
    day_entrys = soup.find_all('div',attrs={"class":u"day-entry"})
    for day_entry in day_entrys :
        date = day_entry['data-date']
        date = datetime.strptime(date, '%Y-%m-%d')
        matches = day_entry.find_all("div", id=lambda value: value and value.startswith("match_"))
        for match in matches :
            m = {}
            m['competitionid'] = competitionid
            m['date'] = date
            m['id'] = match['id']
            teams = match['data-track-event-name'].split(" - ")
            m['hometeam'] = teams[0]
            m['awayteam'] = teams[1]
            odds = match.find_all('span',attrs={"class":u"odd-button "})
            m['home']= float(odds[0].string.replace(',','.'))
            m['draw']= float(odds[1].string.replace(',','.'))
            m['away']= float(odds[2].string.replace(',','.'))
            liste.append(m)
            sql = "SELECT id FROM myapp_teams WHERE oddsname = '"+teams[0]+"'"
            c.execute(sql)
            hometeamid = c.fetchone()[0]
            sql = "SELECT id FROM myapp_teams WHERE oddsname = '"+teams[1]+"'"
            c.execute(sql)
            awayteamid = c.fetchone()[0]
            sql = "SELECT id FROM myapp_fixtures WHERE (status = 'TIMED' OR status = 'SCHEDULED') AND competitionid = '"+ str(competitionid) +"' AND hometeamid = '"+str(hometeamid)+"' AND awayteamid = '"+str(awayteamid)+"'"
            c.execute(sql)
            res = c.fetchone()
            if res :
                m['fixtureid'] = res[0]

    # print(liste)

    for match in liste :
        if 'fixtureid' in match :
            sql = """
                INSERT INTO myapp_fixtures(id,oddshome,oddsdraw,oddsaway)
                VALUES(%(fixtureid)s, %(home)s,%(draw)s,%(away)s)
                ON CONFLICT (id) do
                UPDATE SET
                    oddshome = %(home)s,
                    oddsdraw = %(draw)s,
                    oddsaway = %(away)s"""
            c.execute(sql, match)

        sql = """
            INSERT INTO myapp_odds(id, date,hometeam,awayteam,home,draw,away)
            VALUES(%(id)s, %(date)s,%(hometeam)s, %(awayteam)s, %(home)s,%(draw)s,%(away)s)
            ON CONFLICT (id) do
            UPDATE SET
                date = %(date)s,
                hometeam = %(hometeam)s,
                awayteam = %(awayteam)s,
                home = %(home)s,
                draw = %(draw)s,
                away = %(away)s"""
        c.execute(sql, match)

    conn.commit()
conn.close()

end = datetime.now()
delay = end-start
print end.strftime("%Y-%m-%d %H:%M:%S"),__file__,'terminated in',delay.total_seconds(),'s.'
