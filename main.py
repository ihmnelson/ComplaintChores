import json
import requests
import http.server
import os
import argparse


class Handler(http.server.BaseHTTPRequestHandler):
    # View lists of chores and people
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        with open('data/systems.json', 'r') as file:
            message = file.read()
        self.wfile.write(bytes(message, "utf8"))

    # When they try to set or edit data
    def do_PUT(self):
        valid_calls = [
            'addUser',
            'rmUser',
            'editUser'
        ]
        path = self.path
        pathSplit = path.split('/')
        pathSplit.remove('')

        if pathSplit[0] in valid_calls:
            self.send_response(200)
            self.end_headers()


with http.server.HTTPServer(('', 8000), Handler) as server:
    server.serve_forever()


def addSystem(email, data: dict):
    with open('data/systems.json', 'r+') as file:
        curSystems = json.load(file)
    curSystems[email] = data
    with open('data/systems.json', 'w') as file:
        json.dump(curSystems, file, indent=4)
