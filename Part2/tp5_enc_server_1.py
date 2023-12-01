import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8888))
s.listen(1)
conn, addr = s.accept()

while True:
    try:
        # On reçoit la longueur de l'en-tête du client
        header_length_bytes = conn.recv(4)
        if not header_length_bytes:
            break
        header_length = int.from_bytes(header_length_bytes, byteorder='big')

        # On reçoit l'en-tête du client
        header = conn.recv(header_length)

        # On reçoit le message du client basé sur la longueur de l'en-tête
        data_length_bytes = conn.recv(4)
        data_length = int.from_bytes(data_length_bytes, byteorder='big')

        data = conn.recv(data_length)
        message = data.decode()

        # Vérification de la séquence de fin
        if message.endswith("FIN"):
            print(f"Données reçues du client : {message[:-3]}")
            conn.send("Bien joué mec !".encode())
        else:
            print("Erreur: Séquence de fin manquante.")
            conn.send("Erreur: Séquence de fin manquante.".encode())

    except socket.error:
        print("Error Occurred.")
        break
