import requests
import time

def get_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Example usage
url = 'http://192.168.69.64:5000/umbraco/api/addproduct'

while True:
    text = get_text_from_url(url)
    if text:
        print("Text from URL:", text)
        # Save the text to a file or perform any other desired operations
    else:
        print("Text not available. Waiting...")
    time.sleep(1)  # Wait for 1 second before trying
