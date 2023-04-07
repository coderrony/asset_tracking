import requests
import json

URL = "http://127.0.0.1:8000/"


def get_company_info(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {"content-type": "application/json"}

    json_data = json.dumps(data)
    r = requests.get(headers=headers, url=URL, data=json_data)
    print(r.json())


get_company_info(1)
