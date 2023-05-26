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

# id_value = "e05a23c9-fbb2-4f87-b34a-b8cbea61136b"
# send_post_request_delete_product(id_value)
# send_post_request_verify_product(id_value)

# import requests

# def send_post_request(url):
#     response = requests.post(url)
#     return response

# url = 'https://192.168.69.26:5000/umbraco/api/terminal/DeleteProduct?productId=e3b15b29-92bf-407f-9fe9-86197e58a34c'
         
# response = send_post_request(url)
# print(response.status_code)
# print(response.text)


