import os
import json
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


def get_phone(system: dict, name: str) -> str:
    for person in system['people']:
        if person['name'] == name:
            return person['phone']
    return 'does not exist'


def send_all():
    for filename in os.listdir('systems'):
        choresByPeople = {}
        peopleAndPhones = {}
        with open(f'systems/{filename}', 'r') as file:
            data = json.load(file)
        for chore in data['chores']:
            name = chore['assigned']
            phone = get_phone(data, name)
            if name not in peopleAndPhones:
                peopleAndPhones[name] = phone
            if name in choresByPeople:
                choresByPeople[name].append(chore['name'])
            else:
                choresByPeople[name] = [chore['name']]

        for key in choresByPeople:
            message = f'Hello {key}! Today your chores are:\n'
            for word in choresByPeople[key]:
                message += f' - {word}\n'
            message += 'Have a nice day!'

            send_sms(peopleAndPhones[key], message)


# TODO add alarm loop functionality
