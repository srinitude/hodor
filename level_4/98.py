#!/usr/bin/python3
"""
Voting 98 times as a different user every time
"""

import requests
from proxylist import ProxyList
from lxml import html

def load_proxies():
    pl = ProxyList()
    pl.load_file("./proxy.txt")
    return pl

def update_cookie_and_payload(res, cookie, payload, proxy, proxies):
    """
    Updates the cookie and payload as each vote gets cast
    """
    tree = html.fromstring(res.text)
    key = str(tree.xpath('//input[@name="key"]/@value')[0])
    payload["key"] = key
    cookie["HoldTheDoor"] = res.cookies["HoldTheDoor"]
    proxies["http"] = proxy

def get_initial_data(url, cookie, payload, proxy, proxies):
    """
    Retrieves the initial cookie and payload
    """
    res = requests.get(url)
    update_cookie_and_payload(res, cookie, payload, proxy, proxies)

def cast_vote(url, cookie, payload, proxies):
    """
    Casts a vote as if you were on Windows
    """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    header = {
        "Referer": url,
        "User-Agent": user_agent
    }
    res = requests.post(url, data=payload, cookies=cookie, headers=header, proxies=proxies)
    print(res.text)
    return res

if __name__ == "__main__":
    hodor_cookies = {}
    hodor_payload = {
        "holdthedoor": "Submit",
        "id": "139",
    }
    proxies = {}
    ENDPOINT = "http://158.69.76.135/level4.php"
    proxie_list = load_proxies()
    next_proxy = proxie_list.random().address()
    get_initial_data(ENDPOINT, hodor_cookies, hodor_payload, next_proxy, proxies)

    while True:
        res = cast_vote(ENDPOINT, hodor_cookies, hodor_payload, proxies)
        next_proxy = proxie_list.random().address()
        update_cookie_and_payload(res, hodor_cookies, hodor_payload, next_proxy, proxies)
