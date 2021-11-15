from sqlalchemy.orm import relationship
from app import db

class Qualifications(db.Model):
    __tablename__ = "qualifications"

    prisoners_id = db.Column(db.Integer, db.ForeignKey('prisoner.id'), primary_key=True, autoincrement=True)
    skill = db.Column(db.String(128), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    assigned_prisoner = relationship("Prisoner", back_populates="qualifications")

    def __init__(self, skill: str, level: str) -> None:
        super().__init__()
        self.skill = skill
        self.level = level
    
    def __str__(self) -> str:
        return f"{self.__tablename__} prisoners id: {self.prisoners_id} skill: {self.skill} level: {self.level}"