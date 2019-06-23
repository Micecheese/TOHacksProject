from json import load


def get_active_player_name(string):
    """
    Searches string for active NBA players

    :param string: look for NBA player names in string
    :return: list of NBA players in string
    """
    # Get names of NBA players from player_names.json
    try:
        with open('player_names.json', 'r') as f:
            players = load(f)
    except Exception as e:
        print(e)

    # List of names to be returned
    names_in_string = {}

    # Find names in string
    for player, player_id in players['active_players'].items():

        if player.lower() in string.lower():
            names_in_string[player] = player_id

    return names_in_string


def get_inactive_player_name(string):
    """
    Searches string for inactive NBA players

    :param string: look for NBA player names in string
    :return: list of NBA players in string
    """
    # Get names of NBA players from player_names.json
    try:
        with open('player_names.json', 'r') as f:
            players = load(f)
    except Exception as e:
        print(e)

    # List of names to be returned
    names_in_string = {}

    # Find names in string
    for player, player_id in players['inactive_players'].items():

        if player.lower() in string.lower():
            names_in_string[player] = player_id

    return names_in_string
