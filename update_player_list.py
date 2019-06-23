from nba_api.stats.static.players import get_active_players, get_inactive_players
from json import dumps


def update_player_list():
    """
    Create or update JSON file (player_names) with active player names and inactive player names
    """
    # Get active player and inactive player info from nba_api
    active_player_info = get_active_players()
    inactive_player_info = get_inactive_players()

    # Filter through player info and retrieve only the names as a list
    active_players = {info['full_name']: info['id'] for info in active_player_info}
    inactive_players = {info['full_name']: info['id'] for info in inactive_player_info}

    # Create dictionary of active and inactive players
    all_players = {'active_players': active_players, 'inactive_players': inactive_players}

    # Write player names as JSON data to file
    with open('player_names.json', 'w+') as f:
        f.write(dumps(all_players))


if __name__ == "__main__":
    update_player_list()
