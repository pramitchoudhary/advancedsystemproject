path=/home/maverick/Twitter/finalosproj/breaking_news
hdpath=/home/maverick/Twitter



rm  $path/out1.txt
rm  $path/out2.txt
rm  $path/search_results.txt
./hadoop fs -rmr $hdpath

./hadoop dfs -copyFromLocal $path/hdfs_in $hdpath/in
echo "copied tweets_in.txt into hdfs"

#rm $path/hdfs_in/*
#echo "removed files from shared memory"

start1=$(date +%s)
./hadoop jar /opt/hadoop/contrib/streaming/hadoop-streaming-1.0.0.jar -D mapred.map.tasks=8 -file $path/mapper.py -mapper $path/mapper.py -file $path/reducer.py -reducer $path/reducer.py -input $hdpath/in -output $hdpath/out
end1=$(date +%s)
diff=$(($end1 - $start1))
echo "map reduce-1 is done!! in $diff seconds"

./hadoop dfs -rm $hdpath/in/*
echo "removed tweets.txt file hdfs"

./hadoop dfs -copyToLocal $hdpath/out/ $path/
echo "copied output into local file system"

./hadoop dfs -rmr $hdpath/out
echo "removed output from hdfs"

ls -l $path/out/

sort -r -n -k2 $path/out/part-00000 >> $path/out1.txt
echo "most frequently used words are ready to use" 
rm -r $path/out



################################
#second map/reduce
################################

head $path/out1.txt | python $path/search.py
echo "created search"
head $path/search_results.txt

./hadoop dfs -copyFromLocal $path/search_results.txt $hdpath/in
echo "copied search_results.txt into hdfs"
start2=$(date +%s)
./hadoop jar /opt/hadoop/contrib/streaming/hadoop-streaming-1.0.0.jar -file $path/mapper1.py -mapper $path/mapper1.py -file $path/reducer1.py -reducer $path/reducer1.py -input $hdpath/in/search_results.txt -output $hdpath/out
end2=$(date +%s)
diff1=$(($end2-$start2))

echo "map reduce-2 done!! in $diff1 seconds"

./hadoop dfs -rm $hdpath/in/search_results.txt
echo "removed search_results.txt file hdfs"

./hadoop dfs -copyToLocal $hdpath/out/ $path/
echo "copied output into local file system"

./hadoop dfs -rmr $hdpath/out
echo "removed output from hdfs"

cat $path/out/part-00000 >> $path/out2.txt
rm -r $path/out

head $path/out2.txt
