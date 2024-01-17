from flask import Flask,request,render_template
from config import Config
import numpy as np
import pandas
import sklearn
import pickle

# import model

#creating app flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>samir</h1>"

if __name__ == "__main__":
    app.secret_key = Config.SECRET_KEY
    app.run(port=5000, debug=True)
