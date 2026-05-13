import socket
import time
import uuid

HOST = "127.0.0.1"
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3)

print("[UDP CLIENT READY]")
print("Type 'exit' to quit.\n")

while True:
    message = input("Enter UDP message: ")

    if message.lower() == "exit":
        break

    message_id = str(uuid.uuid4())[:8]
    full_message = f"ID:{message_id} | {message}"

    start_time = time.time()

    client.sendto(full_message.encode(), (HOST, PORT))

    try:
        data, server = client.recvfrom(1024)
        end_time = time.time()

        latency = (end_time - start_time) * 1000

        print("Server:", data.decode())
        print(f"UDP Latency: {latency:.2f} ms\n")

    except socket.timeout:
        print("UDP Error: No response received. Packet may be lost.\n")

client.close()
print("[UDP CLIENT CLOSED]")