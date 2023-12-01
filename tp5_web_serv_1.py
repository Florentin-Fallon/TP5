import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1111))

s.listen(1)
conn, addr = s.accept()
print(f"Connexion établie avec {addr}")

while True:
        try:
            data = conn.recv(1024)
            print(f"Données reçues du client : {data}")
            if not data: 
                 break
            if data.decode().startswith("GET /"):
                conn.sendall("HTTP/1.0 200 OK\nContent-Type: text/html\n\n<h1>Hello je suis un serveur HTTP</h1> \n".encode())
                break
        except socket.error:
            print("Error Occured.")
            break

conn.close()