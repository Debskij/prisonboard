from sqlalchemy.orm import relationship
from app import db


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)

    def __init__(self, name: str, surname: str) -> None:
        super().__init__()
        self.name = name
        self.surname = surname

    def __init__(self, id: int, name: str, surname: str) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.surname = surname
