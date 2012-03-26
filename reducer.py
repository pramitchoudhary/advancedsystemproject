#!/usr/bin/env python

from operator import itemgetter
import sys

current_title= None
current_count = 0
word = None


for line in sys.stdin:
    
    line = line.strip()

    # parse the input we got from mapper.py
    title, count = line.split('\t', 1)

    # convert title count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if current_title == title:
        current_count += count
    else:
        if current_title:
            if(current_count> 1):
                # write result to STDOUT
                print '%s\t%s' % (current_title, current_count)
                #max_so_far=current_count
        current_count = count
        current_title = title

# do not forget to output the last word if needed!
if current_title == title:
    print '%s\t%s' % (current_title, current_count)

