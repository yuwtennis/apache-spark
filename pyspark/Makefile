
TOTAL_EXECUTOR_CORES := 3
EXECUTOR_CORES := 1
EXECUTOR_MEMORY := 1G
SPARK_MATER_HOST := 172.20.0.2
SPARK_DRIVER_HOST := 172.20.0.1

dir:
	hdfs dfs -fs hdfs://localhost:9000 -mkdir -p /data/json
	hdfs dfs -fs hdfs://localhost:9000 -mkdir -p /data/samples/wordcount
	hdfs dfs -fs hdfs://localhost:9000 -mkdir -p /shared/spark-logs
deploy: 
	nohup spark-submit \
		--name $(NAME) \
		--supervise \
		--packages=org.apache.hadoop:hadoop-aws:3.2.2 \
		--total-executor-cores $(TOTAL_EXECUTOR_CORES) \
		--executor-cores $(EXECUTOR_CORES) \
		--executor-memory $(EXECUTOR_MEMORY) \
		--master spark://$(SPARK_MATER_HOST):7077 \
		--conf spark.eventLog.enabled=true \
		--conf spark.eventLog.dir=hdfs://localhost:9000/shared/spark-logs \
		--conf spark.driver.host=$(SPARK_DRIVER_HOST) \
		$(NAME)/task.py > spark_submit_$(NAME)_$(shell date "+%Y_%m_%d_%H_%M_%S").log &
clean:
	hdfs dfs -fs hdfs://localhost:9000 -rm -r /data/results
