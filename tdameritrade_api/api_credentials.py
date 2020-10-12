# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 04:27:58 2019

@author: rayde
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from urllib.parse import parse_qs
import requests
import ssl

class Handler(BaseHTTPRequestHandler):
    url = 'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=http://127.0.0.1&client_id=ABC98765@AMER.OAUTHAP'
    httpd = HTTPServer((Host, Redirect_Port), Handler)

    #SSL cert
    httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile='path/to/key.pem', 
        certfile='path/to/certificate.pem', server_side=True)

    httpd.serve_forever() 

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
        data = { 'grant_type': 'authorization_code', 'access_type': 'offline', 'code': code, 'client_id': 'Consumer Key', 'redirect_uri': 'http://127.0.0.1'}
        authReply = requests.post('https://api.tdameritrade.com/v1/oauth2/token', headers=headers, data=data)
        
        #returned just to test that it's working
        self.wfile.write(authReply.text.encode())
    

class header:

    ''' for more information on encoding/decoding in python visit: 
        https://www.urlencoder.io/python/ '''

    def __init__(self, access_token, decoded_code, client_id):
        self.hdrs = {"access_token": access_token,
                     "expires_in": "1800",
                     "token_type": "Bearer {Access Token}",
                     'grant_type': 'authorization_code',
                       'code': decoded_code,
                       'client_id': client_id,
                       'redirect_uri': 'http://127.0.0.1'
                     }
           
    def encode(self):
        '''
        #Encoding multiple parameters at once in dictionary object
        '''
        for each in self.hdrs:
            try:
                self.hdrs[each]=urllib.parse.quote(self.hdrs[each])
            except:
                pass
    
    def encode_multiple(self):
        '''
        #Encoding multiple parameters at once 
        '''
        return urllib.parse.urlencode(self.hdrs, quote_via=urllib.parse.quote)
       
    def multiple_values(self):
        '''
        Encoding multiple parameters at once where one parameter can have multiple values
        '''
        return urllib.parse.urlencode(self.hdrs, doseq=True)
    