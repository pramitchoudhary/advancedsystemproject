#!/usr/bin/env python

from operator import itemgetter
import sys

current_title = None
current_pop_count=0
current_retw_count=0
title = None

for line in sys.stdin:
    line = line.strip()

    titles = line.split(",")
    title=titles[0]
    
    if(titles[1]=='popular'):
        count_1=1
    else:
        count_1=0

    count_2 = int(titles[2])
    
    if current_title == title:
        current_pop_count += count_1
        current_retw_count += count_2
    else:
        if current_title:
            print '%s\t%s' % (current_title, [current_pop_count,current_retw_count])
        current_pop_count = count_1
        current_retw_count = count_2
        current_title = title

if current_title == title:
    print '%s\t%s' % (current_title, [current_pop_count,current_retw_count])
