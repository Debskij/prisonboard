import logging

from app import app, db
from app.models import Prisoner, Employment, JobOffer, Company
from sqlalchemy import func
from flask import render_template, redirect, url_for, abort, request
from dataclasses import dataclass

logging.basicConfig()
logger = logging.getLogger(__name__)


@dataclass
class PrisonerQueryResult:
    prisoner: Prisoner
    company: Company
    
def get_prisoners_with_companies(prisoners_query_results):
    prisoners = []
    for prisoner in prisoners_query_results:
        companies_query = db.session.query(Company)
        company = companies_query.join(Company, JobOffer, Employment).join(JobOffer.related_employment).filter(Employment.employee_id == prisoner.id)
        prisoners.append(PrisonerQueryResult(prisoner, company))
    return prisoners

@app.route("/prisoners", methods=["GET"], strict_slashes=False)
def get_all_prisoners():
    prisoners_query_results = Prisoner.query.all()
    prisoners = get_prisoners_with_companies(prisoners_query_results)
    return render_template("prisoners.html", prisoners=prisoners)


@app.route("/prisoners", methods=["POST"])
def get_prisoners_by_field_redirect():
    fields = ["name", "surname", "company"]
    for field in fields:
        value = request.form.get(field)
        if value:
            return redirect(url_for(f"get_prisoners_by_{field}", value=value))
    return redirect(url_for(f"get_all_prisoners"))


@app.route("/prisoners/name/<value>", methods=["GET"])
def get_prisoners_by_name(value):
    query = db.session.query(Prisoner)
    prisoners_query_results = query.filter(func.lower(Prisoner.name) == value.lower())
    prisoners = get_prisoners_with_companies(prisoners_query_results)
    return render_template("prisoners.html", prisoners=prisoners)


@app.route("/prisoners/surname/<value>", methods=["GET"])
def get_prisoners_by_surname(value):
    query = db.session.query(Prisoner)
    prisoners_query_results = query.filter(func.lower(Prisoner.surname) == value.lower())
    prisoners = get_prisoners_with_companies(prisoners_query_results)
    return render_template("prisoners.html", prisoners=prisoners)


@app.route("/prisoners/company/<value>", methods=["GET"])
def get_prisoners_by_company(value):
    query = db.session.query(Prisoner).join(Employment).join(JobOffer).join(Company)
    prisoners_query_results = query.filter(
        func.lower(Company.full_name).contains(value.lower())
    ).all()
    prisoners = get_prisoners_with_companies(prisoners_query_results)
    return render_template("prisoners.html", prisoners=prisoners)
