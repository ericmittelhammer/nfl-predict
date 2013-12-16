#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from lxml import etree
from StringIO import StringIO
import urllib2
import sys

teams = [
    {'team': 'BUF',
     'url': 'http://www.buffalobills.com/team/roster.html'},
    {'team': 'MIA',
     'url': 'http://www.miamidolphins.com/team/player-roster.html'},
    {'team': 'NE', 'url': 'http://www.patriots.com/team/roster.html'},
    {'team': 'NYJ', 'url': 'http://www.newyorkjets.com/team/roster.html'
     },
    {'team': 'BAL',
     'url': 'http://www.baltimoreravens.com/team/roster.html'},
    {'team': 'CIN', 'url': 'http://www.bengals.com/team/roster.html'},
    {'team': 'CLE',
     'url': 'http://www.clevelandbrowns.com/team/roster.html'},
    {'team': 'PIT', 'url': 'http://www.steelers.com/team/roster.html'},
    {'team': 'HOU',
     'url': 'http://www.houstontexans.com/team/roster.html'},
    {'team': 'IND', 'url': 'http://www.colts.com/team/roster.html'},
    {'team': 'JAX', 'url': 'http://www.jaguars.com/team/roster.html'},
    {'team': 'TEN',
     'url': 'http://www.titansonline.com/team/roster.html'},
    {'team': 'DEN',
     'url': 'http://www.denverbroncos.com/team/roster.html'},
    {'team': 'KC', 'url': 'http://www.kcchiefs.com/team/roster.html'},
    {'team': 'OAK', 'url': 'http://www.raiders.com/team/roster.html'},
    {'team': 'SD', 'url': 'http://www.chargers.com/team/roster.html'},
    {'team': 'DAL',
     'url': 'http://www.dallascowboys.com/team/roster.html'},
    {'team': 'NYG', 'url': 'http://www.giants.com/team/roster.html'},
    {'team': 'PHI',
     'url': ' http://www.philadelphiaeagles.com/team/roster.html'},
    {'team': 'WAS', 'url': 'http://www.redskins.com/team/roster.html'},
    {'team': 'CHI',
     'url': 'http://www.chicagobears.com/team/roster.html'},
    {'team': 'DET',
     'url': 'http://www.detroitlions.com/team/roster.html'},
    {'team': 'GB', 'url': 'http://www.packers.com/team/players.html'},
    {'team': 'MIN', 'url': 'http://www.vikings.com/team/roster.html'},
    {'team': 'ATL',
     'url': 'http://www.atlantafalcons.com/team/player-roster.html'},
    {'team': 'CAR', 'url': 'http://www.panthers.com/team/roster.html'},
    {'team': 'NO',
     'url': 'http://www.neworleanssaints.com/team/roster.html'},
    {'team': 'TB',
     'url': 'http://www.buccaneers.com/team-and-stats/roster.html'},
    {'team': 'AZ', 'url': 'http://www.azcardinals.com/team/roster.html'
     },
    {'team': 'STL', 'url': 'http://www.stlouisrams.com/team/roster.html'
     },
    {'team': 'SF', 'url': 'http://www.49ers.com/team/roster.html'},
    {'team': 'SEA', 'url': 'http://www.seahawks.com/team/roster.html'},
    ]

dbfile = 'nfl.db'

testteams = [{'team': 'PIT',
             'url': 'http://www.steelers.com/team/roster.html'}]


def fetch():
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS players;''')
    c.execute('''CREATE TABLE IF NOT EXISTS players
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name text,
                     position text,
                     height text,
                     weight text,
                     num text,
                     team text);''')
    for team in teams:
        html = urllib2.urlopen(team['url']).read()
        parser = etree.HTMLParser()
        doc = etree.parse(StringIO(html), parser)
        for player in doc.xpath('//div[contains(./@class, "game-roster")]//tr[not(th)]'):

            # print etree.tostring(player)

            num = player.find('td[@class="col-jersey"]').text.strip()
            name = player.find('td[@class="col-name"]/a/span').text.strip()
            position = player.find('td[@class="col-position"]').text.strip()
            height = player.find('td[@class="col-height"]').text.strip()
            weight = player.find('td[@class="col-weight"]').text.strip()
            c.execute('INSERT INTO players (name, position, height, weight, num, team) VALUES (?, ?, ?, ?, ?, ?)', 
                (name, position, height, weight, num, team['team'],))

    conn.commit()

            # print({'num': num, 'name': name, 'position': position, 'height': height, 'weight': weight, 'team': team['team']})

if __name__ == '__main__':
    func = sys.argv[1]
    if func == 'fetch':
        fetch()
    else:
        print 'nope'
