from kafka import KafkaConsumer
import json


def get_data():
    consumer = KafkaConsumer(
    bootstrap_servers=['broker:29092'],
    value_deserializer = lambda v: json.loads(v.decode('ascii')),
    key_deserializer = lambda v: json.loads(v.decode('ascii')),
    max_poll_records = 10
    )

    consumer.topics()
    consumer.subscribe(topics=['topic_name'])
    consumer.subscription()

    for message in consumer:
        print ("k=%s v=%s" % (message.key,message.value))

