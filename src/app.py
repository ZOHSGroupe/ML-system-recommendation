from flask import Flask,request,render_template
from config import Config
import os
import numpy as np
import pandas
import sklearn
import pickle
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# import model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('minmaxscaler.pkl', 'rb'))

def get_data():
    pass
def consumer_data():
    pass
def producer_data():
    pass



producer = KafkaProducer(
 bootstrap_servers=['broker:29092'],
 max_block_ms=5000,
 value_serializer=lambda v: json.dumps(v).encode('ascii'),
 key_serializer=lambda v: json.dumps(v).encode('ascii')
)

consumer = KafkaConsumer(
 client_id = "client1",
 bootstrap_servers=['broker:29092'],
 value_deserializer = lambda v: json.loads(v.decode('ascii')),
 key_deserializer = lambda v: json.loads(v.decode('ascii')),
 max_poll_records = 10
)


#creating app flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>samir</h1>"






flask_port = os.environ.get('FLASK_PORT', '5000')
if __name__ == "__main__":
    app.secret_key = Config.SECRET_KEY
    app.run(host='0.0.0.0', port=flask_port, debug=True)
