import praw
import random


def get_thread(subreddits, limit):
    threads = r.get_subreddit(subreddits).get_hot(limit=limit)
    return random.choice([x for x in threads])


def get_comment(subreddits):
    comments_pool = r.get_comments(subreddits)
    flat_comments = praw.helpers.flatten_tree(comments_pool)
    return random.choice(flat_comments)


def build_tweet(thread, comment):
    tweet = '"' + thread.title + '" ' + comment.body
    if len(tweet) < 140:
        return tweet
    else:
        build_tweet(
            get_thread(subreddits, limit),
            get_comment(subreddits))

subreddits = 'news+uknews+worldnews'
limit = 100

r = praw.Reddit(
    user_agent='Python/PRAW:Random Comment Sampler:v1.0 (by /u/surprisetrex')

tweet = build_tweet(
            get_thread(subreddits, limit),
            get_comment(subreddits))

print(tweet)
