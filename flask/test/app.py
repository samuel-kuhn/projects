#!/bin/python3
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get("name", "world")
    number = request.args.get("number", 3)
    date = datetime.now().strftime("%d.%m.%Y")
    double = float(number)*2
    return render_template("index.html", name=name, number=number, double=double, time=date)

app.run(host='0.0.0.0', port=80)
