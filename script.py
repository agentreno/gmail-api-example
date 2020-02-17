import googleapiclient.discovery
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession


SERVICE_ACCOUNT_JSON_PATH = ""
IMPERSONATED_EMAIL = ""

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_JSON_PATH,
    scopes=["https://mail.google.com/"]
)
delegated_credentials = credentials.with_subject(IMPERSONATED_EMAIL)
gmail = googleapiclient.discovery.build("gmail", "v1", credentials=delegated_credentials)
response = gmail.users().messages().list(userId="me").execute()
print(response)

# response = gmail.users().messages().get(userId="me", id="").execute()
# raw = response["payload"]["parts"][1]["body"]["data"]
# TODO: Find a better way with python email stdlib
# raw = raw.replace("_", "/")
# raw = raw.replace("-", "+")
# import base64
# print(base64.b64decode(raw))
