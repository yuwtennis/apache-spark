
# Overview

Project to test spark code. Please refer to task.py for per application conditions.

# Design

## Network

Below will be image of network architecture when containers are deployed using docker-compose.
Ip address might vary depending on your environment.

![](imgs/network.png)

# Deploy

## Prerequisite

I have tested this repos on below container platform.

* docker 19.03.5 
* docker-compose 1.25.0, build 0a186604

## Build platform

```
docker-compose up --scale spark-worker=NUM_OF_WORKERS -d
```

## Deploy
cd $APP_DIR
make deploy NAME=NAME_OF_APP

## History server
```
start-history-server.sh --properties-file spark-history-server.conf
```

## How to make dependencies
```
pip install -t deps MODULES
cd deps
zip deps.zip .
```

# Spark Benchmark

I have my docker installed as below filesystem condition.
![](imgs/dockerroot.png)

Below will be sample result for spark benchmarking.

|App Name|Description|DataSet|Number of Datasets|Dataset size|Executor Cpus|Executore Memory|Duration|
|--------|-----------|-------|------------------|------------|-------------|----------------|--------|
|s3connect|Upload jpg imgs from hdfs to S3|[Landsat8](https://registry.opendata.aws/landsat-8/)|35193(small.jpg)|2907B - 18969B|1|1G|4.0h|
|s3connect|Upload jpg imgs from hdfs to S3|[Landsat8](https://registry.opendata.aws/landsat-8/)|35193(small.jpg)|2907B - 18969B|2|1G|2.5h|
|s3connect|Upload jpg imgs from hdfs to S3|[Landsat8](https://registry.opendata.aws/landsat-8/)|35193(small.jpg)|2907B - 18969B|3|1G|1.6h|
