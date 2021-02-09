
TOTAL_EXECUTOR_CORES := 2
EXECUTOR_CORES := 1
EXECUTOR_MEMORY := 1G

dir:
	hdfs dfs -fs hdfs://localhost:9000 -mkdir -p /data/json
	hdfs dfs -fs hdfs://localhost:9000 -mkdir -p /data/samples/wordcount
deploy: 
	spark-submit \
		--name $(NAME) \
		--total-executor-cores $(TOTAL_EXECUTOR_CORES) \
		--executor-cores $(EXECUTOR_CORES) \
		--executor-memory $(EXECUTOR_MEMORY) \
		--master spark://localhost:7077 \
		wordcount.py
clean:
	hdfs dfs -fs hdfs://localhost:9000 -rm -r /data/results
