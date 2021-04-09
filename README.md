# Momentary Bot

Momentary Bot is a twist on my Retweet Bot where you can perform the same functionality as my Retweet Bot, however, it is Momentary, hence the name. Momentary Bot is single-use, you will have to enter your API keys and the target of the bot every time you execute the script
## Python Library

Use the package manager [pip3](https://pypi.org/project/tweepy/) to install Tweepy.

```bash
pip3 install tweepy
```

## Code Snippet

```
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
```

## Copyright

<a class="copyrighted-badge" title="Copyrighted.com Registered &amp; Protected" target="_blank" href="https://www.copyrighted.com/work/SDN9EdkW1uqttNJe"><img alt="Copyrighted.com Registered &amp; Protected" border="0" width="125" height="25" srcset="https://static.copyrighted.com/badges/125x25/05_2_2x.png 2x" src="https://static.copyrighted.com/badges/125x25/05_2.png" /></a>

Momentary Bot is copyrighted by the Twitter user @60MilesPerHour, Momentary Bot is copyrighted (c) under copyrighted.com

I hereby grant you the downloader of my program to use this software free of charge. I the creator of this software grant you permission to use the mentioned software without restriction, however, you are hereby subject to the following conditions

- The software you download is provided as is without any such warranty of any kind. 

- You are forbidden to merchandise off of this software unless otherwise granted by me, the author of this software.

By downloading this software, you agree that i the issuer am not liable for any infringement, claims, damages, or any other liabilities, whether contracted or otherwise.

Contact @60MilesPerHour if you have any questions and i will try to answer them to the best of my ability.
