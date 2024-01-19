from kafka import KafkaProducer
import json

def prod_data (a,b,c,d,e,f,g):
    producer = KafkaProducer(
        bootstrap_servers=['broker:29092'],
        max_block_ms = 5000,
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
    )
    producer.send(
        'topic_name',
        key={"id":1},
        value={""}
        )

    producer.flush()
