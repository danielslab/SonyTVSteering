import requests
import json

# API-DOKU
# https://pro-bravia.sony.net/develop/index.html

TV = '192.168.178.26'  # TV-IP
PSK = "12345"  # PSK from TV

headers = {'X-Auth-PSK': PSK,
           'content-type': 'application/json'}


def audiovolume(value):
    url = f"http://{TV}/sony/system"
    payload = {"method": "setAudioVolume", "version": "1.0", "id": 1,
               "params": [{"target": "speaker", "volume": value}]}
    r = requests.post(url, json.dumps(payload), headers=headers)

def poweroff():
    url = f"http://{TV}/sony/system"
    payload = {
        "method": "setPowerStatus",
        "id": 1,
        "params": [{"status": False}],
        "version": "1.0"
    }
    r = requests.post(url, json.dumps(payload), headers=headers)


#audiovolume("+10")
poweroff()