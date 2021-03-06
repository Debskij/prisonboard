from sqlalchemy.orm import relationship
from app import db
from app.models import Person


class Prisoner(Person):
    __tablename__ = "prisoner"

    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    pesel = db.Column(db.String(128), nullable=False, unique=True)
    avarage_ranking = db.Column(db.Float)
    hired = db.Column(db.Boolean, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)

    qualifications = relationship(
        "Qualification", back_populates="assigned_prisoner", lazy="joined"
    )
    performed_work = relationship(
        "Employment", back_populates="assigned_prisoner", lazy="joined"
    )

    def __init__(
        self,
        id: int,
        name: str,
        surname: str,
        pesel: str,
        avarage_ranking: float,
        hired: bool,
        birth_date,
    ) -> None:
        Person.__init__(self, id, name, surname)
        self.id = id
        self.pesel = pesel
        self.avarage_ranking = avarage_ranking
        self.hired = hired
        self.birth_date = birth_date

    def __str__(self) -> str:
        return f"{self.__tablename__} id: {self.id} pesel: {self.pesel} avarage ranking: {self.avarage_ranking} hired: {self.hired} birth date: {self.birth_date}"
