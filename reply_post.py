import praw
import pdb
import re
import os

# Creating the Reddit instance
reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        # Newline the data
        posts_replied_to = posts_replied_to.split("\n")
        # filter out empty data (lines)
        posts_replied_to = list(filter(None, posts_replied_to))

# getting the top 5 posts on reddit
subreddit = reddit.subreddit('pythonforengineers')

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:

        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Figma is a better language no cap")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)


with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")