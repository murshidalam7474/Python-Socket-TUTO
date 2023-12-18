
import socket

# bind
HOST = '192.168.29.176'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    comm_sock, address = server.accept()
    print(f"Connected to {address}")

    while True:
        message = comm_sock.recv(1024).decode('utf-8')
        print(f"Message from client is -> {message}")

        if message.lower() == 'quit':
            break

        reply = input("Enter your reply: ")
        comm_sock.send(reply.encode('utf-8'))

    comm_sock.close()
    print(f"Connection with {address} closed!")
