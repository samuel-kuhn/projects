#!/bin/python3
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("name")
    if username == "Samuel" and request.form.get("password") == "password123":
        return redirect(url_for("success", name = username ))
    else:
        return render_template("failure.html")

@app.route("/success") #passing of username not working yet
def success(name):
    return render_template("success.html", name = username)

app.run(host="0.0.0.0", port=80) # 0.0.0.0 meaning every ip
