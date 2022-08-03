from datetime import datetime
import time
import socket

# Define socket connection
LEADER = "127.0.0.1"
LEADERPORT = 8080
BUFFER = 1024

# Gets datetime and message to send
DATA = ((time.strftime(r"%d.%m.%Y %H:%M:%S", time.localtime()) + " - " + input("Enter a message to send: ")).encode())

# Opens client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((LEADER, LEADERPORT))

# Sends message
sock.send(DATA)

# Receives acknowledgement from server
REPLY = (sock.recv(1024).decode())
print("Acknowledged: " + REPLY)
