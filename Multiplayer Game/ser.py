import socket
import threading


player = []

def send_mes():
    print("camed")
    mes = "player connected"
    mes = mes.encode()
    for i in player:
        i.send(mes)
        print("finished")


def handle_client(client_socket, client_address, other_client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            print(f"Client {client_address} has disconnected.")
            break

        print(f"Received message from {client_address}: {message}")
        other_client_socket.send(message.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 6665))
server.listen(2)
print("Server is listening for connections...")

client1, addr1 = server.accept()
print(f"Accepted connection from {addr1}")
player.append(client1)

client2, addr2 = server.accept()
print(f"Accepted connection from {addr2}")
player.append(client2)


thread1 = threading.Thread(target=handle_client, args=(client1, addr1, client2))
thread2 = threading.Thread(target=handle_client, args=(client2, addr2, client1))

thread1.start()
thread2.start()
