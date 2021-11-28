from app import app, db
from app.models import JobOffer, Prisoner, Qualification, Employment
from sqlalchemy import func, event
from datetime import date, timedelta
from flask import render_template, url_for, request, abort, redirect
from flask_login import login_required

def what_date_was(years_ago: int):
    today = date.today()
    return today - timedelta(years=years_ago)

@app.route("/experiments", methods=["GET"])
@login_required
def get_experiments():
    return render_template("experiments.html", salary=None)

@app.route("/experiments/get_average", methods=["POST"])
@login_required
def get_avarage_stakes_by_age():
    minimum_age = request.form.get("minimum_age")
    minimum_qualifications = request.form.get("minimum_qualifications")
    return redirect(
        url_for(f"get_jobs_by_salary", minimum_age=minimum_age, minimum_qualifications=minimum_qualifications)
    )


@app.route("/experiments/get_average/<minimum_age>/<minimum_qualifications>", methods=["GET"])
@login_required
def get_avarage_stakes_by_age(minimum_age, minimum_qualifications):
    salary = db.session.query(func.avg(JobOffer.hourly_rate).label('avarage salary'))\
        .join(Employment).join(JobOffer)\
        .groupby(Employment)\
        .filter(Prisoner.birth_date < what_date_was(minimum_age))\
        .having(func.count_(Prisoner.qualifications) >= minimum_qualifications)\
        .all()
    return render_template("experiments.html", salary=salary)

@app.route("/experiments/add_employment", methods=["POST"])
@login_required
def add_employment():
    employment_id = request.form.get("employment_id")
    joboffer_id = request.form.get("joboffer_id")
    employee_id = request.form.get("prisoner_id")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    prisoner = db.session.query(Prisoner).filter(Prisoner.id == employee_id)
    if prisoner is None:
        app.logger.error(f"No inmate with ID: {employee_id}")
        abort(404)
    joboffer = db.session.query(JobOffer).filter(JobOffer.id == joboffer_id)
    if joboffer is None:
        app.logger.error(f"No joboffer with ID: {joboffer_id}")
        abort(404)
    db.session.add(Employment(employment_id, joboffer_id, employee_id, start_date, end_date))
    prisoner.update({"hired": True})
    db.session.commit()
    return redirect(url_for("get_experiments"))