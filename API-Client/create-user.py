import requests
import json

#get-posts
request = requests.get('<host-ip>/get-posts')

#result
responsejson = request.json()
print(request.status_code)
print(json.dumps(responsejson, indent=4))