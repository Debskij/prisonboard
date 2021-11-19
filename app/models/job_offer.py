from sqlalchemy.orm import relationship
from app import db

class JobOffer(db.Model):
    __tablename__ = "joboffer"

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(128), nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    weekly_hours = db.Column(db.Integer, nullable=False)
    
    related_employment = relationship("Employment", back_populates="assigned_offer", lazy='select')

    def __init__(self, job_title: str, hourly_rate: float, weekly_hours: int) -> None:
        super().__init__()
        self.job_title = job_title
        self.hourly_rate = hourly_rate
        self.weekly_hours = weekly_hours

    def __str__(self) -> str:
        return f"{self.__tablename__} job id: {self.job_id} job title: {self.job_title} hourly rate: {self.hourly_rate} weekly hours: {self.weekly_hours}"