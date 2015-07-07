import praw
import random
from TwitterAPI import TwitterAPI


def get_submission(subreddits, num):
    threads_gen = r.get_subreddit(subreddits).get_new(limit=num)
    return random.choice([x for x in threads_gen])


def get_comment(subreddits, num):
    comments_gen = r.get_comments(subreddits, limit=num)
    comments_list = [x for x in comments_gen]
    flat_comments = praw.helpers.flatten_tree(comments_list)
    return random.choice(flat_comments)


def post_tweet(tweet):
    con_key = 'WZlNC5ScS3fGKjnPFnWcyZnFA'
    con_secret = 'lCOs4IFJVgKM7s0Jc3HZWpA2amGSdP6JjvTZa1yLZMhCuzy0E3'
    acc_token = '2967428775-exHsLd98CQBw4Wbz6GPxyupXaG5RWvnA2XVPJPG'
    acc_secret = 'WumBq6sCFTJ0fbTbYETNEuXCKabh47c5IeCEV47oVqVCv'

    api = TwitterAPI(con_key, con_secret, acc_token, acc_secret)
    post = api.request('statuses/update', {'status': tweet})
    return post.status_code

r = praw.Reddit(
    user_agent='Python/PRAW:Random Comment Sampler:v1.0 by /u/surprisetrex')

subreddits = 'news+uknews+worldnews'
snark = random.choice((
    'Typical!', 'Hah!', 'Pfft.', 'Hmm.', 'Uh oh.',
    'Yeah right.', 'What next?', 'Obviously.'))

tweet = ''

while tweet == '' or len(tweet) > 140:
    submission = get_submission(subreddits, 500)
    comment = get_comment(subreddits, 100)
    tweet = '"' + submission.title + '" ' + snark + ' ' + comment.body

print(tweet)
post_tweet(tweet)
