#!/usr/bin/python3
"""
Voting as a Windows user
"""


import requests
from lxml import html


def update_cookie_and_payload(res, cookie, payload):
    """
    Updates the cookie and payload as each vote gets cast
    """
    cookie["HoldTheDoor"] = res.cookies["HoldTheDoor"]
    tree = html.fromstring(res.content)
    key = str(tree.xpath('//input[@name="key"]/@value')[0])
    payload["key"] = key

def get_initial_data(url, cookie, payload):
    """
    Retrieves the initial cookie and payload
    """
    res = requests.get(url)
    update_cookie_and_payload(res, cookie, payload)

def cast_vote(url, cookie, payload):
    """
    Casts a vote as if you were on Windows
    """
    user_agent = "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"
    header = {
        "User-Agent": user_agent
    }
    res = requests.post(url, data=payload, cookies=cookie, headers=header)
    return res

cookie = {}
payload = {
    "id": "139",
    "holdthedoor": "Submit"
}
endpoint = "http://158.69.76.135/level2.php"

get_initial_data(endpoint, cookie, payload)

for i in range(1024):
    res = cast_vote(endpoint, cookie, payload)
    update_cookie_and_payload(res, cookie, payload)
