# II. Opti calculatrice
# 0. Setup
# 1. Strings sur mesure
# 🌞 tp5_enc_client_1.py
Voici le fichier avec le code qu'il faut pour réalisez toutes les demandes :

* [tp5_enc_client_1.py](tp5_enc_client_1.py)
# 🌞 tp5_enc_server_1.py
Voici le fichier avec le code qu'il faut pour réalisez toutes les demandes :

* [tp5_enc_server_1.py](tp5_enc_server_1.py)
# 2. Code Encode Decode

# 🌞 tp5_enc_client_2.py et tp5_enc_server_2.py

# III. Serveur Web HTTP

# 0. Ptite intro HTTP
# 1. Serveur Web
# 🌞 tp5_web_serv_1.py un serveur HTTP super basique

Voici le fichier [click-here](tp5_web_serv_1.py) avec le contenu coté serveur :<br>


Le ***curl*** :

```bash
florentinfallon@MacBook-Pro-de-Florentin TP5 % curl localhost:2222
<h1>Hello je suis un serveur HTTP</h1>     
```

Le ***GET*** :

```bash
florentinfallon@MacBook-Pro-de-Florentin TP5 % nc localhost 1111
GET /
HTTP/1.0 200 OK
Content-Type: text/html

<h1>Hello je suis un serveur HTTP</h1>      
```

# 2. Client Web
# 🌞 tp5_web_client_2.py un client HTTP super basique

Voici le fichier [Click-here](tp5_web_client_2.py) :

Voici le résultat reçu avec le ***client*** :

```bash
florentinfallon@MacBook-Pro-de-Florentin TP5 % python3 tp5_web_client_2.py
HTTP/1.0 200 OK
Content-Type: text/html

<h1>Hello je suis un serveur HTTP</h1> 
```

Voici le résultat du coté du ***serveur*** :

```bash
florentinfallon@MacBook-Pro-de-Florentin TP5 % python3 tp5_web_serv_1.py
Connexion établie avec ('127.0.0.1', 52307)
Données reçues du client : b'GET / \r\nHost: localhost\r\n\r\n'
```
# 3. Délivrer des pages web
# 🌞 tp5_web_serv_3.py


# 4. Quelques logs
# 🌞 tp5_web_serv_4.py


# 5. File download
# 🌞 tp5_web_serv_5.py