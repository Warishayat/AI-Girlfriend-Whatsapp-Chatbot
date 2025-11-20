from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()


Twillio_sid  = os.getenv('Twillio_Account_sid')
Twillio_auth = os.getenv('Twillio_Account_Auth_Token')


client = Client(Twillio_sid,Twillio_auth)

message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="Test message from Python!",
    to="whatsapp:+923090333420"
)

print(message.sid)