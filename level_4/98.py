#!/usr/bin/python3
"""
Voting 98 times as a different user every time
"""

import requests
from proxylist import ProxyList

def load_proxies():
    pl = ProxyList()
    pl.load_file("./proxy.txt")
    return pl

def update_cookie_and_payload(res, cookie, payload):
    """
    Updates the cookie and payload as each vote gets cast
    """
    tree = html.fromstring(res.text)
    key = str(tree.xpath('//input[@name="key"]/@value')[0])
    payload["key"] = key
    cookie["HoldTheDoor"] = res.cookies["HoldTheDoor"]
    if not "PHPSESSID" in cookie:
        cookie["PHPSESSID"] = res.cookies["PHPSESSID"]

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

if __name__ == "__main__":
    hodor_cookies = {}
    hodor_payload = {
        "holdthedoor": "Submit",
        "id": "139",
    }
    ENDPOINT = "http://158.69.76.135/level4.php"
    proxies = load_proxies()
    get_initial_data(ENDPOINT, hodor_cookies, hodor_payload)

    while True:
        res = cast_vote(ENDPOINT, hodor_cookies, hodor_payload)
        update_cookie_and_payload(res, hodor_cookies, hodor_payload)
