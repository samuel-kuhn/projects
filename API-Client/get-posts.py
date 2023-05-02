import requests
import json

name = "John"
email = "John@nonexistent.com"
password = "securepassword"


#new user
request = requests.post('<host-ip>/users?', json={"name": name, "email": email, "password": password})



#result
print(request.status_code)
print(request.content)