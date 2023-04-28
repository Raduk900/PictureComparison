import socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',3333))
payload = str(1)

try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        more=input('Want to send more data to the server press y: ')
        if more.lower()=='y':
            payload=input("Enter Payload: ")
        else:
            break
except KeyboardInterrupt:
    print("Exited by user")
client_socket.close()