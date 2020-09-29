# Momentary Bot is copyrighted by by the twitter user @60MilesPerHour, Momentary Bot is copyrighted (c) under copyrighted.com

# NO LOGS VERSION!

import sys
import time
import os
import tweepy

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
        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.retweet()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    else:
        sys.exit("you may only use values between 1 and 25")
main()
