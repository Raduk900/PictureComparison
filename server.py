import socket
import json
import requests
import sys
import os
from database import database_validations

# import database.database_validations as database_validations

def get_request_path(request_data):
    lines = request_data.split('\n')
    first_line = lines[0].strip()

    if first_line.startswith('POST'):
        parts = first_line.split()
        if len(parts) >= 2:
            path = parts[1]
            return path

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
            request_path = get_request_path(data.decode("utf-8"))
            print(request_path)
            json_data = get_json_from_request(data.decode("utf-8"))
            if json_data:
                print("JSON data from client:", json_data)

                productId = json_data.get('productId')
                memberId = json_data.get('memberId')
                photoUrl = json_data.get('photoUrl')
                uniqueCode = json_data.get('uniqueCode')

                if request_path == '/api/addproduct':
                    database_validations.add_item_to_user(memberId, productId, "192.168.69.64:5000" + photoUrl, uniqueCode)
                if request_path == '/api/addreservation':
                    database_validations.take_item_to_user(memberId, '1', productId, uniqueCode)
                client_socket.close()

                client_socket, addr = server_socket.accept()

            else:
                print("Failed to extract JSON data from the request")
        except json.JSONDecodeError:
            print("Invalid JSON data received from client")

    client_socket.close()