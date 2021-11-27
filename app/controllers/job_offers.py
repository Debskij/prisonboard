import logging

from app import app, db
from app.models import JobOffer, Company
from sqlalchemy import func
from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required


logging.basicConfig()
logger = logging.getLogger(__name__)


@app.route("/jobs", methods=["GET"], strict_slashes=False)
@login_required
def get_all_jobs():
    jobs = JobOffer.query.order_by(JobOffer.job_id).all()
    return render_template("job_offers.html", jobs=jobs)


@app.route("/jobs/<job_id>", methods=["GET", "POST"], strict_slashes=False)
@login_required
def get_job_by_id(job_id):
    query = JobOffer.query
    job_id = int(job_id)
    job = query.get(job_id)
    return render_template("job_offer.html", job=job)


@app.route("/jobs/delete/<job_id>", methods=["POST"])
@login_required
def delete_job_by_id(job_id):
    job_id = int(job_id)
    job_offer = db.session.query(JobOffer).filter(JobOffer.job_id == job_id).first()
    db.session.delete(job_offer)
    db.session.commit()
    return redirect(url_for("get_all_jobs"))


@app.route("/jobs", methods=["POST"])
@login_required
def get_jobs_by_field_redirect():
    fields = ["title", "company"]
    for field in fields:
        value = request.form.get(field)
        if value:
            return redirect(url_for(f"get_jobs_by_{field}", value=value))
    return redirect(url_for("get_all_jobs"))


@app.route("/jobs/title/<value>", methods=["GET"])
@login_required
def get_jobs_by_title(value):
    query = db.session.query(JobOffer)
    jobs = query.filter(func.lower(JobOffer.job_title).contains(value.lower()))
    return render_template("job_offers.html", jobs=jobs)


@app.route("/jobs/company/<value>", methods=["GET"])
@login_required
def get_jobs_by_company(value):
    query = db.session.query(JobOffer).join(Company)
    jobs = query.filter(func.lower(Company.full_name).contains(value.lower())).all()
    return render_template("job_offers.html", jobs=jobs)


@app.route("/jobs/hours", methods=["POST"])
@login_required
def get_jobs_by_hours_redirect():
    hours_from = request.form.get("from")
    hours_to = request.form.get("to")
    return redirect(
        url_for(f"get_jobs_by_hours", hours_from=hours_from, hours_to=hours_to)
    )


@app.route("/jobs/hours/<hours_from>/<hours_to>", methods=["GET"])
@login_required
def get_jobs_by_hours(hours_from, hours_to):
    query = db.session.query(JobOffer)
    jobs = query.filter(JobOffer.weekly_hours.between(hours_from, hours_to))
    return render_template("job_offers.html", jobs=jobs)


@app.route("/jobs/salary", methods=["POST"])
@login_required
def get_jobs_by_salary_redirect():
    salary_from = request.form.get("from")
    salary_to = request.form.get("to")
    return redirect(
        url_for(f"get_jobs_by_salary", salary_from=salary_from, salary_to=salary_to)
    )


@app.route("/jobs/salary/<salary_from>/<salary_to>", methods=["GET"])
@login_required
def get_jobs_by_salary(salary_from, salary_to):
    query = db.session.query(JobOffer)
    jobs = query.filter(JobOffer.hourly_rate.between(salary_from, salary_to))
    return render_template("job_offers.html", jobs=jobs)


@app.route("/jobs/edit/<job_id>", methods=["POST"])
@login_required
def edit_job_by_id(job_id):
    job_id = int(job_id)
    job_offer = db.session.query(JobOffer).filter(JobOffer.job_id == job_id)
    job_title = request.form.get("job_title")
    salary = request.form.get("salary")
    weekly_hours = request.form.get("weekly_hours")
    update_dict = {
        "job_title": job_title,
        "hourly_rate": salary,
        "weekly_hours": weekly_hours,
    }
    job_offer.update(update_dict)
    db.session.commit()
    return redirect(url_for("get_job_by_id", job_id=job_id))
