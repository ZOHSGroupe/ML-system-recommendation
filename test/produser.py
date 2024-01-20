from kafka import KafkaProducer
import json
import time
import os

# Replace 'broker:29092' with your actual Kafka broker address
bootstrap_servers = 'broker:29092'
topic_name = os.environ.get('TOPIC_NAME')

def produce_test_data():
    producer = KafkaProducer(
        bootstrap_servers=[bootstrap_servers],
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
    )

    # Replace the following with your test data
    test_data = {
        "Seniority": 5,
        "Power": 150,
        "Cylinder_capacity": 130,
        "Value_vehicle": 15000,
        "N_doors": 4,
        "Type_fuel": "D",
        "Weight": 2
    }

    # Send test data to Kafka topic
    producer.send(topic=topic_name, key=str(time.time()), value=test_data)
    producer.flush()

if __name__ == "__main__":
    produce_test_data()
