import requests

url = "https://geo.craigslist.org/iso/us"

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4"}

response = requests.get(url, headers=headers)

