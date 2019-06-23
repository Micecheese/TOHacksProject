import praw

# name of bot in the praw.ini file
reddit = praw.Reddit('bot1')

# setting the subreddit we want to get information off of
subreddit = reddit.subreddit ("nba")

# Printing the information gathered using the Reddit RESTful api
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("------------------------\n")
