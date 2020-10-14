# Started with example code from:
# https://developer.tdameritrade.com/content/web-server-authentication-python-3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import requests
import ssl
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        #Get the Auth Code
        path, _, query_string = self.path.partition('?')
        code = parse_qs(query_string)['code'][0]

        #Post Access Token Request
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

        authReply = requests.post(
            'https://api.tdameritrade.com/v1/oauth2/token',
			code=code,
            headers=headers,
            data=data
        )

        #returned just to test that it's working
        self.wfile.write(authReply.text.encode())


httpd = HTTPServer(("localhost", 5000), Handler)


#SSL cert
httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile='certs/key.pem',
        certfile='certs/certificate.pem', server_side=True)


httpd.serve_forever()
