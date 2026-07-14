from google.auth.transport.requests import Request # This module is used to refresh the token when it expires and also to check if the token is valid or not. It is used in conjunction with the Credentials module.
from google.oauth2.credentials import Credentials # This module is used to create a credentials object from the token.json file that is created after the first time you authenticate with your google account. It is used to refresh the token when it expires and also to check if the token is valid or not.
from google_auth_oauthlib.flow import InstalledAppFlow #The new window pop up that asks for authentication is built with this module.
from googleapiclient.discovery import build #This module is used to select the service like gmail and we provide it with credentials. Through it we send mails. It's like the gateway from where we access everything in that service.
import os.path #This is used to interact with OS.

def establish_connection():

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    creds = None

    if os.path.exists("token.json"):
        creds= Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds= flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("sheets", "v4", credentials=creds)

def create_spreadsheet(title, service): #Google sheets API has a method called create which is used to create a new spreadsheet. It takes a body parameter which is a dictionary that contains the properties of the spreadsheet. The title of the spreadsheet is passed as a parameter to this function and is used to set the title of the spreadsheet.
    spreadsheet_body = {
        'properties': {
            'title' : title
        }
    }
    request= service.spreadsheets().create(body=spreadsheet_body).execute()
    print(f"Spreadsheet created: {request.get('spreadsheetUrl')}")
    return request.get("spreadsheetId")


if __name__ == "__main__":
    service = establish_connection()     #service variable is set here and is used above
    create_spreadsheet("Hello", service) #Here we gave "title" the name "hello" which gives the sheet name hello.