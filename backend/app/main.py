from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, admin
from typing import Tuple, List 
import logging
import sys
import os

from .database import SessionLocal, engine, get_db, Database
from sqlalchemy.orm import Session

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
models.Base.metadata.create_all(bind=engine)

# Source: https://stackoverflow.com/questions/63069190/how-to-capture-arbitrary-paths-at-one-route-in-fastapi
# Created by Noah Cardoza
# Modified to use regular functions instead of async
class SinglePageApplication(StaticFiles):
    """Acts similar to the bripkens/connect-history-api-fallback
    NPM package."""

    def __init__(self, directory: os.PathLike, index="index.html") -> None:
        self.index = index

        # set html=True to resolve the index even when no
        # the base path is passed in
        super().__init__(directory=directory, packages=None, html=True, check_dir=True)

    def lookup_path(self, path: str) -> Tuple[str, os.stat_result]:
        """Returns the index file when no match is found.

        Args:
            path (str): Resource path.

        Returns:
            [tuple[str, os.stat_result]]: Always retuens a full path and stat result.
        """
        full_path, stat_result = super().lookup_path(path)

        # if a file cannot be found
        if stat_result is None:
            return super().lookup_path(self.index)

        return (full_path, stat_result)


app = FastAPI(
    title="System zarządzający wynikami w kręglarstwie klasycznym",
    openapi_url="/api/v1/openapi.json",
    redoc_url="/api/v1/redoc",
    docs_url="/api/v1/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add routes there

static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))


@app.get("/api/v1/bowling_alleys/", response_model=None)
def get_all_bowling_alleys(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[models.BowlingAlley]:
    print("Dupa!")
    bowling_alleys = db.query(models.BowlingAlley).offset(skip).limit(limit).all()
    return bowling_alleys

@app.get("/api/v1/bowling_alleys/{bowling_alley_id}", response_model=None)
def get_bowling_alley(bowling_alley_id: int, db: Session = Depends(get_db)) -> models.BowlingAlley:
    bowling_alley = db.query(models.BowlingAlley).filter(models.BowlingAlley.id == bowling_alley_id).first()
    if bowling_alley is None:
        raise HTTPException(status_code=404, detail="BowlingAlley not found")
    return bowling_alley


# GET all tournaments
@app.get("/api/v1/tournaments", response_model=None)
def get_all_tournaments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[models.Tournament]:
    tournaments = db.query(models.Tournament).offset(skip).limit(limit).all()
    return tournaments

# GET a specific tournament by ID
@app.get("/api/v1/tournaments/{tournament_id}", response_model=None) 
def get_tournament(tournament_id: int, db: Session = Depends(get_db)) -> models.Tournament:
    tournament = db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()
    if tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return tournament

# GET scores for a specific tournament by ID
@app.get("/api/v1/tournaments/{tournament_id}/scores", response_model=None)
def get_tournament_scores(tournament_id: int, db: Session = Depends(get_db)) -> list[models.TournamentScore]:
    tournament = db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()
    if tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")

    scores = db.query(models.TournamentScore).filter(models.TournamentScore.tournament_id == tournament.id).all()
    return scores


@app.get("/api/v1/training_scores", response_model=None)
def get_all_training_scores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    training_scores = db.query(models.TrainingScore).offset(skip).limit(limit).all()
    return training_scores

# POST a new training score
@app.post("/api/v1/training_scores")
def create_training_score(training_score_create: schemas.TrainingScoreCreate, db: Session = Depends(get_db)):
    # Create a new TrainingScore instance
    new_training_score = models.TrainingScore(**training_score_create.dict())

    # Save the new TrainingScore to the database
    db.add(new_training_score)
    db.commit()
    db.refresh(new_training_score)

    return new_training_score















# to na koncu debilu

app.mount("/admin/", WSGIMiddleware(admin.flask_app))
app.mount("/static/", StaticFiles(directory=static_path), name="static")
app.mount(path="/", app=SinglePageApplication(directory="dist"), name="SPA")
