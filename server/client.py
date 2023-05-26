import socket
import time

# 101 to open the box
# 202 to close the box

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def open_socket():
    # client_socket.connect(('192.168.43.2',3333))
    # client_socket.connect(('192.168.153.1',3333))
    client_socket.connect(('127.0.0.1',3333))

def close_socket():
    client_socket.close()
    
def sending_data(data):

    payload = str(data) 

    try:
        while True:
            client_socket.send(payload.encode('utf-8'))
            break
    except KeyboardInterrupt:
        print("Exited by user")
    