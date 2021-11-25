import logging

from app import app, db
from app.models import Prisoner, Employment, JobOffer
from sqlalchemy import func
from flask import render_template, redirect, url_for, abort, request

logging.basicConfig()
logger = logging.getLogger(__name__)


@app.route("/prisoners", methods=["GET"], strict_slashes=False)
def get_all_prisoners():
    prisoners = Prisoner.query.all()
    return render_template("prisoners.html", prisoners=prisoners)


@app.route("/prisoners", methods=["POST"])
def get_prisoners_by_field_redirect():
    fields = ["name", "surname", "position"]
    for field in fields:
        value = request.form.get(field)
        if value:
            return redirect(url_for(f"get_prisoners_by_{field}", value=value))
    return redirect(url_for(f"get_all_prisoners"))


@app.route("/prisoners/name/<value>", methods=["GET"])
def get_prisoners_by_name(value):
    query = db.session.query(Prisoner)
    prisoners = query.filter(func.lower(Prisoner.name) == value.lower())
    return render_template("prisoners.html", prisoners=prisoners)


@app.route("/prisoners/surname/<value>", methods=["GET"])
def get_prisoners_by_surname(value):
    query = db.session.query(Prisoner)
    prisoners = query.filter(func.lower(Prisoner.surname) == value.lower())
    return render_template("prisoners.html", prisoners=prisoners)


@app.route("/prisoners/position/<value>", methods=["GET"])
def get_prisoners_by_position(value):
    query = db.session.query(Prisoner).join(Employment).join(JobOffer)
    prisoners = query.filter(
        func.lower(JobOffer.job_title).contains(value.lower())
    ).all()
    return render_template("prisoners.html", prisoners=prisoners)
