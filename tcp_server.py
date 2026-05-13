import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8050

def handle_client(conn, addr):
    print(f"[TCP CONNECTED] {addr}")

    with conn:
        while True:
            data = conn.recv(1024)

            if not data:
                break

            message = data.decode()
            time_now = datetime.now().strftime("%H:%M:%S")

            print(f"[{time_now}] TCP Client {addr}: {message}")

            response = f"TCP ACK: Message received successfully at {time_now}"
            conn.sendall(response.encode())

    print(f"[TCP DISCONNECTED] {addr}")

def start_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[TCP SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE TCP CLIENTS] {threading.active_count() - 1}")

start_tcp_server()