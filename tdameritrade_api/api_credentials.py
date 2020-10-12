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

    def __init__(self):
        self.hdrs = {"access_token": "IXrpDuPJBQhg5ZvEtW/I/CqO5aDHVLqA+EgGHpr9ue+2ss7E+bPbEQky17m/tXzecQgzArd92nyEVhj4+RBChqTw6oLhw+jaQCZFMNDxtVGPGGbTEOPF/iSktghlq4+G5eGtCueWxKKAN9eneK3bExSzjRYEUp7CcJd4oVAZH8hzXqS5pAYAFr9b0dfiNvPxU4wQHHZ4hhrCAfBTvMvPJbEnJ+Xgl5ADP6JlU5cu9BoxzMBd28FqYgoISMdd9Es6Y7IHu3SLOSq9OfeV4ch5a1TlMiCZOvTF1bc9WJaBi+outwFHLhNy6UJexh3UAxTIgpCRVN5UETz9mFd6W5dbhVsylE5h7XPZaGvxqG5JiJXrr3B/jNtQ4JjzQmaSjcP1ctuDgt4IDDRqAiOA1lRATP5bZBOAzvLVtFj2AIaN5SDm1gtDlMgla1Ea1OMJ2vXExYp0naRog0NLfBfdqXRmaRB5Mm7RKhBkBmpKeWcxojWTy7EkYKvLyPf6MslY/BNzquujZ100MQuG4LYrgoVi/JHHvlsNf77JLc3MtXROIPWvxlGFCfCDz8vsL9deWJeP+pxn4w4CAgcnvrENEiItp53/15t4T3J6svEM1x4M2R4WWfFKEW22qLJMXZdcAbImWCh8On8zO51jcvKY68hGq2sxpYPIbsRa1RigXS1BIACJbABfBCnCAaHo74RayvYeFra2eoTyvIh1xeZHeChovXRrmldXngFHJeUyvGdaua6hVLFJvRKUgh5+yUYVRWR5CcT2Rstb0gIyLQyVEl9RkFsrGAPbARBMYkART65Mj9nhulDc0V4q6vRl/5rqWHTzyFJipeGX7qUsae1r4byxch3Hj5WfCL6UPCsSz56LvTmaUgiyK129E3ZSqHQgM84tqLaIHPTGlHGulFGOU2wrx5isIfkJUumlmK4G5ADy11Vnqt6DZZvbKS6DMEoQcpAY8N4k/dqpZwVCKb2jQtJgyemJXMG5Wok+wAJ2ZBX5Z/t5MS/HzOeIjtBj4zPrNdH0i9vKyUCR9wyEHf9D0SBJrTQhb2qv8k4E212FD3x19z9sWBHDJACbC00B75E",
                     "expires_in": "1800",
                     "token_type": "Bearer {Access Token}",
                     'grant_type': 'authorization_code',
                       'code': 'decoded code',
                       'client_id': 'ABC98765@AMER.OAUTHAP',
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
    