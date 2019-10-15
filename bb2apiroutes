from auth import BB2_AUTH
import requests


def layers():
    '''
    Layers is used to show all the API layers that are available. This exposes
    the methods for all future calls below. This also explains what data is
    required for each method call as well.
    '''
    return requests.get('http://web.cyanide-studio.com/ws/?key='+BB2_AUTH).json()


def coaches(LEAGUE='Rebbl - Rel',PLATFORM='pc',COMPETITION='',LIMIT=10):
    '''
    Uses coaches method to pull a list of coaches in a league. By adding
    competition, a more specific list is pulled. Competition is not required.
    '''
    METHOD = 'coaches'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'competition' : '', # default = all competitions from given league
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()


def matches(LEAGUE='Rebbl - Rel',PLATFORM='pc',COMPETITION='',LIMIT=10):
    '''
    Pulls matches up to the limit between the start and end date. This is used
    for ladder or league matches, but is less useful than the contests method.
    This is good for ladder, but less for week format leagues.

    Requires a value for competition, start, or end, or requires not passing
    a null value. Need to add logic to pass them in variables exist, or to
    ignore the parameters.
    '''
    METHOD = 'matches'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'competition' : COMPETITION, # optional []
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'limit': LIMIT,  # default 100, up to 10000 works?
        'bb': '2', # says Opus 1|2, unsure what that means, 2 seems to work
        'start': '2018-01-01', # default = 20 days ago, format YYYY-MM-DD
#        'end': '' # default = today, format YYYY-MM-DD
        }
    return requests.get(ROOT, params=REQUEST).json()


def teams(LEAGUE='Rebbl  -Rel',PLATFORM='pc',COMPETITION='',LIMIT=10):
    '''
    Pulls teams from the league and competition. It also has a competition
    breakout for the league selected in ['competitions']
    
    Team dictionary includes: team, coach, team id, description, logo, race, race_id, team name
    League dictionary includes: competitions names, league name and description
    '''
    METHOD = 'teams'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' % METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'competition' : COMPETITION, # default = all competitions from given league
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()


def ladder(LEAGUE='Cabalvision Official League', COMPETITION='Open Ladder', PLATFORM='pc', LIMIT=10):
    METHOD = 'ladder'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'competition' : COMPETITION, # default = Open Ladder
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()


def match(LEAGUE='Blood of the Noobs',PLATFORM='xb1',MATCH='12000f0c95'):
    '''
    Uses uuid to gather match information. Value can be found by matches,
    contests, or ladder.

    Returns coaches method information, match information that includes player
    breakout, and team descriptions. For coaches and teams, matches information
    that would be found using their methods.

    The match dictionary has league information, start/finish times.

    The match:teams dictionary has all the pregame inducement information, 
    game totals, and high level team information.

    The match:teams:roster dictionary has high level player information and attributes.
    This includes whether they got the MVP, SPP starting and gain for the game,
    and the skills and injuries the player may have had before the game.

    the match:teams:roster:stats has all the inflicted and received stats. Includes
    injuries, TDs, catches, passes for and against the player.
    '''
    METHOD = 'match'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'match_id': MATCH, # uses Match UUID
        'platform': PLATFORM, # pc, xb1, ps4
        'bb': '2', # says Opus 1|2, unsure what that means, 2 seems to work
        }
    return requests.get(ROOT, params=REQUEST).json()


def hof(LEAGUE='Rebbl - Rel', COMPETITION = '', PLATFORM='pc',LIMIT=10):
    METHOD = 'halloffame'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'competition' : COMPETITION, # default = Open Ladder, no value is all
        'exact': 1, # exact league name
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()


def contests(LEAGUE='Rebbl - Rel', COMPETITION = '', PLATFORM='pc', \
    ROUND=1, STATUS='played',LIMIT=10):
    '''
    The upcoming_matches dictionary has a list of matches in a competition by round
    
    Each match has league name and format, match_uuid, and high level coach/team info
    
    Contains image url location for logos, portraits, skills, and stadiums
    '''
    METHOD = 'contests'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'competition' : COMPETITION, # default = all, no value is all
        'exact': 1, # exact league name
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'round': ROUND,
        'status': STATUS, # scheduled|in_progress|played (default: sheduled)
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()

def contests2(LEAGUE,COMPETITION,PLATFORM,ROUND,STATUS,LIMIT=100):
    '''
    The upcoming_matches dictionary has a list of matches in a competition by round
    
    Each match has league name and format, match_uuid, and high level coach/team info
    
    Contains image url location for logos, portraits, skills, and stadiums
    '''
    METHOD = 'contests'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'competition' : COMPETITION, # default = all, no value is all
        'exact': 1, # exact league name
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'round': ROUND,
        'status': STATUS, # scheduled|in_progress|played (default: sheduled)
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()

def competitions(LEAGUE='Rebbl - Rel', PLATFORM='pc',LIMIT=100):
    '''
    Pulls the names of all competitions associated to a league.
    
    The competitions dictionary has competition names, creation dates, formats,
    and basic information about rules for the competition
    
    The competitions:leagues dictionary has the high level information including logo,
    date created, and number of registered teams.
    '''
    METHOD = 'competitions'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()

def team(TEAMNAME=':one: :punch: :Ogre:', PLATFORM='pc',LIMIT=100): #TEAMID = '353629'
    '''
    Pulls the most recent team roster, as well as high level team information.
    
    The team dictionary has non player purchases, coaches, cheerleaders, apoth, etc
    
    The team:roster dictionary has the list of current players
    
    The team:roster:player has the current attributes, injuries, skills, TV, and xp.
    '''
    METHOD = 'team'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
#        'id' : TEAMID, # not used if name is used
        'name': TEAMNAME, #team name
        'platform': PLATFORM, # pc, xb1, ps4
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()

def league(LEAGUE='Rebbl - Rel', PLATFORM='pc'):
    '''
    Pulls basic league information, name, logo, team counts.
    '''
    METHOD = 'league'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'league': LEAGUE, # default = Cabalvision Official League
        'platform': PLATFORM, # pc, xb1, ps4
        }
    return requests.get(ROOT, params=REQUEST).json()

def leagues(PLATFORM='pc',TEAMS=50,LIMIT=1000):
    '''
    Pulls all leagues from a platform.
    '''
    METHOD = 'leagues'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'platform': PLATFORM, # pc, xb1, ps4
        'teams': TEAMS, # default 1, states the minimum number of registered teams
        'limit': LIMIT  # default 100, up to 1000 works?
        }
    return requests.get(ROOT, params=REQUEST).json()

def replay(MATCH='12000f0c95',PLATFORM='xb1'):
    '''
    Uses uuid to gather match information based on the replay file for a game.
    This view is currently not available for all key holders. Could be interesting
    for future use.
    '''
    METHOD = 'replay'
    ROOT = 'http://web.cyanide-studio.com/ws/bb2/%s/' %METHOD
    REQUEST = {
        'key': BB2_AUTH, 
        'platform': PLATFORM, # pc, xb1, ps4
        'match_id': MATCH, # uses Match UUID
        'format': 'zip'
        }
    return requests.get(ROOT, params=REQUEST).json()
