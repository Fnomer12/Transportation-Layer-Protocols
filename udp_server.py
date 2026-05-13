import socket
from datetime import datetime
import random

HOST = "127.0.0.1"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"[UDP SERVER STARTED] Listening on {HOST}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)
    message = data.decode()

    time_now = datetime.now().strftime("%H:%M:%S")

    print(f"[{time_now}] UDP Client {addr}: {message}")

    # Simulate UDP unreliability
    packet_loss_chance = random.randint(1, 10)

    if packet_loss_chance <= 2:
        print("[UDP PACKET DROPPED SIMULATION]")
        continue

    response = f"UDP ACK: Message received at {time_now}"
    server.sendto(response.encode(), addr)