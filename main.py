import io
import json
import http.server
import os


def addSystem(email):
    default_system = {
        "email": email,
        "people": [

        ],
        "chores": [

        ]
    }
    with open(f'systems/{email}.json', 'w') as file:
        json.dump(default_system, file, indent=4)


class Handler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        path = self.path
        path_split = path.split('/')
        path_split.remove('')
        if len(path_split) < 1:
            self.send_response(200)
            self.end_headers()
            return
        if path_split[0] == 'system':
            if len(path_split) < 2:
                self.send_response(404)
                self.end_headers()
                return
            email = path_split[1]
            if os.path.exists(f'systems/{email}.json'):
                self.send_response(200)
                with open(f'systems/{email}.json', 'r') as file:
                    message = file.read()
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(message, "utf8"))
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    # When they try to set or edit systems
    def do_POST(self):
        path = self.path
        path_split = path.split('/')
        path_split.remove('')

        if path_split[0] == 'system':
            content_len = int(self.headers.get('content-length', 0))
            post_body = self.rfile.read(content_len)
            content = json.loads(post_body.decode('utf8'))

            addSystem(content['email'])

            self.send_response(200)
            self.end_headers()


with http.server.HTTPServer(('', 8000), Handler) as server:
    server.serve_forever()
