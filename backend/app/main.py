from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, admin, routes
from typing import Tuple, List 
from datetime import datetime
import logging
import sys
import os
from os import getenv
from faker import Faker
import random
from werkzeug.security import generate_password_hash
from .database import SessionLocal, engine, get_db, Database
from sqlalchemy.orm import Session

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Recreate the database tables, load fixtures on restart
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

username = getenv("ADMIN_USERNAME")
password = getenv("ADMIN_PASSWORD")
email = getenv("ADMIN_EMAIL")


hashed_password = generate_password_hash(password)
new_user = models.User(
    first_name="Administrator",
    last_name="The Great",
    login=username,
    email=email,
    password=hashed_password
)


bowling_alleys_data = [
    {"id": 1, "name": "Wronki"},
    {"id": 2, "name": "Leszno"},
    {"id": 3, "name": "Sieraków"},
    {"id": 4, "name": "Tarnowo Podgórne"},
    {"id": 5, "name": "Poznań"},
    {"id": 6, "name": "Łaziska Górne"},
    {"id": 7, "name": "Puck"},
    {"id": 8, "name": "Gostyń"},
]
tournaments_data = [
    {"id": 1, "name": "Mistrzostwa Polski Juniorów 2024", "bowling_alley_id": 5, "finished": False,
     "date_start": datetime(2024, 1, 20), "date_end": datetime(2024, 1, 28)},
    {"id": 2, "name": "4. Memoriał Ryszarda Bonka", "bowling_alley_id": 4, "finished": True,
     "date_start": datetime(2023, 1, 1), "date_end": datetime(2023, 1, 3)},
    {"id": 3, "name": "8. Puchar Starosty w Sierakowie", "bowling_alley_id": 3, "finished": True,
     "date_start": datetime(2023, 6, 11), "date_end": datetime(2023, 6, 15)},
]

fake = Faker(locale = 'pl_PL')

# Seed TournamentScore table
tournament_scores_data = []

for tournament_id in range(1, 4):  # Assuming you have tournaments with IDs 1, 2, and 3
    for _ in range(random.randint(5, 15)):
        #tournament_start_date = tournaments_data[tournament_id - 1]['date_start']
        #tournament_end_date = tournaments_data[tournament_id - 1]['date_end']
        score_data = {
            "score": random.randint(400, 650),
            #"notes": fake.text(),
            #"private_notes": fake.text(),
            "tournament_id": tournament_id,
            "name": fake.first_name(),
            "surname": fake.last_name(),
        }
        tournament_scores_data.append(score_data)

with SessionLocal() as db:
    # Add the new user to the database
    db.add(new_user)

    # Commit the changes
    db.commit()

    for alley_data in bowling_alleys_data:
        bowling_alley = models.BowlingAlley(**alley_data)
        db.add(bowling_alley)
    db.commit()
    
    for tournament_data in tournaments_data:
        tournament = models.Tournament(**tournament_data)
        db.add(tournament)
    db.commit()

    for score_data in tournament_scores_data:
        tournament_score = models.TournamentScore(**score_data)
        db.add(tournament_score)
    db.commit()

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


class AppFactory:
    @staticmethod
    def create_app():
        # Initialize FastAPI app with specific configurations
        app = FastAPI(
            title="System zarządzający wynikami w kręglarstwie klasycznym",
            openapi_url="/api/v1/openapi.json",
            redoc_url="/api/v1/redoc",
            docs_url="/api/v1/docs",
        )

        # Add CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Attach routes
        routes.GetBowlingAlleys().attach(app)
        routes.GetTournament().attach(app)
        routes.CreateTournament().attach(app)
        routes.GetTournaments().attach(app)
        routes.GetTournamentScores().attach(app)
        routes.GetTrainingScores().attach(app)
        routes.CreateTrainingScore().attach(app)

        # Mount admin Flask app
        app.mount("/admin/", WSGIMiddleware(admin.flask_app))

        # Mount static files
        static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))
        app.mount("/static/", StaticFiles(directory=static_path), name="static")

        # Mount SPA
        app.mount(path="/", app=SinglePageApplication(directory="dist"), name="SPA")

        return app

app = AppFactory.create_app()