from nba_api.stats.endpoints import playercareerstats, commonallplayers, commonplayerinfo
import pandas


def make_csv(id):
    player_info = playercareerstats.PlayerCareerStats(player_id=id)
    df = player_info.get_data_frames()[0]
    df.to_csv('Stats.csv')
    read_df = pandas.read_csv('Stats.csv')
    raw_values = read_df.sum(axis=0, skipna=True)
    return raw_values


def points_per_game(id):
    raw_values = make_csv(id)
    total_points = raw_values.iloc[27]
    total_games = raw_values.iloc[7]
    return round(total_points/total_games, 1)


def assists_per_game(id):
    raw_values = make_csv(id)
    total_assists = raw_values.iloc[22]
    total_games = raw_values.iloc[7]
    return round(total_assists/total_games, 1)


def rebounds_per_game(id):
    raw_values = make_csv(id)
    total_rebounds = raw_values.iloc[21]
    total_games = raw_values.iloc[7]
    return round(total_rebounds/total_games, 1)


def minutes_per_game(id):
    raw_values = make_csv(id)
    total_minutes = raw_values.iloc[9]
    total_games = raw_values.iloc[7]
    return round(total_minutes/total_games, 1)


def ft_percentage(id):
    raw_values = make_csv(id)
    ft_made = raw_values.iloc[16]
    ft_attempted = raw_values.iloc[17]
    return round(ft_made/ft_attempted, 3)


def fg_percentage(id):
    raw_values = make_csv(id)
    fg_made = raw_values.iloc[10]
    fg_attempted = raw_values.iloc[11]
    return round(fg_made/fg_attempted, 3)


print(points_per_game(202695))
print(assists_per_game(2544))
print(rebounds_per_game(202695))
print(minutes_per_game(2544))
print(ft_percentage(202695))
print(fg_percentage(202695))





