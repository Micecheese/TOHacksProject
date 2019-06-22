from nba_api.stats.static.players import get_active_players, get_inactive_players
from json import dumps

active_player_info = get_active_players()
inactive_player_info = get_inactive_players()

active_players = [info['full_name'] for info in active_player_info]
inactive_players = [info['full_name'] for info in inactive_player_info]

all_players = {'active_players' : active_players, 'inactive_players' : inactive_players}


