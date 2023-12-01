import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3033))

s.listen(1)
conn, addr = s.accept()
print(f"Connexion établie avec {addr}")

while True:
        try:
            data = conn.recv(1024)
            print(f"Données reçues du client : {data}")
            if not data: 
                 break
            file = open("index.html", "rb")
            html = file.read()
            http_header = "HTTP/1.1 200 OK\n\nContent-Type: text/html\r\n\r\n" + html
            s.send(http_header.encode())
            file.close()
        except socket.error as e:
            print(e)
            break

conn.close()