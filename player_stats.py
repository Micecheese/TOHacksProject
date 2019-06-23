from nba_api.stats.endpoints import playercareerstats, commonallplayers, commonplayerinfo
import pandas


# Creates the csv file with the raw data
def make_csv(id):
    player_info = playercareerstats.PlayerCareerStats(player_id=id)
    df = player_info.get_data_frames()[0]
    df.to_csv('Stats.csv')
    read_df = pandas.read_csv('Stats.csv')
    raw_values = read_df.sum(axis=0, skipna=True)
    return raw_values


# Metric for points per game (career)
def points_per_game(id):
    raw_values = make_csv(id)
    total_points = raw_values.iloc[27]
    total_games = raw_values.iloc[7]
    return round(total_points/total_games, 1)


# Metric for assists per game (career)
def assists_per_game(id):
    raw_values = make_csv(id)
    total_assists = raw_values.iloc[22]
    total_games = raw_values.iloc[7]
    return round(total_assists/total_games, 1)


# Metric for rebounds per game (career)
def rebounds_per_game(id):
    raw_values = make_csv(id)
    total_rebounds = raw_values.iloc[21]
    total_games = raw_values.iloc[7]
    return round(total_rebounds/total_games, 1)


# Metric for minutes per game (career)
def minutes_per_game(id):
    raw_values = make_csv(id)
    total_minutes = raw_values.iloc[9]
    total_games = raw_values.iloc[7]
    return round(total_minutes/total_games, 1)


# Metric for steals per game (career)
def steals_per_game(id):
    raw_values = make_csv(id)
    total_steals = raw_values.iloc[23]
    total_games = raw_values.iloc[7]
    return round(total_steals/total_games, 1)


# Metric for free throw percentage (career)
def ft_percentage(id):
    raw_values = make_csv(id)
    ft_made = raw_values.iloc[16]
    ft_attempted = raw_values.iloc[17]
    return round(ft_made/ft_attempted, 3)


# Metric for field goal percentage (career)
def fg_percentage(id):
    raw_values = make_csv(id)
    fg_made = raw_values.iloc[10]
    fg_attempted = raw_values.iloc[11]
    return round(fg_made/fg_attempted, 3)


# Metric for three point percentage (career)
def tp_percentage(id):
    raw_values = make_csv(id)
    tp_made = raw_values.iloc[13]
    tp_attempted = raw_values.iloc[14]
    return round(tp_made/tp_attempted, 3)

