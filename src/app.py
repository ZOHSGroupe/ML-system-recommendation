from flask import Flask,request,render_template
from config import Config
import os
import numpy as np
import pandas
import sklearn
import pickle

# import model
# model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
# scaler_path = os.path.join(os.path.dirname(__file__), 'minmaxscaler.pkl')

# model = pickle.load(open(model_path, 'rb'))
# scaler = pickle.load(open(scaler_path, 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('minmaxscaler.pkl', 'rb'))


#creating app flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>samir</h1>"




flask_port = os.environ.get('FLASK_PORT', '5000')
if __name__ == "__main__":
    app.secret_key = Config.SECRET_KEY
    app.run(host='0.0.0.0', port=flask_port, debug=True)
