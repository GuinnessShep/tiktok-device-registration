import requests
import json

API_KEY = "036141108000fde7ce29b51fbe74c6b04a86b996c439f9f1af0c" # contact t.me/scrapguru for test key

def device_reg():
    if API_KEY == "":
        raise Exception("API key is required")

    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }
    
    r = requests.get("https://tiktokapi.dev/device-reg", headers=headers)
    return r.json()

print(device_reg())
