#!/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/") #python decorator
def index():
    return "Es hat geklappt!"


app.run(host="0.0.0.0", port=80) #ip 0.0.0.0 meaning all adresses
