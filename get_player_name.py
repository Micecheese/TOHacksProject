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
    names_in_string = []

    # Find names in string
    for name in players['active_players']:
        if name.lower() in string.lower():
            names_in_string.append(name)

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
    names_in_string = []

    # Find names in string
    for name in players['inactive_players']:
        if name.lower() in string.lower():
            names_in_string.append(name)

    return names_in_string


if __name__ == "__main__":
    print(get_active_player_name('LeBron James'))
    print(get_inactive_player_name('Michael Jordan'))
