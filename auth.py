import os
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

CLIENT_SECRET_FILE = 'client_secret.json'
TOKEN_FILE = 'token.json'

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


def get_authenticated_service():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    credentials = None

    if os.path.exists(TOKEN_FILE):
        print("Cargando credenciales desde token.json...")
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, scopes)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print("Credentials expired, refreshing token...")
            credentials.refresh(Request())
        else:
            print("No valid token found, performing initial authorization...")
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, scopes)
            credentials = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'w') as data_json:
            data_json.write(credentials.to_json())
        print("Credentials are not to token.json")

    return googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)
