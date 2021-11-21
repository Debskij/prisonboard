from app import app
from flask import render_template


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")