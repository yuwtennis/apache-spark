
from pyspark.sql import SparkSession

def save(row):
    # Send to target

def run():
    spark = SparkSession.builder.getOrCreate()

    df = spark\
             .read.format("binaryFile")\
             .option("pathGlobFilter", "*.jpg")\
             .load("hdfs://namenode:9000/data/s3/L8/*/*/*")

    rdd = df\
             .withColumn('path', regexp_replace('path', r'data', 'data2'))\
             .rdd

    rdd.map(save)

run()
