import json
import requests
reponse = requests.get('http://api.open-notify.org/iss-now.json')

print(reponse.status_code)
status_code = reponse.status_code
