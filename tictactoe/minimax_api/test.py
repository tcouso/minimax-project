import requests
import json

"""Request tester module"""

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "move", {
    "board": json.dumps([["x", "", ""], ["x", "", ""], ["", "", ""]])
    })
print(response.json())
