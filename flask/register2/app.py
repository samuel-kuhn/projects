#!/bin/python3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Registered people
registered = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", registered=registered)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    street = request.form.get("street")
    if not name or not street:
        return render_template("failure.html")
    registered.append(f"{name} from {street}")
    return redirect("/registrants")


app.run(host="0.0.0.0", port=80) # 0.0.0.0 meaning every ip
