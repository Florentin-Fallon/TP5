import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3040))

s.listen(1)


while True:
        try:
            conn, addr = s.accept()
            print(f"Connexion établie avec {addr}")
            data = conn.recv(1024)
            print(f"Données reçues du client : {data}")
            if not data: 
                 break
            file = open("index.html")
            html = file.read()
            file.close()
            http_header = "HTTP/1.1 200 OK\n\nContent-Type: text/html\r\n\r\n" + html
            s.send(http_header.encode())
            conn.close()
        except socket.error as e:
            print(e)
            break

