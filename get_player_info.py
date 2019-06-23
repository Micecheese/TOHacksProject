from nba_api.stats.endpoints import playercareerstats, commonallplayers, commonplayerinfo

player_info = playercareerstats.PlayerCareerStats(player_id=2544)
df = player_info.get_data_frames()[0]
print(df)
df.to_csv('Stats.csv')




