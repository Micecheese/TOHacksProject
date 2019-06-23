import praw
import pdb
import re
import os
from nba_api.stats.endpoints import playercareerstats

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
for submission in subreddit.hot(limit=5):
    # Filtering out the threads we have already replied in using the .txt file
    if submission.id not in posts_replied_to:
        # Case insensitive search
        if re.search("Lebron James", submission.title, re.IGNORECASE):
            # What you want to reply with
            submission.reply(career.get_data_frames()[0])
            print("Bot replying to: ", submission.title)
            # Store the data id into the txt file to prevent double posting
            posts_replied_to.append(submission.id)

# Update the file with the data id
''' with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n") '''