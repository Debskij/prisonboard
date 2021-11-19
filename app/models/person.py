from sqlalchemy.orm import relationship
from app import db

class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)

    assigned_user = relationship("SystemUser", back_populates="assigned_person", lazy='joined')
    assigned_prisoner = relationship("Prisoner", back_populates="assigned_person", lazy='joined')

    def __init__(self, name: str, surname: str) -> None:
        super().__init__()
        self.name = name
        self.surname = surname
    
    def __str__(self) -> str:
        return f"{self.__tablename__} id: {self.id} name: {self.name} surname: {self.surname}"