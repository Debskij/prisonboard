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
    db.session.add(
        Prisoner(100, "Jan", "Kowalski", "90101001123", 3.2, True, datetime(1990, 1, 1))
    )
    db.session.add(
        Prisoner(
            101, "Grzegorz", "Maliniak", "81273901223", 4.2, True, datetime(1996, 2, 1)
        )
    )
    db.session.add(
        Prisoner(
            102, "Anna", "Wożniak", "712364012923", 3.2, True, datetime(2010, 1, 1)
        )
    )
    db.session.add(
        Prisoner(
            103, "Józef", "Maliniak", "81098601223", 4.2, True, datetime(1996, 2, 1)
        )
    )
    db.session.add(
        Prisoner(
            104, "Grzegorz", "Wójcik", "90101002323", 3.2, True, datetime(1990, 1, 1)
        )
    )
    db.session.add(
        Prisoner(105, "Maria", "Daciuk", "81235601223", 4.2, True, datetime(1996, 2, 1))
    )
    
    db.session.add(SystemUser(200, "Adam", "Nowak", "adamos", "123456"))
    
    db.session.add(Qualification(100, "Plumbering", 3))
    db.session.add(Qualification(100, "CNC machinery", 4))
    
    db.session.add(Company(200, "ul. Jakaśtam 24, Warszawa", "Tiropolex sp. z o. o.", "Tiropolex"))
    db.session.add(Company(201, "ul. Zmyślona 14, Warszawa", "Google Ltd.", "Google"))
    
    db.session.add(JobOffer(300, 200, "Plumber", 15.5, 30))
    db.session.add(JobOffer(301, 201, "Tech guy", 15.5, 30))
    db.session.add(JobOffer(302, 201, "Lecturer", 15.5, 30))
    
    db.session.add(Employment(300, 100, datetime(2021, 1, 1), datetime(2021, 12, 1)))
    db.session.add(Employment(301, 101, datetime(2021, 3, 6), datetime(2021, 11, 7)))
    db.session.add(Employment(302, 102, datetime(2021, 5, 10), datetime(2021, 9, 11)))
    
    db.session.commit()
