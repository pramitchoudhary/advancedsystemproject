#!/usr/bin/env python

import sys
import search
import string

#queries=["Cameron"]
#search.search(queries)
#print 'i am here'
#print queries
#sys.exit()

for line in sys.stdin:
      
    line = line.strip()
    #line = line.replace("#",' ')
    #line = line.replace("@",' ')
    #for i in range(0,len(data["results"])):
         #   tweet_info=query+","+data["results"][i]["metadata"]["result_type"]+","
          #  if(len(data["results"][i]["metadata"])==2):
           #     tweet_info=tweet_info+str(data["results"][i]["metadata"]["recent_retweets"])
            #else:
             #   tweet_info=tweet_info+"0"
            #tweets.append(tweet_info)
            #print tweet_info 
        #f = open(file_name, 'a')
        #for tweet in tweets:
         #   f.write(tweet+'\n')
        #f.close()
    words = line.split(",")
    try:
	if(string.find(words[3],words[0])!=-1):
		print words[0]+","+words[1]+","+words[2]
    except:
	pass
    print words[0]+","+words[1]+","+words[2]
    #subword = words[3].split()
    #for sword in subword:
	#if words[0] == sword:
		
