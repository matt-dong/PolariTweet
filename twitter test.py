#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:37:48 2020

@author: mattdong03
"""
import json
import tweepy

### TWITTER API KEYS AND STUFF

api_key = "0bT8P7xI2ARoI56EoBM1GzIeT"
api_secret = "jtR1JyCLnAaIDcpwY1r8qpoVo7EaQMAtUfDZle0zvb49PIBgC7"
access_token = "1272587244407328771-RcSEjhsOyvGXG2eaTZn0En0x39ZffX"
access_secret = "AY6ROLZcCiJx8cj8cgiNgLftNF6lTy7vHJR5QS3gdT9Qt"

# authorization
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# choose tweet
name = 'realDonaldTrump'
tweet_id = '1273666793362673665'

# obtain replies
replies=[]
for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent').items(80):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)
            
# extract texts and convert to json
replies_text = []
for tweet in replies:
    replies_text.append(tweet.text)

# writes to json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(replies_text, f, ensure_ascii=False, indent=4)
    