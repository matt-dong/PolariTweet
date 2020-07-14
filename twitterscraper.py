#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:03:59 2020

@author: mattdong03
"""

from twitterscraper import query_tweets

if __name__ == '__main__':
    list_of_tweets = query_tweets("Trump OR Clinton", 10)

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("Trump OR Clinton", 10):
        print(tweet)

    #Or save the retrieved tweets to file:
    file = open(“output.txt”,”w”)
    for tweet in query_tweets("Trump OR Clinton", 10):
        file.write(tweet.encode('utf-8'))
    file.close()