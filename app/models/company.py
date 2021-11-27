from sqlalchemy.orm import relationship
from app import db


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(128), nullable=False)
    short_name = db.Column(db.String(128), nullable=False)

    job_offers = relationship("JobOffer", back_populates="company", lazy="select")

    def __init__(self, id: int, address: str, full_name: str, short_name: str) -> None:
        super().__init__()
        self.id = id
        self.address = address
        self.full_name = full_name
        self.short_name = short_name
