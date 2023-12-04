import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 3040
s.connect((host, port))

s.send(b"GET / \r\nHost: localhost\r\n\r\n")

data = s.recv(1024)
print(data.decode())

s.close()