import requests
import time
key = 'api-key'
url = "https://api-free.deepl.com/v2/translate"
header = {'Authorization': key}
Text = "Dies ist eine Test Nachricht. Kann ich sie in Englisch übersetzt bekommen?"
lang = 'EN'
source_lang = 'DE'
param = {
    "text": Text,
    "source_lang": source_lang,
    "target_lang": lang
}

response = requests.get(url, params=param, headers=header)

print(response.status_code)
print(response.json())

