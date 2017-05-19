# -*- coding: utf-8 -*-
"""

@author: Vijay Penumarti <pvjdev@gmail.com>
"""

import json #Handle JSONs in Python
import os #Import for the clear command
from pymongo import MongoClient #Use Mongo to store the tweets

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#clear console by using clear()
clear = lambda: os.system('cls')

#the config object
config = json.load(open('development/local.json'))

#Twitter Credentials
TWITTER_CREDENTIALS = config["TWITTER_CREDENTIALS"]

#This is a basic listener that justs prints received tweets to stdout
class TweetListener(StreamListener):

    def on_data(self, data):
        client = MongoClient('localhost', 27017)

        #Database Name: anime_manga_tweets
        #Collection Name: tweets

        db = client.anime_manga_tweets #use anime DB

        datajson = json.loads(data) #Decode JSON

        db.tweets.insert(datajson)  #Insert into collection
        return True

    def on_error(self,status):
        print (status)

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    listen = TweetListener()
    auth = OAuthHandler(
        TWITTER_CREDENTIALS["APP_KEY"],
        TWITTER_CREDENTIALS["APP_SECRET"]
    )

    auth.set_access_token(
        TWITTER_CREDENTIALS["ACCESS_TOKEN"],
        TWITTER_CREDENTIALS["ACCESS_TOKEN_SECRET"]
    )

    stream = Stream(auth, listen)

    #This line filter Twitter Streams to capture data by the keywords: 'anime', 'manga'
    stream.filter(track=['anime','manga'])