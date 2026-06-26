import requests
import json

url = "http://127.0.0.1:5000/catalogo"

payload = json.dumps({
  "producto": " Proyector",
  "precio": 100.50,
  "stock": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)