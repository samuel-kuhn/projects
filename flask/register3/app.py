#!/bin/python3
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        registered = list(reader)
    return render_template("registered.html", registered=registered)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    street = request.form.get("street")
    if not name or not street:
        return render_template("failure.html")
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((name, street))
    file.close()
    return render_template("success.html")


app.run(host="0.0.0.0", port=80) # 0.0.0.0 meaning every ip
