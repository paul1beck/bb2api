import BloodBowlAPI as bb
import pandas as pd

"""
matchData opens the existing match data for the preseason
"""
def matchData():
    matchdata = pd.read_csv('C:/Users/PaulA/Documents/BoTN_MatchData.csv')
    existing_match_data = []
    for INDEX, ROW in matchdata.iterrows():
        existing_match_data.append(ROW['match_id'])
    list_of_games = []
    pull_matches = bb.matches(LEAGUE='Blood of the Noobs',PLATFORM='xb1',
                          COMPETITION='preseason ladder',LIMIT=1000)
    for X in pull_matches['matches']:
        list_of_games.append(X['uuid'])
    list_of_games = list(set(list_of_games) - set(existing_match_data))
    if len(list_of_games)==0:
        return
    for X in list_of_games:
        game = bb.match(MATCH=X)
        team1=pd.io.json.json_normalize(game['match']['teams'][0]['roster'])
        team1['coach']=game['coaches'][0]['name']
        if game['match']['teams'][0]['score'] > game['match']['teams'][1]['score']:
            team1['final']='w'
        elif game['match']['teams'][0]['score'] == game['match']['teams'][1]['score']:
            team1['final']='d'
        else: team1['final']='l'
        team1['match_id']=game['uuid']
        team1['Competition']=game['match']['competitionname']
        team1['League']=game['match']['leaguename']
        team1['Team Name']=game['match']['teams'][0]['teamname']
        matchdata = matchdata.append(team1,ignore_index=True)
        
        team2=pd.io.json.json_normalize(game['match']['teams'][1]['roster'])
        team2['coach']=game['coaches'][1]['name']
        if game['match']['teams'][1]['score'] > game['match']['teams'][0]['score']:
            team2['final']='w'
        elif game['match']['teams'][0]['score'] == game['match']['teams'][1]['score']:
            team2['final']='d'
        else: team2['final']='l'
        team2['match_id']=game['uuid']
        team2['Competition']=game['match']['competitionname']
        team2['League']=game['match']['leaguename']
        team2['Team Name']=game['match']['teams'][1]['teamname']
        matchdata = matchdata.append(team2,ignore_index=True)       
    matchdata.to_csv('C:/Users/PaulA/Documents/BoTN_MatchData.csv', encoding='utf-8', index=False)

def coachData():
    teamlist = bb.teams(COMPETITION='preseason ladder',LIMIT=200,
             LEAGUE='Blood of the Noobs',PLATFORM='xb1')
    coach_data = pd.DataFrame()
    for X in teamlist['teams']:
        team_info = pd.io.json.json_normalize(bb.team(TEAMNAME=X['team'], PLATFORM='xb1',LIMIT=100)['team'])
        team_info['Coach']=X['coach']
        team_info['Competition']='preseason ladder'
        team_info['Race']=X['race']
        coach_data = coach_data.append(team_info,ignore_index=True)
    coach_data.to_csv('C:/Users/PaulA/Documents/BoTN_CoachData.csv', encoding='utf-8', index=False)
