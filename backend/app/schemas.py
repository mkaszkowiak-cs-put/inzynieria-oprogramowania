from __future__ import annotations
from typing import ForwardRef, Optional, List, Any
from pydantic import BaseModel
from datetime import date
from . import models 

class TrainingScoreCreate(BaseModel):
    score: int
    date: date
    notes: Optional[str] = None
    private_notes: Optional[str] = None
    bowling_alley_id: Optional[int] = None

class TournamentScore(BaseModel):
    id: int
    score: int
    name: str
    surname: str
    tournament_id: int

    class Config:
        orm_mode = True

class TournamentCreate(BaseModel):
    name: str
    date_start: date
    date_end: date
    bowling_alley_id: int

class Tournament(BaseModel):
    id: int
    name: str
    date_start: date
    date_end: date
    finished: bool
    bowling_alley_id: int = None

    class Config:
        orm_mode = True

class BowlingAlley(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class TrainingScore(BaseModel):
    id: int
    score: int
    date: date
    notes: str
    private_notes: str
    bowling_alley_id: int = None 

    class Config:
        orm_mode = True
