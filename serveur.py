import socket
import os

# dans cette partie, on va fonctionner en TCP
# on précise le type de socket et la couche transport --> TCP
connexion_principale=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

