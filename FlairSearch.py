import time

from dotenv import load_dotenv
import os
import praw


def main():
    load_dotenv()  # This line brings all environment variables from .env into os.environ
    reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                         client_secret=os.environ['CLIENT_SECRET'],
                         user_agent=os.environ['USER_AGENT'],
                         username=os.environ['REDDIT_USERNAME'],
                         password=os.environ['REDDIT_PASSWORD'], )
    subreddit = reddit.subreddit(os.environ['SUBREDDIT_NAME'])
    reddit.read_only = False
    getflairs(subreddit)


def getflairs(subreddit):
    for flair in subreddit.flair(limit=None):
        userName = flair['user'].name
        flairText = flair['flair_text']
        if flairText == os.environ['USER_FLAIR_TO_FIND']:
            print(flair)


if __name__ == "__main__":
    main()
