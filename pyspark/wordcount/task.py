
from pyspark import SparkContext, SparkConf

def run():
    conf = SparkConf()
    sc = SparkContext(conf=conf)

    text_file = sc.textFile("hdfs://namenode:9000/data/part-00000-b7403f4d-101d-4e2d-9356-f381a96903b3-c000.json")
    counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile("hdfs://namenode:9000/data/results")

run()
