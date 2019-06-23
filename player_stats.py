from nba_api.stats.endpoints import playercareerstats, commonallplayers, commonplayerinfo
import pandas


def points_per_game(id):
    player_info = playercareerstats.PlayerCareerStats(player_id=id)
    df = player_info.get_data_frames()[0]
    #df.to_csv('Stats.csv')

    read_df = pandas.read_csv('Stats.csv')
    print(read_df)

    raw_values = read_df.sum(axis = 0, skipna=True)

    print(raw_values.iloc[7])

    total_points = raw_values.iloc[27]
    total_games = raw_values.iloc[7]
    return round(total_points/total_games, 1)







