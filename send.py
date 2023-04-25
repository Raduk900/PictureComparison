import requests
import json

# Define the API endpoint URL and the boolean value to send
url = 'http://localhost:8000/api/endpoint'
data = {
    'boolean_param': True
}

# Convert the data to a JSON string
json_data = json.dumps(data)

# Send the POST request with JSON data
response = requests.post(url, json=json_data)

# Print the response content
print(response.content)