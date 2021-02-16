
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from functools import partial
import os

"""
Uploads png imgs from local to s3.

Required environment variables

AWS_ACCESS_KEY_ID: Access key id for AWS.
AWS_SECRET_ACCESS_KEY: Secret access key for AWS.
DATA_SOURCE: Binary datasource.
    https://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext.binaryFiles
"""

def upload_img_to_s3(row, aws_access_key_id, aws_secret_access_key):
    import boto3
    import io

    path = row.path
    data = row.content

    client = boto3.client(\
                 's3',\
                  aws_access_key_id=aws_access_key_id,\
                  aws_secret_access_key=aws_secret_access_key)

    s3_key = 'uploaded/'+path.split('/')[-1]

    fd = io.BytesIO(data)
    client.upload_fileobj(fd, 'ai-factory', s3_key)
    fd.close()

    return

def run():

    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    ds = os.getenv('DATA_SOURCE')

    conf = SparkConf()\
            .setAll([
                ('fs.s3a.access.key', aws_access_key_id),
                ('fs.s3a.secret.key', aws_secret_access_key),
            ])
    spark = SparkSession \
        .builder \
        .config(conf=conf) \
        .getOrCreate()

    imgs = spark.read.format("binaryFile").option("pathGlobFilter", "*small.jpg").load(ds)

    imgs.foreach(\
        partial(\
            upload_img_to_s3,\
            aws_access_key_id=aws_access_key_id,\
            aws_secret_access_key=aws_secret_access_key\
        )\
    )

run()
