from django.db import models
import requests


def api_request(hostname, url, payload, headers):
    answer = []
    get_data = requests.post('https://' + hostname + url, json=payload, headers=headers)
    answer.append(get_data)
    if answer[0].json()['error']['message'] == 'Invalid Request':
        answer.append('Invalid Request')
        return answer
    else:
        answer.append(get_data.json())
        return answer
