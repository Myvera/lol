# coding: utf-8

__author__ = 'Insung'


import urllib
import json
import time

def Date_Cal(a):
    hey = time.localtime(a)
    return time.strftime("%y/%m/%d %H:%M", hey)

def Error(newkey):
    a = urllib.urlopen("https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/"+newkey+"?api_key=70286ee1-aebb-47c7-8b9a-108728735e04").read()
    if a[:6] == '<html>':
        return 1
    else:
        return 0

class Infinite:
    def __init__(self, newkey):
        self.input = newkey
        self.url_name = "https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/"+newkey+"?api_key=70286ee1-aebb-47c7-8b9a-108728735e04"
        self.read_name = urllib.urlopen(self.url_name).read()
        self.obj = json.loads(self.read_name)
        self.id = self.obj[(newkey.lower()).decode('utf-8')]['id']
        self.str_id = str(self.id)

        self.match_history = "https://kr.api.pvp.net/api/lol/kr/v2.2/matchhistory/"+self.str_id+"?api_key=70286ee1-aebb-47c7-8b9a-108728735e04"
        self.game = "https://kr.api.pvp.net/api/lol/kr/v1.3/game/by-summoner/"+self.str_id+"/recent?api_key=70286ee1-aebb-47c7-8b9a-108728735e04"
        self.league = "https://kr.api.pvp.net/api/lol/kr/v2.5/league/by-summoner/"+self.str_id+"?api_key=70286ee1-aebb-47c7-8b9a-108728735e04"

        self.read_match_history = urllib.urlopen(self.match_history).read()
        self.read_game = urllib.urlopen(self.game).read()
        self.read_league = urllib.urlopen(self.league).read()

    def How_Many(self):
        obj = json.loads(self.read_game)
        m = 0
        for n in obj['games']:
            m += 1
        return m

    def Summoner_Level(self):
        obj = json.loads(self.read_name)
        return obj[(self.input.lower()).decode('utf-8')]['summonerLevel']

    def Create_Date(self, i):
        obj = json.loads(self.read_game)
        return Date_Cal(obj['games'][i]['createDate']/1000)

    def Champ(self, i):
        obj = json.loads(self.read_game)
        return obj['games'][i]['championId']

    def Play_Time(self, i):
        obj = json.loads(self.read_game)
        time = obj['games'][i]['stats']['timePlayed']
        minutes = time / 60
        seconds = time % 60
        return "%d분 %d초" % (minutes, seconds)

    def Kill(self, i):
        obj = json.loads(self.read_game)
        stats = obj['games'][i]['stats']
        if 'championsKilled' in stats:
            kill = obj['games'][i]['stats']['championsKilled']
        else:
            kill = 0
        if 'numDeaths' in stats:
            death = obj['games'][i]['stats']['numDeaths']
        else:
            death = 0
        if 'assists' in stats:
            assist = obj['games'][i]['stats']['assists']
        else:
            assist = 0
        return "%d / %d / %d" % (kill, death, assist)

    def KDA(self, i):
        obj = json.loads(self.read_game)
        stats = obj['games'][i]['stats']
        if 'championsKilled' in stats:
            kill = obj['games'][i]['stats']['championsKilled']
        else:
            kill = 0
        if 'numDeaths' in stats:
            death = obj['games'][i]['stats']['numDeaths']
        else:
            death = 0
        if 'assists' in stats:
            assist = obj['games'][i]['stats']['assists']
        else:
            assist = 0
        if death != 0:
            kda = (kill+assist)/float(death)
            return "%.2f" % kda
        else:
            return "Perfect"

    def Victory(self, i):
        obj = json.loads(self.read_game)
        return obj['games'][i]['stats']['win']

    def Item(self, i, m):
        obj = json.loads(self.read_game)
        stats = obj['games'][i]['stats']
        item = [0 for j in range(7)]

        if 'item'+str(m) in stats:
            item[m] = obj['games'][i]['stats']['item'+str(m)]
        else:
            item[m] = 0

        return item[m]

    def Summoner_Spell(self, i, m):
        obj = json.loads(self.read_game)
        spell = [0, 0]
        spell[m-7] = obj['games'][i]['spell'+str(m-6)]
        return spell[m-7]

    def League_Tier(self):
        if self.read_league:
            obj = json.loads(self.read_league)
            tier = obj[self.str_id][0]['tier']
            tier_dic = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
            for i in obj[self.str_id][0]['entries']:
                if i['playerOrTeamId'] == self.str_id:
                    return tier+'_%s' % tier_dic[i['division']]
        else:
            return 'unrank'
