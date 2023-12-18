import socket

HOST = '192.168.29.176'
PORT = 9090

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter your message (type 'quit' to exit): ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'quit':
        break

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server's reply: {response}")

client_socket.close()
