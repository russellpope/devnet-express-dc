#!/usr/bin/env python

import requests
import json

auth_token = 'Bearer NWU4ZWE1MWMtNzQyMi00NWFjLTk2NmUtZjU3YThjZjBkOGNmNDFjNDVmMmUtYTcz'

r = requests.get(
    url='https://api.ciscospark.com/v1/rooms',
    headers={'Content-type': 'Application/json',
             'Accept': 'Application/json',
             'Authorization': auth_token})

#
rooms = json.loads(r.content)


for room in rooms["items"]:
    if room['title'] == "DNE-DCI-LV-External room":
        payload = {
            "roomId": room['id'],
            "text": "Sending a very fine message via python",
        }

        post = requests.post(
            url='https://api.ciscospark.com/v1/messages',
            headers={'Content-type': 'Application/json',
                     'Accept': 'Application/json',
                     'Authorization': auth_token},
            data=json.dumps(payload))
        print(post.content)


