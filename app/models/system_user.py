from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import db
from app.models import Person


class SystemUser(Person, UserMixin):
    __tablename__ = "systemuser"

    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(
        self, id: int, name: str, surname: str, username: str, password: str
    ) -> None:
        Person.__init__(self, id, name, surname)
        self.id = id
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f"{self.__tablename__} id: {self.id} username: {self.username} password: {self.password}"
