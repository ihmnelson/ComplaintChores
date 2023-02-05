import datetime
import time
from twilio.rest import Client


def send_sms(phone: str, message: str):
    account_sid = 'AC9ed7f6cf2929b503dbfd6a27ff649ab3'
    with open('token.txt', 'r') as token_file:
        auth_token = token_file.read()

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG52f2582c5f1ce73815ed611d2077b425',
        body=message,
        to=phone
    )


def send_all():
    return

# TODO add alarm loop functionality
