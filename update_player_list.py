from nba_api.stats.static.players import get_active_players, get_inactive_players
from json import dumps

active_player_info = get_active_players()
inactive_player_info = get_inactive_players()

active_players = [info['full_name'] for info in active_player_info]
inactive_players = [info['full_name'] for info in inactive_player_info]

active_players.sort()
inactive_players.sort()

all_players = {'active_players' : active_players, 'inactive_players' : inactive_players}

with open('player_names.json', 'w+') as f:
    f.write(dumps(all_players))

