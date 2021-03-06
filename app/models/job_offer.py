from sqlalchemy.orm import relationship
from app import db


class JobOffer(db.Model):
    __tablename__ = "joboffer"

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    job_title = db.Column(db.String(128), nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    weekly_hours = db.Column(db.Integer, nullable=False)

    related_employment = relationship(
        "Employment", back_populates="assigned_offer", lazy="select"
    )
    company = relationship("Company", back_populates="job_offers", lazy="select")

    def __init__(
        self,
        job_id: int,
        company_id: int,
        job_title: str,
        hourly_rate: float,
        weekly_hours: int,
    ) -> None:
        super().__init__()
        self.job_id = job_id
        self.company_id = company_id
        self.job_title = job_title
        self.hourly_rate = hourly_rate
        self.weekly_hours = weekly_hours

    def __str__(self) -> str:
        return f"Job id: {self.job_id}, Title: {self.job_title}, Hourly rate: {self.hourly_rate}, Weekly hours: {self.weekly_hours}"
