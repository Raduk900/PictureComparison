# import http.server
# import socketserver
# from http.server import BaseHTTPRequestHandler

# PORT = 8000

# class MyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(b'Hello, world!')

#     def do_POST(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(b'Received a POST request')

# with socketserver.ThreadingTCPServer(("", PORT), MyHandler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
    
    
import socket
import json
import requests

def get_json_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error occurred during the request:", str(e))
        return None

def get_json_from_request(request):
    try:
        start_index = request.find("{")
        end_index = request.rfind("}")
        if start_index != -1 and end_index != -1:
            json_data = request[start_index:end_index+1]
            return json.loads(json_data)
        else:
            return None
    except json.JSONDecodeError as e:
        print("Error occurred during JSON decoding:", str(e))
        return None

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.69.218', 5000))
server_socket.listen(5)

url_add_product = 'http://192.168.69.64:5000/umbraco/api/addproduct'
url_add_reservation = 'http://192.168.69.64:5000/umbraco/api/addreservation'

while True:
    print("Server waiting for connection")
    client_socket, addr = server_socket.accept()
    print("Client connected from", addr)

    while True:
        data = client_socket.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        print("Received from client:", data.decode("utf-8"))

        try:
            json_data = get_json_from_request(data.decode("utf-8"))
            if json_data:
                print("JSON data from client:", json_data)
                # Access the specific fields as needed
                productId = json_data.get('productId')
                memberId = json_data.get('memberId')
                photoUrl = json_data.get('photoUrl')
                uniqueCode = json_data.get('uniqueCode')
                # Process the data further
                # ...
            else:
                print("Failed to extract JSON data from the request")
        except json.JSONDecodeError:
            print("Invalid JSON data received from client")

        # Perform the second request to add a reservation
        reservation_data = {
            'productId': productId,
            'memberId': memberId,
            'reservationDate': '2023-05-24'  # Example date
        }
        reservation_response = requests.post(url_add_reservation, json=reservation_data)
        if reservation_response.status_code == 200:
            reservation_json = reservation_response.json()
            print("Reservation added:", reservation_json)
        else:
            print("Failed to add reservation")

        try:
            client_socket.send(bytes('Hey, client', 'utf-8'))
        except:
            print("Exited by the user")

    client_socket.close()