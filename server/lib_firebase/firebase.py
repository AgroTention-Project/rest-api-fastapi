"""Firebase Setup and Configurations"""

import json
import sys

from fastapi.logger import logger
from firebase_admin import auth, firestore_async, initialize_app, storage
from firebase_admin.credentials import ApplicationDefault, Certificate
from google.api_core.exceptions import GoogleAPICallError, GoogleAPIError
from google.cloud import secretmanager


def get_credential(secret_name: str):
    """
    ## `get_credential`
    Get service account from secret
    """
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/555046474426/secrets/{secret_name}/versions/latest"

    response = client.access_secret_version(name=name)
    secret_value = response.payload.data.decode("UTF-8")
    return Certificate(json.loads(secret_value))


try:
    logger.info("Try get credential from google secret manager...")
    cred = get_credential("FIREBASE_ADMIN_SA")
    logger.info(
        "Found credential for project %s from google secret manager", cred.project_id
    )
except (GoogleAPIError, GoogleAPICallError) as exc:
    logger.error("An error occurred: %s - %s", type(exc).__name__, str(exc))
    logger.info("Try get credential from local...")
    cred = ApplicationDefault()
    logger.info("Found credential for project %s from local", cred.project_id)
except (FileNotFoundError, ValueError) as exc:
    print(exc)
    sys.exit(1)


fb_app = initialize_app(cred)
fb_auth = auth.Client(fb_app)
fb_fstore = firestore_async.client(fb_app, database_id="agrotention-firestore-db")
fb_storage = storage.bucket(
    name="agrotention-project-441716.firebasestorage.app", app=fb_app
)


__all__ = [
    "fb_app",
    "fb_auth",
    "fb_fstore",
    "fb_storage",
]
