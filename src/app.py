from flask import Flask,request,render_template
from config import Config
import os
import numpy as np
import pickle
from kafka import KafkaConsumer
# from kafka import KafkaProducer
import json
# from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from time import time


# Import model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('minmaxscaler.pkl', 'rb'))

bootstrap_servers = 'broker:29092'
predects =0


topic_name = os.environ.get('TOPIC_NAME',"recomendation")

def predect():
    consumer = KafkaConsumer(
        bootstrap_servers=[bootstrap_servers],
        value_deserializer=lambda v: json.loads(v.decode('ascii')),
        key_deserializer=lambda v: json.loads(v.decode('ascii')),
        max_poll_records=10
    )

    # Subscribe to the specified topic
    consumer.subscribe(topics=["samir"])

    # Fetch messages from the subscribed topic
    for message in consumer:
        # Process each message
        message_dict = {
            "key": message.key,
            "value": message.value
        }
        type_fuel_dict = {
            'P': 1,
            'D': 2
        }
        Seniority = message_dict['value']['Seniority']
        Power = message_dict['value']['Power']
        Cylinder_capacity = message_dict['value']['Cylinder_capacity']
        Value_vehicle = message_dict['value']['Value_vehicle']
        N_doors = message_dict['value']['N_doors']
        Type_fuel = type_fuel_dict[message_dict['value']['Type_fuel']]
        Weight = message_dict['value']['Weight']
        feature_list = [Seniority, Power, Cylinder_capacity, Value_vehicle, N_doors, Type_fuel, Weight]
        single_pred = np.array(feature_list).reshape(1, -1)
        scaled_features = scaler.transform(single_pred)
        final_pred = model.predict(scaled_features)
        insurance_dict = {
            0: 'Civil liability insurance',
            1: 'Insurance with Damage',
            3: 'Insurance with all risks'
        }
        if final_pred[0] in insurance_dict:
            insurance_type = insurance_dict[final_pred[0]]
            return insurance_type
        else:
            return "Sorry, we are not able to recommend this insurance."



# def producer_data():
#     producer = KafkaProducer(
#         bootstrap_servers=['broker:29092'],
#         max_block_ms=5000,
#         value_serializer=lambda v: json.dumps(v).encode('ascii'),
#         key_serializer=lambda v: json.dumps(v).encode('ascii')
#         )



app = Flask(__name__)

@app.route('/')
def index():
    result = predect()
    return f"<h1>{result}</h1>"


# Get Flask port from environment variable or use default value 5000
flask_port = os.environ.get('FLASK_PORT', '5000')

if __name__ == "__main__":
    app.secret_key = Config.SECRET_KEY
    app.run(host='0.0.0.0', port=flask_port, debug=True)

