from __future__ import annotations
from typing import ForwardRef, Optional
from pydantic import BaseModel
from datetime import date

class TrainingScoreCreate(BaseModel):
    score: int
    date: date
    notes: Optional[str] = None
    private_notes: Optional[str] = None
    bowling_alley_id: Optional[int] = None
