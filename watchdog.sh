#!/bin/sh
path=/home/maverick/Twitter/finalosproj/breaking_news

counter=0

while [ $counter -lt 15 ]
#while []
do
 
  #truncate -s0 tweets_down.txt
  python $path/streamwatcher_p.py
  
  #truncate -s0 tweets_in.txt
  mv $path/tweets_down.txt $path/hdfs_in/tweets_in$counter.txt

  
  chmod 777 $path/hdfs_in/tweets_in$counter.txt

  # echo $counter
  counter=`expr $counter + 1`



   #/home/maverick/Twitter/2ndAttempt/./runHadoop.sh

  #sleep 5

done
