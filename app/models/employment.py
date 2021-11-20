from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app import db

class Employment(db.Model):
    __tablename__ = "employment"

    employment_id = db.Column(db.Integer, db.ForeignKey('joboffer.job_id'), primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('prisoner.id'), nullable=False)
    start_date = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    
    assigned_prisoner = relationship("Prisoner", back_populates="performed_work", lazy='joined')
    assigned_offer = relationship("JobOffer", back_populates="related_employment", lazy='joined')

    def __init__(self, employment_id: int, employee_id: int, start_date, end_date) -> None:
        super().__init__()
        self.employment_id = employment_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self) -> str:
        return f"{self.__tablename__} employment id: {self.employment_id} employee id: {self.employee_id} start_date: {self.start_date} end_date: {self.end_date}"