import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345

    server_socket.bind((host, port))
    print(f"Server started on {host}:{port}")

    server_socket.listen(5)

    while True:
        print("Waiting for a connection...")
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")

        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    # no data means client has disconnected
                    break

                message = data.decode('utf-8')
                print(f"Received from {addr}: {message}")


                response = 'Hi! Recieved your message: ' + message
                client_socket.send(response.encode('utf-8'))

            except socket.error as e:
                # send err msg to client
                client_socket.send('ERR'.encode('utf-8'))
                print(f"Socket error: {e}")
                break

        client_socket.close()
        print(f"Connection with {addr} closed.")

if __name__ == '__main__':
    start_server()
