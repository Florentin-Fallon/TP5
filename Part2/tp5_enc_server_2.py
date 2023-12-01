import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8888))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit la string Hello du client
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")


        conn.send("Bien jouer mec !".encode())

        # On reçoit la longueur du calcul du client
        data_length_bytes = conn.recv(4)
        data_length = int.from_bytes(data_length_bytes, byteorder='big')

        # On reçoit le calcul du client
        expression = data.decode().lstrip('\x00')
        # Nettoyer la chaîne avant d'évaluer
        expression = ''.join(char for char in expression if char.isalnum() or char in {'+', '-', '*'})
        try:
            # Evaluation du résultat
            res = eval(expression)
            conn.send(str(res).encode())
        except Exception as e:
            print("Erreur lors de l'évaluation de l'expression :", str(e))
            conn.send("Erreur lors de l'évaluation de l'expression".encode())




    except socket.error:
        print("Error Occured.")
        break