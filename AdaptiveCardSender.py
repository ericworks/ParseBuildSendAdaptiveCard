import json
import requests
from PyinstallerUtils import resource_path


def send_requests(url: str, card_request: dict):
    request_template = {}
    with open(resource_path('RequestTemplate.json'), 'r') as fp:
        request_template = json.load(fp)
    request_template["attachments"][0]["content"] = card_request

    resp = requests.post(url, json=request_template)
    print(f"Request Response: " + str(resp.status_code) + ", " + resp.text)