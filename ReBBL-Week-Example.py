#Rel Week Data

import BloodBowlAPI as bb
import pandas as pd

LEAGUE = 'Rebbl - Rel'
PLATFORM = 'pc'
DIVISIONS = ['Season 8 - Division 1','Season 8 - Division 2','Season 8 - Division 3',
             'Season 8 - Division 4','Season 8 - Division 5', 'Season 8 - Division 6',
             'Season 8 - Division 7','Season 8 - Division 9A',
             'Season 8 - Division 9B','Season 8 - Division 9C','Season 8 - Division 9D',
             'Season 8 - Division 9E']
#weeksplayed= ['1','2','3','4','5','6','7','8']
weeksplayed = ['9','10']
#
#DIVISIONS = [''Season 8 - Division 8'']
#weeksplayed= ['1']

'''
#Itterates through Divisions to pull match data, need to break out between rounds up to 13, range?
#Need to also break between played and scheduled and how that data is different
for DIV in divisions:
    week1 = pd.DataFrame()
    week1 = bb.contests(LEAGUE,DIV,PLATFORM,1,'played',100)
    print(week1)
'''

#week1p = bb.contests(LEAGUE,'Season 8 - Division 1',PLATFORM,9,'played',100)


match_prep = pd.DataFrame()
for WEEK in weeksplayed:
    for DIVISION in DIVISIONS:
        DF = pd.DataFrame([{'Week': WEEK, 'Division': DIVISION}])
        match_prep = match_prep.append(DF)
match_prep = match_prep.reset_index(drop=True)

list_of_matches = pd.DataFrame()
for INDEX, ROW in match_prep.iterrows():
    DF = bb.contests(LEAGUE,ROW['Division'],PLATFORM,ROW['Week'],'played',100)['upcoming_matches']
    for MATCH in DF:
        list_of_matches = list_of_matches.append(
                [{'Week': ROW['Week'], 'Division': ROW['Division'], 'match_uuid':MATCH['match_uuid']}], ignore_index=True)
list_of_matches = list_of_matches.reset_index(drop=True)

match_full_data = pd.read_pickle('C:/Users/PaulA/Documents/ReBBL_Season_Data.pkl')

for INDEX, ROW in list_of_matches.iterrows():
    game = bb.match(LEAGUE,PLATFORM,ROW['match_uuid'])
    game['week']=ROW['Week']
    match_full_data = match_full_data.append([{'data':game}])
match_full_data = match_full_data.reset_index(drop=True)


match_full_data.to_pickle('C:/Users/PaulA/Documents/ReBBL_Season_Data.pkl')


player_data = pd.DataFrame()
for X in match_full_data['data']:
    team1=pd.io.json.json_normalize(X['match']['teams'][0]['roster'])
    team1['Coach']=X['coaches'][0]['name']
    team1['match_id']=X['uuid']
    team1['Week']=X['week']
    team1['Competition']=X['match']['competitionname']
    team1['League']=X['match']['leaguename']
    team1['Team Name']=X['match']['teams'][0]['teamname']
    player_data = player_data.append(team1,ignore_index=True)
    
    team2=pd.io.json.json_normalize(X['match']['teams'][1]['roster'])
    team2['Coach']=X['coaches'][1]['name']
    team2['match_id']=X['uuid']
    team2['Week']=X['week']
    team2['Competition']=X['match']['competitionname']
    team2['League']=X['match']['leaguename']
    team2['Team Name']=X['match']['teams'][1]['teamname']
    player_data = player_data.append(team2,ignore_index=True)
player_data = player_data.reset_index(drop=True)
#player_data.to_csv('C:/Users/PaulA/Documents/ReBBL_Season_Player_Data_Test.csv', encoding='utf-8', index=False)
