#!/usr/bin/env python

import time
from getpass import getpass
from textwrap import TextWrapper

import tweepy
import sys

import datetime, time
now = time.time()
future = now + 20




class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')
    current_tweet_count = 0
    file_name = '/home/maverick/Twitter/finalosproj/breaking_news/tweets_down.txt'
    tweet_list = []
    count = 0
    def on_status(self, status):
              
	if(time.time() > future):
            sys.exit()
		
	else:
	    	try:
			self.current_tweet_count = self.current_tweet_count + 1
		    	f = open(self.file_name, 'a')
		   	f.write(status.text+ '\n')
		    	f.close()
		    	#print '%s : %s'  % (self.current_tweet_count, status.text)
	        except:
		    	self.current_tweet_count = self.current_tweet_count - 1
		    	pass		
	
    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing Zzzzzz'


def gettweet():
    #username = raw_input('Twitter username: ')
    #password = getpass('Twitter password: ')
    stream = tweepy.Stream(tweepy.BasicAuthHandler('111_cj', 'Aa@123'), StreamWatcherListener(), timeout=None)
    stream.sample()


if __name__ == '__main__':
	#try:
       	gettweet()
	#print '\n i am here'	
	print then
	print datetime.datetime.now()
    	#except KeyboardInterrupt:
      		#print '\nGoodbye!'
