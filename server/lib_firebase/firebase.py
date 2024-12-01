from firebase_admin import initialize_app, auth, firestore_async
from firebase_admin.credentials import Certificate, ApplicationDefault
from google.cloud import secretmanager
import json


def get_credential(secret_name: str):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/555046474426/secrets/{secret_name}/versions/latest"

    response = client.access_secret_version(name=name)
    secret_value = response.payload.data.decode("UTF-8")
    return Certificate(json.loads(secret_value))


try:
    cred = get_credential()
except:
    cred = ApplicationDefault()

fb_app = initialize_app(cred)
fb_auth = auth.Client(fb_app)
fb_fstore = firestore_async.client(fb_app, database_id="agrotention-firestore-db")

__all__ = [
    "fb_app",
    "fb_auth",
    "fb_fstore",
]
