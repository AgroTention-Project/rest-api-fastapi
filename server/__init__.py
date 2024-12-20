"""
Main modul contain main `app`
"""

from contextlib import asynccontextmanager

from typing import Dict
from fastapi import FastAPI
from firebase_admin.exceptions import FirebaseError
from firebase_admin.ml import list_models, Model
from google.api_core.exceptions import GoogleAPICallError
from pydantic import ValidationError
from pydantic.errors import PydanticUserError

from . import app_diseases, app_news, app_plants, app_root, app_scanner, app_users
from .lib_exceptions.common import common_error
from .lib_exceptions.firebase import firebase_error
from .lib_exceptions.gcloud import google_cloud_error
from .lib_exceptions.validation import pydantic_user_error, validation_error
from .lib_firebase import fb_app


ml_models: Dict[str, Model] = {}


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    app lifespan
    """
    # Load the ML model

    load_models = list_models(app=fb_app)
    for model in load_models.models:
        ml_models[model.display_name] = model

    print("loaded ml models", ml_models)
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()
    print("crear ml models")


app = FastAPI(
    debug=True,
    lifespan=lifespan,
    title="AgroTention API",
    version="0.0.3",
    description="""
## About the Project
AgroTention is part of the Bangkit Capstone Project by Team `C242-PS073`. The application leverages modern machine learning technologies to:
- Identify diseases affecting plants.
- Provide actionable insights for better agricultural practices.

## Features
- **Robust API Design**: Built using FastAPI for speed and scalability.
- **Cloud Integration**: Deployed on **Google Cloud Platform** using **Firestore** as the database and **Vertex AI** for machine learning model deployment.
- **Accurate Disease Detection**: Utilizes labeled datasets validated by experts for plant disease classification.

## Team
**Team ID**: `C242-PS073`  
Developed by the Bangkit Capstone AgroTention Project Team  
""",
)


app.exception_handler(FirebaseError)(firebase_error)
app.exception_handler(PydanticUserError)(pydantic_user_error)
app.exception_handler(GoogleAPICallError)(google_cloud_error)
app.exception_handler(Exception)(common_error)
app.exception_handler(ValidationError)(validation_error)

app.include_router(app_news.router)
app.include_router(app_plants.router)
app.include_router(app_root.router)
app.include_router(app_users.router)
app.include_router(app_diseases.router)
app.include_router(app_scanner.router)
