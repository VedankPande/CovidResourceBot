""" test code here """ 
import requests


response = requests.post('https://api-ssl.bitly.com/v4/shorten',headers={"group_guid": "cdbf2bacdaf83d2a3fede50260c76eccaf7a6a5a",  "domain": "bit.ly",  "long_url": "https://dev.bitly.com" })
print(response)