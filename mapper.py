#!/usr/bin/env python

import sys
stopwords=["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he",
"him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves",
"what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has",
"had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at",
"by","for","with","about","against","between","into","through","during","before","after","above","below","to","from",
"up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where",
"why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same",
"so","than","too","very","s","t","can","will","just","don","should","now","de","que","en","un","my","why","all","be","just","fix"]

def remove_stopwords(wl):
    for s in stopwords:
      for w in wl:
        if w == s:
          wl.remove(w)
    return wl

def filter_words(wl,rem_sw):
    for w in wl:
	if (len(w) <= 2 or len(w) >= 8):
 	    wl.remove(w)
    if rem_sw:
        wl = remove_stopwords(wl)
    return wl

for line in sys.stdin:
    line = line.strip()
    line=line.lower()
    tweettitles = line.split()
    tweettitles=filter_words(tweettitles,True)
    # increase counters
    for title in tweettitles:
        print '%s\t%s' % (title, 1)
