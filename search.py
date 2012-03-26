import json
import sys
import urllib2

def search(queries):
    file_name = '/home/maverick/Twitter/finalosproj/breaking_news/search_results.txt'
    
    for query in queries:
        tweet_url='http://search.twitter.com/search.json?q='+query+'&rpp=1&locale=en&result_type=mixed'
        #print tweet_url
        f=urllib2.urlopen(tweet_url)
        #print tweet_url
        data=json.load(f)
	
        tweets=[]
        for i in range(0,len(data["results"])):
            tweet_info=query+","+data["results"][i]["metadata"]["result_type"]+","
            if(len(data["results"][i]["metadata"])==2):
                tweet_info=tweet_info+str(data["results"][i]["metadata"]["recent_retweets"])+","
            else:
                tweet_info=tweet_info+"0"+","
	    tweet_info=tweet_info+(data["results"][i]["text"])
            tweets.append(tweet_info)
            #print tweet_info 
        f = open(file_name, 'a')
        for tweet in tweets:
	    tweet = tweet.encode('ascii', 'ignore')
            f.write(tweet+'\n')
        f.close()
    
if __name__ == '__main__':
    queries=[]

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        queries.append(word)
    
    print queries
    #queries= [ queries[0], queries [1], queries [2]]
    search(queries)
