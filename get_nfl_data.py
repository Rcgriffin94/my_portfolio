import pandas as pd
import datetime as dt

df = pd.read_csv('https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv')
df['gameday'] = pd.to_datetime(df['gameday']).dt.date
df.sort_values(by='gameday', ascending=False, inplace=True)

teams = {
    'Tampa Bay Buccaneers': 'TB',
    'Los Angeles Rams': 'LA',
    'Atlanta Falcons': 'ATL',
    'Buffalo Bills': 'BUF',
    'Chicago Bears': 'CHI',
    'Cincinnati Bengals': 'CIN',
    'Denver Broncos': 'DEN',
    'Jacksonville Jaguars': 'JAX',
    'Houston Texans': 'HOU',
    'Las Vegas Raiders': 'LV',
    'Minnesota Vikings': 'MIN',
    'New England Patriots': 'NE',
    'New York Giants': 'NYG',
    'Philadelphia Eagles': 'PHI',
    'Pittsburgh Steelers': 'PIT',
    'San Francisco 49ers': 'SF',
    'Carolina Panthers': 'CAR',
    'Cleveland Browns': 'CLE',
    'Green Bay Packers': 'GB',
    'Indianapolis Colts': 'IND',
    'Los Angeles Chargers': 'LAC',
    'Miami Dolphins': 'MIA',
    'Tennessee Titans': 'TEN',
    'New York Jets': 'NYJ',
    'Kansas City Chiefs': 'KC',
    'Washington Commanders': 'WAS',
    'Baltimore Ravens': 'BAL',
    'Dallas Cowboys': 'DAL',
    'New Orleans Saints': 'NO',
    'Arizona Cardinals': 'ARI',
    'Detroit Lions': 'DET',
    'Seattle Seahawks': 'SEA',
    'Oakland Raiders': 'OAK',   # legacy abbreviation
    'San Diego Chargers': 'SD', # legacy abbreviation
    'St. Louis Rams': 'STL'     # legacy abbreviation
}

def get_games():
    all_games = {}

    for team in teams:
        team_abv = teams[team]
        games = df[((df['home_team'] == team_abv) | (df['away_team'] == team_abv)) & (df['gameday'] <= dt.date.today())]
        all_games[team] = games
    
    return all_games