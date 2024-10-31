import socket
import threading
import sys
from datetime import datetime

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"\n\033[92m{message}\033[0m")  # لون أخضر للرسائل الواردة
            else:
                break
        except Exception as e:
            print("Error receiving message:", e)
            break

def send_messages(sock, username):
    while True:
        message = input(f"\033[94m{username}:\033[0m ")
        timestamp = datetime.now().strftime('%H:%M:%S')
        full_message = f"[{timestamp}] {username}: {message}"
        sock.sendall(full_message.encode('utf-8'))

def main():
    host = input("Enter host (IP address of your friend): ")
    port = int(input("Enter port (default 5000): ") or 5000)
    username = input("Enter your username: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except ConnectionRefusedError:
        print("Connection failed. Make sure the server is running.")
        sys.exit()

    print("Connected to the chat! Type your messages below.")

    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()
    send_messages(sock, username)

if __name__ == "__main__":
    main()
