import praw
import os
import get_player_name
import player_stats
from nba_api.stats.endpoints import playercareerstats
from update_player_list import update_player_list

# Update player name file
# update_player_list()

career = playercareerstats.PlayerCareerStats(player_id = 2544)

# Creating the Reddit instance
reddit = praw.Reddit('bot1')

# Creating a file by assuming that the file does not exist
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
# If the list has been created, it will have data on the text file showing what not to reply with
else:
    # Reading the file
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        # Newline the data
        posts_replied_to = posts_replied_to.split("\n")
        # filter out empty data (lines)
        posts_replied_to = list(filter(None, posts_replied_to))

# Setting the subreddit that we want to get the hot 5 posts in
subreddit = reddit.subreddit('NBAInfoBot')

# Getting the hot 5 posts on reddit
for submission in subreddit.new(limit=5):
    # Filtering out the threads we have already replied in using the .txt file
    if submission.id not in posts_replied_to:
        # Find active and inactive players in submission title
        active_players = get_player_name.get_active_player_name(submission.title)
        inactive_players = get_player_name.get_inactive_player_name(submission.title)
        # Reply to submissions with player data
        for player, player_id in active_players.items():
            reply = player + "\n\nPoints per game : " + str(player_stats.points_per_game(player_id)) + \
                "\n\nAssists per game : " + str(player_stats.assists_per_game(player_id)) + \
                "\n\nRebounds per game : " + str(player_stats.rebounds_per_game(player_id)) + \
                "\n\nMinutes per game : " + str(player_stats.minutes_per_game(player_id)) + \
                "\n\nFree throw percentage : " + str(player_stats.ft_percentage(player_id)) + \
                "\n\nField goal percentage : " + str(player_stats.fg_percentage(player_id))
            submission.reply(reply)
        for player, player_id in inactive_players.items():
            reply = player + "\n\nPoints per game : " + str(player_stats.points_per_game(player_id)) + \
                    "\n\nAssists per game : " + str(player_stats.assists_per_game(player_id)) + \
                    "\n\nRebounds per game : " + str(player_stats.rebounds_per_game(player_id)) + \
                    "\n\nMinutes per game : " + str(player_stats.minutes_per_game(player_id)) + \
                    "\n\nFree throw percentage : " + str(player_stats.ft_percentage(player_id)) + \
                    "\n\nField goal percentage : " + str(player_stats.fg_percentage(player_id))
            submission.reply(reply)

# Update the file with the data id
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")