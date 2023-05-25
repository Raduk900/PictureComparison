import requests

url = 'http://192.168.166.64:5000/umbraco/api/terminal/ping'

response = requests.get(url, timeout=5)

print(response.status_code)
print(response.text)