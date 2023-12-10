from espn_api.hockey import League
import pandas as pd


leagueID = None
espnS2 = None
SWID = None

league = League(league_id=leagueID, year=2024, espn_s2=espnS2, swid=SWID)

#statistical categories for skaters
SNAME = []
GP = []
G = []
A = []
PlusMinus = []
SOG = []
HIT = []
BLK = []
STP = []

#statisitcal categories for goalies
GNAME = []
GS = []
W = []
GA = []
SV = []
MIN = []
GAA = []
SVPercentage = []

#gets the stats for all players who are free agents
free_agents = league.free_agents(size = 1000)
for agent in free_agents:
    if "Total 2024" in agent.stats.keys():
        if "GS" in agent.stats["Total 2024"]["total"].keys():
            GNAME.append(agent.name)
            GS.append(agent.stats["Total 2024"]["total"]['GS'])
            W.append(agent.stats["Total 2024"]["total"]['W'])
            GA.append(agent.stats["Total 2024"]["total"]['GA'])
            SV.append(agent.stats["Total 2024"]["total"]['SV'])
            MIN.append(agent.stats["Total 2024"]["total"]['MIN ?'])
            GAA.append(agent.stats["Total 2024"]["total"]['GAA'])
            SVPercentage.append(agent.stats["Total 2024"]["total"]['SV%'])
        else:
            SNAME.append(agent.name)
            GP.append(agent.stats["Total 2024"]["total"]["GP"])
            G.append(agent.stats["Total 2024"]["total"]["G"])
            A.append(agent.stats["Total 2024"]["total"]["A"])
            PlusMinus.append(agent.stats["Total 2024"]["total"]["+/-"])
            SOG.append(agent.stats["Total 2024"]["total"]["SOG"])
            HIT.append(agent.stats["Total 2024"]["total"]["HIT"])
            BLK.append(agent.stats["Total 2024"]["total"]["BLK"])
            STP.append(agent.stats["Total 2024"]["total"]["STP"])

#gets the stats for all players rostered by fantasy team in league
teams = league.teams
for team in teams:
    for player in team.roster:
        if "Total 2024" in player.stats.keys():
            if "GS" in player.stats["Total 2024"]["total"].keys():
                GNAME.append(player.name)
                GS.append(player.stats["Total 2024"]["total"]['GS'])
                W.append(player.stats["Total 2024"]["total"]['W'])
                GA.append(player.stats["Total 2024"]["total"]['GA'])
                SV.append(player.stats["Total 2024"]["total"]['SV'])
                MIN.append(player.stats["Total 2024"]["total"]['MIN ?'])
                GAA.append(player.stats["Total 2024"]["total"]['GAA'])
                SVPercentage.append(player.stats["Total 2024"]["total"]['SV%'])
            else:
                SNAME.append(player.name)
                GP.append(player.stats["Total 2024"]["total"]["GP"])
                G.append(player.stats["Total 2024"]["total"]["G"])
                A.append(player.stats["Total 2024"]["total"]["A"])
                PlusMinus.append(player.stats["Total 2024"]["total"]["+/-"])
                SOG.append(player.stats["Total 2024"]["total"]["SOG"])
                HIT.append(player.stats["Total 2024"]["total"]["HIT"])
                BLK.append(player.stats["Total 2024"]["total"]["BLK"])
                STP.append(player.stats["Total 2024"]["total"]["STP"])

#creates two dictionaries of stats to be converted to CSV files
skaters = {'NAME': SNAME, 'GP': GP, 'G': G, 'A': A, '+/-': PlusMinus, 'SOG': SOG, 'HIT': HIT, 'BLK': BLK, 'STP': STP}
goalies = {'NAME': GNAME, 'GS': GS, 'W': W, 'GA': GA, 'SV': SV, 'MIN': MIN, 'GAA': GAA, 'SV%': SVPercentage}

#converts the dictionaries to pandas dataframes
skaterFrame = pd.DataFrame(skaters)
goalieFrame = pd.DataFrame(goalies)

#converts the dataframes to CSV files
skaterFrame.to_csv('skaters.csv')
goalieFrame.to_csv('goalies.csv')