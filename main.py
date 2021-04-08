import requests
import json

TV = '192.168.178.26'  # TV-IP
PSK = "12345"  # PSK from TV

headers = {'X-Auth-PSK': '12345',
           'content-type': 'application/json'}

def audio(value):
    url = f"http://{TV}/sony/audio"
    payload = {"method": "setAudioVolume", "version": "1.0", "id": 1, "params": [{"target": "speaker", "volume": value}]}
    r = requests.post(url, json.dumps(payload), headers=headers)
    print(type(value))

audio("+10")