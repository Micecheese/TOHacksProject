from nba_api.stats.endpoints import playercareerstats, commonallplayers, commonplayerinfo
import pandas

def make_csv(id):
    player_info = playercareerstats.PlayerCareerStats(player_id=id)
    df = player_info.get_data_frames()[0]
    df.to_csv('Stats.csv')
    read_df = pandas.read_csv('Stats.csv')
    raw_values = read_df.sum(axis=0, skipna=True)
    print(raw_values)
    return raw_values


def points_per_game(id):
    raw_values = make_csv(id)
    total_points = raw_values.iloc[27]
    total_games = raw_values.iloc[7]
    return round(total_points/total_games, 1)

def assists_per_game(id):
    raw_values = make_csv(id)


print(points_per_game(202695))




