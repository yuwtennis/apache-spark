
# Overview

Project to test spark code.

# Deploy

## Pre Requisite

docker  
docker-compose

## Build platform

Docker compose is based on 2 repositories.

https://github.com/bitnami/bitnami-docker-spark  
https://github.com/big-data-europe/docker-spark

```
docker-compose up -d
```

## Deploy code
cd $APP_DIR
make deploy NAME=NAME_OF_APP
