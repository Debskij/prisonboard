from sqlalchemy.orm import relationship
from app import db

class SystemUser(db.Model):
    __tablename__ = "systemuser"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    assigned_person = relationship("Person", back_populates="assigned_user")

    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.password = password
    
    def __str__(self) -> str:
        return f"{self.__tablename__} id: {self.id} username: {self.username} password: {self.password}"