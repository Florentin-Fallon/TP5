import socket
import re

max_value = 4294967295  # 2^32 - 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))

msg = input("Veuillez saisir une expression arithmétique : ")

msg += "FIN"
header = len(msg).to_bytes(4, byteorder='big')
s.send(header)
s.send(msg.encode())

pattern = re.compile(r'^\s*\d+\s*[\+\-\*]\s*\d+\s*$')

if not pattern.match(msg):
    print("Expression invalide")
    exit()
else:
    try:
        match = re.match(r'^\s*(\d+)\s*([\+\-\*])\s*(\d+)\s*$', msg)
        x, operation, y = match.groups()

        x, y = int(x), int(y)
        if 0 <= x <= max_value and 0 <= y <= max_value:
            if operation == '+':
                result = str(x + y)
            elif operation == '-':
                result = str(x - y)
            elif operation == '*':
                result = str(x * y)
            else:
                raise ValueError("Opération invalide")
        else:
            raise ValueError("Nombres hors limite")

        print(f"Résultat de l'expression : {result}")

    except Exception as e:
        print("Erreur dans l'expression saisie", str(e))
        exit()

# Envoi de la requête au serveur
header = len(msg).to_bytes(4, byteorder='big')
s.send(header + msg.encode())

header = len(msg).to_bytes(4, byteorder='big')
clean_msg = msg.encode().lstrip(b'\x00')
s.send(header + clean_msg)

# Réception de la réponse du serveur
s_data = s.recv(1024)
print(s_data.decode())


response = s.recv(1024)
print(response.decode())

s.close()
