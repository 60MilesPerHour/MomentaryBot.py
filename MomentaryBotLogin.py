import sys
import logging
import datetime
import tweepy
import time
import os

x = datetime.datetime.now()

LOG_FILENAME = 'Logs.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

username = "Username"
password = "Password"

for i in range(2):
    usr = input("Username: ")
    i = 2
    if(usr == username):
        print("Username is correct!")
        break
    else:
        logging.debug('Failed User Login ' + str(datetime.datetime.now()))
        sys.exit("Please try again later")
        continue

for i in range(3):
    pwd = input("Password: ")
    j=3
    if(pwd == password):
        print("welcome!")
        logging.debug('Successful User Login ' + str(datetime.datetime.now()))

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

        break
    else:
        logging.debug('Failed User Login ' + str(datetime.datetime.now()))
        sys.exit("Please try again later")
        continue