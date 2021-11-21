from app import app, db
from app.models import Prisoner
from flask import render_template, redirect, url_for, abort, request


@app.route("/qualifications", methods=["GET"])
def get_qualifications_no_selections():
    return redirect(url_for("index"))

@app.route("/qualifications", methods=["POST"])
def post_qualifications():
    prisoner_id = request.form['prisoner_id']
    return redirect(url_for("get_qualifications", prisoner_id=prisoner_id))

@app.route("/qualifications/<prisoner_id>", methods=["GET"])
def get_qualifications(prisoner_id):
    query = db.session.query(Prisoner)
    prisoner_id = int(prisoner_id)
    prisoner = query.get(prisoner_id)
    if prisoner is None:
        app.logger.error(f"No inmate with ID: {prisoner_id}")
        abort(404)
    return render_template("qualifications.html", prisoner=prisoner)

