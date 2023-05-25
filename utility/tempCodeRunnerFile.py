import requests

url = 'http://192.168.69.64:5000/umbraco/api/terminal/DeleteProduct?productId=af5aed39-c73b-4999-a4a0-76205568a07c'
response = requests.get(url, timeout=5)  # increase timeout to 5 seconds

print(response.status_code)
print(response.text)