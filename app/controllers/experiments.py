from app import app, db
from app.models import JobOffer, Prisoner, Qualification, Employment
from sqlalchemy import func, event
from datetime import date
from dateutil.relativedelta import relativedelta
from flask import render_template, url_for, request, abort, redirect
from flask_login import login_required
from time import time


def what_date_was(years_ago: int):
    today = date.today()
    return today - relativedelta(years=int(years_ago))

@app.route("/experiments", methods=["GET"])
@login_required
def get_experiments():
    return render_template("experiments.html", salary=None, time=None)

@app.route("/experiments/get_average", methods=["POST"])
@login_required
def get_average_redirect():
    minimum_age = request.form.get("minimum_age")
    minimum_qualifications = request.form.get("minimum_qualifications")
    return redirect(
        url_for(f"get_average", minimum_age=minimum_age, minimum_qualifications=minimum_qualifications)
    )

@app.route("/experiments/get_average/<minimum_age>/<minimum_qualifications>", methods=["GET"])
@login_required
def get_average(minimum_age, minimum_qualifications):
    t0 = time()
    salary = db.session.query(func.avg(JobOffer.hourly_rate).label('avg_salary'))\
            .join(Employment).join(Prisoner).join(Qualification)\
            .filter(Prisoner.birth_date < what_date_was(minimum_age))\
            .having(func.count_(Prisoner.qualifications) >= int(minimum_qualifications))\
            .group_by(Prisoner.id)\
            .subquery()
    better_salary = db.session.query(func.avg(salary.c.avg_salary)).scalar()
    end = time() - t0
    return render_template("experiments.html", salary=format(better_salary, '.2f'), time=end)

@app.route("/experiments/add_employment", methods=["POST"])
@login_required
def add_employment():
    t0 = time()
    employment_id = request.form.get("employment_id")
    joboffer_id = request.form.get("joboffer_id")
    employee_id = request.form.get("prisoner_id")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    prisoner = db.session.query(Prisoner).filter(Prisoner.id == employee_id)
    if prisoner is None:
        app.logger.error(f"No inmate with ID: {employee_id}")
        return abort(404)
    joboffer = db.session.query(JobOffer).filter(JobOffer.job_id == joboffer_id)
    if joboffer is None:
        app.logger.error(f"No joboffer with ID: {joboffer_id}")
        return abort(404)
    db.session.add(Employment(employment_id, joboffer_id, employee_id, start_date, end_date))
    prisoner.update({"hired": True})
    db.session.commit()
    end = time() - t0
    return render_template("experiments.html", salary=None, time=end)