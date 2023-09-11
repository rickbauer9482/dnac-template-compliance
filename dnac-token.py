import requests
import json

url = "https://172.30.1.196/dna/system/api/v1/auth/token"

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cmlja2JhdWU6Q2lzY28xMjMkJQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
