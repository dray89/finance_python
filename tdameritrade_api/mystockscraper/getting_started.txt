#Note: https://developer.tdameritrade.com/guides; TDAmeritrade API guides assume professional integration with multiple users. This project is designed for personal use.

#Python guide: https://developer.tdameritrade.com/content/web-server-authentication-python-3

#Getting Started Guide: https://developer.tdameritrade.com/content/getting-started

#Get User Principals: https://developer.tdameritrade.com/user-principal/apis/get/userprincipals-0

#Simple App Authorization: https://developer.tdameritrade.com/content/simple-auth-local-apps

#Post Access Token: https://developer.tdameritrade.com/authentication/apis/post/token-0

#Request authorization from tdameritrade server
auth_url = "https://api.tdameritrade.com/v1/oauth2/token"

body = {
	grant_type
}

results = requests.get(auth_url, date=body)

#Code is requested and comes out as an output. Redirect_url is a self-created url for the ameritrade server to communicate back results. 
#Essentially, you can choose anything you want. Client_id is a self created alphanumeric string created to identify your application for authorization.

params = {
  'access_type': 'offline', 
	'response_type': 'code',
	'redirect_url': 'https//localhost',
	'client_id': 'EXAMPLE@AMER.OAUTHAP'
}
