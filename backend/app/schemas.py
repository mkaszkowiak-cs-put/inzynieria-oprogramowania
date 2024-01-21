from __future__ import annotations
from typing import ForwardRef, Optional
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from datetime import date
from . import models 

class TrainingScoreCreate(BaseModel):
    score: int
    date: date
    notes: Optional[str] = None
    private_notes: Optional[str] = None
    bowling_alley_id: Optional[int] = None

Tournament = sqlalchemy_to_pydantic(models.Tournament)
BowlingAlley = sqlalchemy_to_pydantic(models.BowlingAlley)
TournamentScore = sqlalchemy_to_pydantic(models.TournamentScore)
TrainingScore = sqlalchemy_to_pydantic(models.TrainingScore)
