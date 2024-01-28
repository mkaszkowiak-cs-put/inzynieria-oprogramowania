from abc import ABC, abstractmethod
from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas

from .database import SessionLocal, engine, get_db, Database
from sqlalchemy.orm import Session


class AbstractController(ABC):
    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def attach(self, app):
        pass

class BowlingAlleyRepository:
    def getAll(self, db, skip=0, limit=10):
        return db.query(models.BowlingAlley).offset(skip).limit(limit).all()

class GetBowlingAlleys(AbstractController):
    def call(self, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[models.BowlingAlley]:
        repository = BowlingAlleyRepository()
        bowling_alleys = repository.getAll(db, skip=skip, limit=limit)
        return bowling_alleys

    def attach(self, app):
        app.add_api_route("/api/v1/bowling_alleys/", endpoint=self.call, response_model=list[schemas.BowlingAlley])

class TournamentRepository:
    def getById(self, db, tournament_id: int):
        return db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()

    def getAll(self, db, skip=0, limit=10):
        return db.query(models.Tournament).offset(skip).limit(limit).all()
    
    def create(self, db, tournament_create):
        new_tournament = models.Tournament(**tournament_create.dict())
        db.add(new_tournament)
        db.commit()
        db.refresh(new_tournament)
        return new_tournament

class GetTournament(AbstractController):
    def call(self, tournament_id: int, db: Session = Depends(get_db)) -> models.Tournament:
        repository = TournamentRepository()
        tournament = repository.getById(db, tournament_id)
        if tournament is None:
            raise HTTPException(status_code=404, detail="Tournament not found")
        return tournament

    def attach(self, app):
        app.add_api_route("/api/v1/tournaments/{tournament_id}", endpoint=self.call, response_model=schemas.Tournament)

class CreateTournament(AbstractController):
    def call(self, tournament_create: schemas.TournamentCreate, db: Session = Depends(get_db)) -> models.Tournament:
        repository = TournamentRepository()
        new_tournament = repository.create(db, tournament_create)
        return new_tournament

    def attach(self, app):
        app.add_api_route("/api/v1/tournaments", endpoint=self.call, methods=["POST"], response_model=schemas.Tournament)

class GetTournaments(AbstractController):
    def call(self, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[models.Tournament]:
        repository = TournamentRepository()
        tournaments = repository.getAll(db, skip=skip, limit=limit)
        return tournaments

    def attach(self, app):
        app.add_api_route("/api/v1/tournaments", endpoint=self.call, response_model=list[schemas.Tournament])

class GetTournamentScores(AbstractController):
    def call(self, tournament_id: int, db: Session = Depends(get_db)) -> list[models.TournamentScore]:
        repository = TournamentRepository()
        tournament = repository.getById(db, tournament_id)
        if tournament is None:
            raise HTTPException(status_code=404, detail="Tournament not found")
        scores = db.query(models.TournamentScore).filter(models.TournamentScore.tournament_id == tournament.id).order_by(models.TournamentScore.score.desc()).all()
        return scores

    def attach(self, app):
        app.add_api_route("/api/v1/tournaments/{tournament_id}/scores", endpoint=self.call, response_model=list[schemas.TournamentScore])

class TrainingScoreRepository:
    def getById(self, db, training_score_id: int):
        return db.query(models.TrainingScore).filter(models.TrainingScore.id == training_score_id).first()

    def getAll(self, db, skip=0, limit=10):
        return db.query(models.TrainingScore).offset(skip).limit(limit).all()

    def create(self, db, training_score_create):
        new_training_score = models.TrainingScore(**training_score_create.dict())
        db.add(new_training_score)
        db.commit()
        db.refresh(new_training_score)
        return new_training_score
    
    def update(self, db, training_score_id, training_score_update):
        existing_training_score = self.getById(db, training_score_id)

        if existing_training_score:
            for key, value in training_score_update.dict(exclude_none=True).items():
                setattr(existing_training_score, key, value)
            db.add(existing_training_score)
            db.commit()
            db.refresh(existing_training_score)
            return existing_training_score
        else:
            raise HTTPException(status_code=404, detail="Training Score not found")

class GetTrainingScores(AbstractController):
    def call(self, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[models.TrainingScore]:
        repository = TrainingScoreRepository()
        training_scores = repository.getAll(db, skip=skip, limit=limit)
        return training_scores

    def attach(self, app):
        app.add_api_route("/api/v1/training_scores", endpoint=self.call, response_model=list[schemas.TrainingScore])

class CreateTrainingScore(AbstractController):
    def call(self, training_score_create: schemas.TrainingScoreCreate, db: Session = Depends(get_db)) -> models.TrainingScore:
        repository = TrainingScoreRepository()
        new_training_score = repository.create(db, training_score_create)
        return new_training_score

    def attach(self, app):
        app.add_api_route("/api/v1/training_scores", endpoint=self.call, methods=["POST"], response_model=schemas.TrainingScore)

class UpdateTrainingScore(AbstractController):
    def call(self, training_score_id: int, training_score_update: schemas.TrainingScoreUpdate, db: Session = Depends(get_db)) -> models.TrainingScore:
        repository = TrainingScoreRepository()
        updated_training_score = repository.update(db, training_score_id, training_score_update)
        return updated_training_score

    def attach(self, app):
        app.add_api_route("/api/v1/training_scores/{training_score_id}", endpoint=self.call, methods=["PATCH"], response_model=schemas.TrainingScore)
        app.add_api_route("/api/v1/training_scores/{training_score_id}", endpoint=self.call, methods=["PUT"], response_model=schemas.TrainingScore)
