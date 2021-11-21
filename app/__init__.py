from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import *
from .controllers import *


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Prisoner(100, "Jan", "Kowalski", "90101001123", 3.2, True, datetime(1990, 1, 1)))
    db.session.add(SystemUser(200, "Adam", "Nowak", "adamos", "123456"))
    db.session.add(Qualifications(100, "Plumbering", 3))
    db.session.add(Qualifications(100, "CNC machinery", 4))
    db.session.add(JobOffer(300, "Plumber", 15.5, 30))
    db.session.add(Employment(300, 100, datetime(2021, 1, 1), datetime(2021, 12, 1)))
    db.session.commit()
