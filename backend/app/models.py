from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UniqueConstraint, Date, CheckConstraint, Text
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    login = Column(String(80), unique=True)
    email = Column(String(120))
    password = Column(String(128))

    # Flask-Login integration
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username

class BowlingAlley(Base):
    __tablename__ = "bowling_alley"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tournaments = relationship("Tournament", back_populates="bowling_alley", lazy="dynamic")
    training_scores = relationship("TrainingScore", back_populates="bowling_alley", lazy="dynamic")
    
    def __str__(self):
        return f"<{self.id}> {self.name}"

class Tournament(Base):
    __tablename__ = "tournament"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    date_start = Column(Date)
    date_end = Column(Date)
    finished = Column(Boolean, default=False)

    # N-1 relationship with BowlingAlley
    bowling_alley_id = Column(Integer, ForeignKey("bowling_alley.id"), nullable=True)
    bowling_alley = relationship("BowlingAlley", back_populates="tournaments")

    scores = relationship("TournamentScore", back_populates="tournament")

    def __str__(self):
        return f"<{self.id}> {self.name}"

class TournamentScore(Base):
    __tablename__ = "tournament_score"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    score = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    # N-1 relationship with Tournament
    tournament_id = Column(Integer, ForeignKey("tournament.id"), nullable=False)
    tournament = relationship("Tournament", back_populates="scores")

    def __str__(self):
        return f"<{self.name} {self.surname}> {self.score}"


class TrainingScore(Base):
    __tablename__ = "training_score"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    score = Column(Integer, nullable=False)
    date = Column(Date)
    notes = Column(Text)
    private_notes = Column(Text)

    # N-1 relationship with BowlingAlley
    bowling_alley_id = Column(Integer, ForeignKey("bowling_alley.id"), nullable=True)
    bowling_alley = relationship("BowlingAlley", back_populates="training_scores")

    def __str__(self):
        return f"{self.score}"
