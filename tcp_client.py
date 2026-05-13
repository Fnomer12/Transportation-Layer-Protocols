import socket
import time
import uuid

HOST = "127.0.0.1"
PORT = 8050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("[TCP CLIENT CONNECTED]")
print("Type 'exit' to quit.\n")

while True:
    message = input("Enter TCP message: ")

    if message.lower() == "exit":
        break

    message_id = str(uuid.uuid4())[:8]
    full_message = f"ID:{message_id} | {message}"

    start_time = time.time()
    client.sendall(full_message.encode())

    response = client.recv(1024).decode()
    end_time = time.time()

    latency = (end_time - start_time) * 1000

    print("Server:", response)
    print(f"TCP Latency: {latency:.2f} ms\n")

client.close()
print("[TCP CLIENT CLOSED]")