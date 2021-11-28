from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "login_get"
login_manager.init_app(app)

from .models import *
from .controllers import *


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return SystemUser.query.get(int(user_id))


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

    db.session.add(
        SystemUser(200, "Adam", "Nowak", "adamos", generate_password_hash("123456"))
    )
    db.session.add(
        SystemUser(201, "Admin", "Admin", "admin", generate_password_hash("admin"))
    )

    db.session.add(Qualification(100, "Plumbering", 3))
    db.session.add(Qualification(100, "CNC machinery", 4))
    db.session.add(Qualification(100, "Driving", 3))
    db.session.add(Qualification(101, "Speaking", 3))
    db.session.add(Qualification(101, "Playing games", 3))
    db.session.add(Qualification(102, "Java", 4))


    db.session.add(
        Company(200, "ul. Jakaśtam 24, Warszawa", "Tiropolex sp. z o. o.", "Tiropolex")
    )
    db.session.add(Company(201, "ul. Zmyślona 14, Warszawa", "Google Ltd.", "Google"))
    db.session.add(Company(202, "ul. Wall Street 23, New York", "Facebook Ltd.", "FB"))
    db.session.add(
        Company(203, "ul. Chłodna 26, Warszawa", "Intel Technology Poland", "Intel")
    )

    db.session.add(JobOffer(300, 200, "Plumber", 15, 30))
    db.session.add(JobOffer(301, 201, "Tech guy", 16, 40))
    db.session.add(JobOffer(302, 201, "Lecturer", 25, 40))
    db.session.add(JobOffer(303, 202, "Librarian", 7, 10))
    db.session.add(JobOffer(304, 202, "Chef", 18, 15))
    db.session.add(JobOffer(305, 203, "Programmer", 40, 20))

    db.session.add(
        Employment(400, 300, 100, datetime(2021, 1, 1), datetime(2021, 12, 1))
    )
    db.session.add(
        Employment(401, 301, 101, datetime(2021, 3, 6), datetime(2021, 11, 7))
    )
    db.session.add(
        Employment(402, 302, 102, datetime(2021, 5, 10), datetime(2021, 9, 11))
    )

    db.session.commit()
