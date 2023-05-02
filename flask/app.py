#!/bin/python3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World" # or render_template("index.html")

app.run(host="0.0.0.0", port=80) # 0.0.0.0 meaning every ip
