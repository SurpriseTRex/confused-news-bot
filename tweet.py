import json
import requests
import re
import random
from bs4 import BeautifulSoup
from TwitterAPI import TwitterAPI


def post_tweet():
    consumer_key = 'WZlNC5ScS3fGKjnPFnWcyZnFA'
    consumer_secret = 'lCOs4IFJVgKM7s0Jc3HZWpA2amGSdP6JjvTZa1yLZMhCuzy0E3'
    access_token = '2967428775-exHsLd98CQBw4Wbz6GPxyupXaG5RWvnA2XVPJPG'
    access_secret = 'WumBq6sCFTJ0fbTbYETNEuXCKabh47c5IeCEV47oVqVCv'

    # api = TwitterAPI(
    #    consumer_key, consumer_secret, access_token, access_secret)
    # post = api.request('statuses/update', {'status':'Post Post'})
    # return post.status_code

# BITLY API
# KEY - R_33acc292e0b147679fc9a211f511b11d
# generic access token = efa6545a253cdf31124fdcd4e1ecda632112b7ac

headlines_url = 'http://www.bbc.co.uk/news/'
# Use THE SUN news comments.
comments_url = ''

page = requests.get(headlines_url)
soup = BeautifulSoup(page.content)

stories = soup.find_all('a', class_='story')

print(stories)

'''story = random.choice(stories)
story = story.text.replace('\n', '')
story = re.sub('^\d*:? *', '', story).strip()
story = re.sub('Watch*\d*:?\d*$', '', story)
story = re.sub(' *-* *\d* *Secs* *', '', story)

print(story)'''
