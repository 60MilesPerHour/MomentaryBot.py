# Momentary Bot is copyrighted by by the twitter user @60MilesPerHour, Momentary Bot is copyrighted (c) under copyright.com

import sys
import time
import os
import tweepy
import logging
import datetime

x = datetime.datetime.now()

LOG_FILENAME = 'TwitterBotLogs.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)


consumer_key = str(input("input consumer key: "))
consumer_secret = str(input("input consumer secret key: "))
access_token = str(input("input access token: "))
access_token_secret = str(input("input access token secret: "))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    search = str(input("input twitter user with @ symbol: "))

    numberofTweets = int(input("# of retweets: ")) #KEEP RETWEET NUMBER BELOW OR AT @ 25

    if numberofTweets <= 25:

        logging.debug('User Entered a # of: ' + numberofTweets + str(datetime.datetime.now()))

        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.retweet()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    else:
        logging.debug('User Entered a value above 25' + str(datetime.datetime.now()))
        sys.exit("you may only use values between 1 and 25")
main()