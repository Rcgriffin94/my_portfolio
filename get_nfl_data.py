import pandas as pd
import datetime as dt
import numpy as np

teams = {
    'Tampa Bay Buccaneers': {'abv': 'TB', 'color': '#D50A0A'},  # Buccaneer Red
    'Los Angeles Rams': {'abv': 'LA', 'color': '#4169E1'},      # Royal Blue
    'Atlanta Falcons': {'abv': 'ATL', 'color': '#C60C30'},      # Red
    'Buffalo Bills': {'abv': 'BUF', 'color': '#1E50AC'},        # Blue
    'Chicago Bears': {'abv': 'CHI', 'color': '#0B162A'},        # Bears Blue
    'Cincinnati Bengals': {'abv': 'CIN', 'color': '#FF6600'},   # Brighter Orange
    'Denver Broncos': {'abv': 'DEN', 'color': '#FB4F14'},       # Orange
    'Jacksonville Jaguars': {'abv': 'JAX', 'color': '#00BFAE'}, # Teal
    'Houston Texans': {'abv': 'HOU', 'color': '#03202F'},       # Deep Steel Blue
    'Las Vegas Raiders': {'abv': 'LV', 'color': '#AAAAAA'},     # Silver
    'Minnesota Vikings': {'abv': 'MIN', 'color': '#9B4F96'},    # Brighter Purple
    'New England Patriots': {'abv': 'NE', 'color': '#1F4E79'},  # Brighter Blue
    'New York Giants': {'abv': 'NYG', 'color': '#1E3A77'},      # Brighter Navy
    'Philadelphia Eagles': {'abv': 'PHI', 'color': '#008C95'},  # Teal
    'Pittsburgh Steelers': {'abv': 'PIT', 'color': '#FFB612'},  # Gold
    'San Francisco 49ers': {'abv': 'SF', 'color': '#C8102E'},   # Red
    'Carolina Panthers': {'abv': 'CAR', 'color': '#00B0F0'},    # Bright Blue
    'Cleveland Browns': {'abv': 'CLE', 'color': '#311D00'},     # Brown
    'Green Bay Packers': {'abv': 'GB', 'color': '#4C9F38'},     # Green
    'Indianapolis Colts': {'abv': 'IND', 'color': '#004C97'},   # Blue
    'Los Angeles Chargers': {'abv': 'LAC', 'color': '#0072CE'}, # Blue
    'Miami Dolphins': {'abv': 'MIA', 'color': '#00BFC4'},       # Teal
    'Tennessee Titans': {'abv': 'TEN', 'color': '#4B92DB'},     # Titans Blue
    'New York Jets': {'abv': 'NYJ', 'color': '#127758'},        # Green
    'Kansas City Chiefs': {'abv': 'KC', 'color': '#E31837'},    # Red
    'Washington Commanders': {'abv': 'WAS', 'color': '#B02E4D'},# Burgundy
    'Baltimore Ravens': {'abv': 'BAL', 'color': '#361D7E'},     # Purple
    'Dallas Cowboys': {'abv': 'DAL', 'color': '#0054A6'},       # Blue
    'New Orleans Saints': {'abv': 'NO', 'color': '#F6BE00'},    # Gold
    'Arizona Cardinals': {'abv': 'ARI', 'color': '#97233F'},    # Red
    'Detroit Lions': {'abv': 'DET', 'color': '#0076B6'},        # Blue
    'Seattle Seahawks': {'abv': 'SEA', 'color': '#1C5C80'},     # Teal-Blue
    # Legacy teams
    'Oakland Raiders': {'abv': 'OAK', 'color': '#AAAAAA'},      # Silver
    'San Diego Chargers': {'abv': 'SD', 'color': '#0072CE'},    # Blue
    'St. Louis Rams': {'abv': 'STL', 'color': '#4169E1'},       # Royal Blue
}


def get_all_games():
    df = pd.read_csv('https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv')
    df['gameday'] = pd.to_datetime(df['gameday']).dt.date

    columns_to_keep = [
        'away_coach',
        'away_qb_name',
        'away_score',
        'away_team',
        'div_game',
        'game_type',
        'gameday',
        'gametime',
        'home_coach',
        'home_qb_name',
        'home_score',
        'home_team',
        'location',
        'overtime',
        'referee',
        'roof',
        'season',
        'stadium',
        'surface',
        'temp',
        'total',
        'week',
        'weekday',
        'wind'  
    ]
    
    all_games = {}

    for team in teams:
        team_abv = teams[team]['abv']
        games = df[((df['home_team'] == team_abv) | (df['away_team'] == team_abv)) & (df['gameday'] <= dt.date.today())]
        games = games[columns_to_keep]

        games["winner"] = np.where(
            games["home_score"] > games["away_score"], games["home_team"],
            np.where(games["away_score"] > games["home_score"], games["away_team"],
            "Tie")
        )

        all_games[team] = games

    return all_games