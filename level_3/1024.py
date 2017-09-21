#!/usr/bin/python3
"""
Voting as a Windows user and evading Captcha
"""

from lxml import html
from PIL import Image
import requests
import pytesseract
import shutil

def pull_captcha_image(cookie, url):
    captcha_res = requests.get(url, cookies=cookie, stream=True)
    if captcha_res.status_code == 200:
        try:
            with open("captcha.png", "wb") as pic_file:
                captcha_res.raw.decode_content = True
                shutil.copyfileobj(captcha_res.raw, pic_file)
        except FileNotFoundError:
            print("File not found")
        try:
            with open("captcha.png", "rb") as pic_file:
                img = Image.open(pic_file)
                return img
        except IOError:
            print("Couldn't open image")

def extract_text(image):
    return pytesseract.image_to_string(image)

def grab_captcha_text(res, url):
    image = pull_captcha_image(res, url)
    image_text = extract_text(image)
    return image_text

def update_cookie_and_payload(res, cookie, payload, captcha=None):
    """
    Updates the cookie and payload as each vote gets cast
    """
    tree = html.fromstring(res.text)
    key = str(tree.xpath('//input[@name="key"]/@value')[0])
    payload["key"] = key
    if captcha:
        payload["captcha"] = captcha
    cookie["HoldTheDoor"] = res.cookies["HoldTheDoor"]

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
        "key": "1234",
        "captcha": "ba23"
    }
    ENDPOINT = "http://158.69.76.135/level3.php"
    CAPTCHA_URL = "http://158.69.76.135/captcha.php"

    get_initial_data(ENDPOINT, hodor_cookies, hodor_payload)

    for i in range(1, 1025):
        res = cast_vote(ENDPOINT, hodor_cookies, hodor_payload)
        captcha = grab_captcha_text(hodor_cookies, CAPTCHA_URL)
        update_cookie_and_payload(res, hodor_cookie, hodor_payload, captcha)
