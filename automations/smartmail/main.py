import base64 #base64 is a cryptographic encoding method, Base64 and base64url are two different methods as base64url removes specific characters from the encoding that will mess up with urls and thus is more web friendly and gmail allows only base64url encoded messages to be sent as mails. 
from email.mime.text import MIMEText #To send an email you have to write it in a specific structure and MIMEText is a module simplifies that.
from google.auth.transport.requests import Request # This module is used to refresh the token when it expires and also to check if the token is valid or not. It is used in conjunction with the Credentials module.
from google.oauth2.credentials import Credentials # This module is used to create a credentials object from the token.json file that is created after the first time you authenticate with your google account. It is used to refresh the token when it expires and also to check if the token is valid or not.
from google_auth_oauthlib.flow import InstalledAppFlow #The new window pop up that asks for authentication is built with this module.
from googleapiclient.discovery import build #This module is used to select the service like gmail and we provide it with credentials. Through it we send mails. It's like the gateway from where we access everything in that service.
import os.path #This is used to interact with OS.

#We start with defining the scope of the app. Like sending email.

scope = ['https://www.googleapis.com/auth/gmail.compose']

#As said earlier gmail accepts only base64url encoded messages. So first we encode the message.

def email_encoded_email(sender,to, subject, message_text):
    message= MIMEText(message_text) # Here we create a message object with the message text that we want to send. The MIMEText class takes the message text as an argument and creates a message object that can be sent as an email.
    message['To'] = to #because the message object is a dictionary like object we can set the To, From and Subject fields of the email by setting the corresponding keys in the message object.
    message['From'] = sender 
    message['Subject'] = subject

    raw_bytes = message.as_bytes() #base64 doesn't take strings as input, So we convert it into bytes.

    encoded_bytes = base64.urlsafe_b64encode(raw_bytes) #Then encode those bytes

    encoded_string = encoded_bytes.decode('utf-8') #And decode it back to string so that we can send it as a json object. because the send method of the gmail api takes a json object as input and we can't send bytes as json object.

    return {'raw': encoded_string} #raw is the key that the gmail api expects in the json object that we send to it. It contains the base64url encoded message that we want to send as an email.

email_data = email_encoded_email(
    sender="shafiqahmaddon302@gmail.com",
    to="ahmad@fincrow.dev",
    subject="hello this is sparrowusa",
    message_text="ouch ouch ouch"
)

print(email_data)


# In brief we first set creds to none and then check if token.json file exist(which is the cache so we don't login from pop up everytime)  and If they don't or are expired we use credentials.json file and with InstalledAppFlow we make that pop up and then save those tokens. Last but not least we use build module to select gmail as service and get all the gmail related powers from google and later using service variable which holds build's powers we send the encoded email.
def send_email():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scope)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scope)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    email_sent = service.users().messages().send(userId= "me", body=email_data).execute()


if __name__ == "__main__":
    send_email()

