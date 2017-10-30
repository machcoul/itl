from urllib2 import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

html = urlopen('https://www.betclic.fr/football/ligue-1-e4').read()
soup = BeautifulSoup(html,"html.parser")
print(soup.name)
# soup.find('div',attrs={"class":u"block-common block-player-programme"})
matches = soup.find_all("div", id=lambda value: value and value.startswith("match_"))
liste=[]
day_entrys = soup.find_all('div',attrs={"class":u"day-entry"})
for day_entry in day_entrys :
    date = day_entry['data-date']
    date = datetime.strptime(date, '%Y-%m-%d')
    matches = day_entry.find_all("div", id=lambda value: value and value.startswith("match_"))
    for match in matches :
        m = {}
        m['date'] = date
        teams = match['data-track-event-name'].split(" - ")
        m['homeTeam'] = teams[0]
        m['awayTeam'] = teams[1]
        # print(dir(match))
        odds = match.find_all('span',attrs={"class":u"odd-button "})
        m['odds'] ={}
        m['odds']['home']= float(odds[0].string.replace(',','.'))
        m['odds']['draw']= float(odds[1].string.replace(',','.'))
        m['odds']['away']= float(odds[2].string.replace(',','.'))
        liste.append(m)
print(liste)
