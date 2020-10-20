import socket
import os

# dans cette partie, on va fonctionner en TCP
# on précise le type de socket et la couche transport --> TCP
# le paramètre qui indqiue que le scket est en TCP est : socket.SOCK_STREAM

connexion_principale=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

