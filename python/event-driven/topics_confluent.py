from conflent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({"bootstrap_servers": "localhost:9092"})
topic_list = []
topic_list.append(NewTopic("auction_topic", 1, 1))
admin_client.create_topics(topic_list)
