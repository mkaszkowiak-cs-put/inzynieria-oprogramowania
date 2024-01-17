from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, admin
from typing import Tuple
import os

from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session

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

app.mount("/admin/", WSGIMiddleware(admin.flask_app))
app.mount("/static/", StaticFiles(directory=static_path), name="static")
app.mount(path="/", app=SinglePageApplication(directory="dist"), name="SPA")
