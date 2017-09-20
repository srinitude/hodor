#!/usr/bin/python3
"""
Sending a POST request to Hodor resource 4096 times
"""
from lxml import html
import requests

url = "http://158.69.76.135/level1.php"
page = requests.get(url)
hodor_cookie = {}
hodor_cookie["HoldTheDoor"] = page.cookies["HoldTheDoor"]
tree = html.fromstring(page.content)
hodor_key = str(tree.xpath('//input[@name="key"]/@value')[0])

for i in range(4096):
    hodor_data = {"id": "139", "holdthedoor": "Submit", "key": hodor_key}
    res = requests.post(url, data=hodor_data, cookies=hodor_cookie)
    print("Vote #{:d} casted".format(i))
    hodor_cookie["HoldTheDoor"] = res.cookies["HoldTheDoor"]
    tree = html.fromstring(res.text)
    hodor_key = str(tree.xpath('//input[@name="key"]/@value')[0])
