#!/bin/python3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("street"):
        return render_template("failure.html")
    return render_template("success.html")


app.run(host="0.0.0.0", port=80) # 0.0.0.0 meaning every ip
