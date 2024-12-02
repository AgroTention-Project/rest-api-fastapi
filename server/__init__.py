"""
Main modul contain main `app`
"""

from fastapi import FastAPI
from firebase_admin.exceptions import FirebaseError
from google.api_core.exceptions import GoogleAPICallError
from pydantic.errors import PydanticUserError

from . import app_diseases, app_news, app_plants, app_root, app_users
from .exceptions.common import common_error
from .exceptions.firebase import firebase_error
from .exceptions.gcloud import google_cloud_error
from .exceptions.validation import pydantic_user_error

app = FastAPI(
    title="AgroTention Back End RESTFul API",
    description="Back End REST API service for AgroTention App. Developed by bangkit capstone AgroTention Project team (ID: C242-PS073)",
)

app.exception_handler(FirebaseError)(firebase_error)
app.exception_handler(PydanticUserError)(pydantic_user_error)
app.exception_handler(GoogleAPICallError)(google_cloud_error)
app.exception_handler(Exception)(common_error)

app.include_router(app_news.router)
app.include_router(app_plants.router)
app.include_router(app_root.router)
app.include_router(app_users.router)
app.include_router(app_diseases.router)
