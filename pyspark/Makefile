
TOTAL_EXECUTOR_CORES := 2
EXECUTOR_CORES := 1
EXECUTOR_MEMORY := 1G

dir:
	hdfs dfs -fs hdfs://namenode:9000 -mkdir -p /data/json
	hdfs dfs -fs hdfs://namenode:9000 -mkdir -p /data/samples/wordcount
	hdfs dfs -fs hdfs://namenode:9000 -mkdir -p /shared/spark-logs
deploy: 
	spark-submit \
		--name $(NAME) \
		--total-executor-cores $(TOTAL_EXECUTOR_CORES) \
		--executor-cores $(EXECUTOR_CORES) \
		--executor-memory $(EXECUTOR_MEMORY) \
		--master spark://debian:7077 \
		--conf spark.eventLog.enabled=true \
		--conf spark.eventLog.dir=hdfs://namenode:9000/shared/spark-logs \
		$(NAME)/task.py
clean:
	hdfs dfs -fs hdfs://namenode:9000 -rm -r /data/results
