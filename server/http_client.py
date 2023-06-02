import requests

def send_post_request_delete_product(id):
    url = 'http://192.168.69.64:5000/umbraco/api/terminal/DeleteProduct?productId=' + str(id)
    
    print(url)

    response = requests.get(url, timeout=5)

    print(response.status_code)
    print(response.text)
    
def send_post_request_verify_product(id):
    url = 'http://192.168.69.64:5000/umbraco/api/terminal/VerifyProduct?productId=' + str(id)
    
    print(url)

    response = requests.get(url, timeout=5)

    print(response.status_code)
    print(response.text)


