import socket

# Defines server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8080))
print("Port defined and bound")
# Opens log file (In final, replace log.txt with absolute path and hard-coded file)
log = open("log.txt", 'a')
print("Log file found and opened")
# Open socket
sock.listen(3)
print("Listening...\n")

# Infinitely receives client connections
while True:
	# Accepts client and saves its details as variables
	(clientsocket, address) = sock.accept()
	print("Accepted connection")
	# Receives data from client and writes data to log + new line
	data = clientsocket.recv(1024)
	print("Writing data...")
	log.write(data.decode() + "\n")
	# Acknowledges client and sends back response code. 0 for success, anything else for error
	clientsocket.send(("0").encode())
	print("Acknowledged\n")
