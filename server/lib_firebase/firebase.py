"""Firebase Setup and Configurations"""

import json

from firebase_admin import auth, firestore_async, initialize_app
from firebase_admin.credentials import ApplicationDefault, Certificate
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
    cred = get_credential("FIREBASE_ADMIN_SA")
except Exception as exc:
    print(f"An error occurred: {type(exc).__name__} - {exc}")
    cred = ApplicationDefault()

fb_app = initialize_app(cred)
fb_auth = auth.Client(fb_app)
fb_fstore = firestore_async.client(fb_app, database_id="agrotention-firestore-db")

__all__ = [
    "fb_app",
    "fb_auth",
    "fb_fstore",
]
