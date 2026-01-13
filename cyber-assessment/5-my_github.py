#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

    if response.status_code == 200:
        print(response.json().get("id"))
