from random import *
import base64
import os
import pickle

d={
    0: 'A', 17: 'R', 34: 'i', 51: 'z',
     1: 'B', 18: 'S', 35: 'j', 52: '0',
     2: 'C', 19: 'T', 36: 'k',53: '1', 
     3: 'D', 20: 'U', 37: 'l', 54: '2', 
     4: 'E', 21: 'V', 38: 'm', 55: '3', 
     5: 'F', 22: 'W', 39: 'n', 56: '4', 
     6: 'G', 23: 'X', 40: 'o', 57: '5', 
     7: 'H', 24: 'Y', 41: 'p', 58: '6', 
     8: 'I', 25: 'Z', 42: 'q', 59: '7', 
     9: 'J', 26: 'a', 43: 'r', 60: '8', 
     10: 'K', 27: 'b', 44: 's', 61: '9', 
     11: 'L', 28: 'c', 45: 't', 62: '+', 
     12: 'M', 29: 'd', 46: 'u', 63: '/', 
     13: 'N', 30: 'e', 47: 'v', 14: 'O', 
     31: 'f', 48: 'w', 15: 'P', 32: 'g', 
     49: 'x', 16: 'Q', 33: 'h', 50: 'y',
     'complement': '\\'}
# sauvegarde du dictionnaire
def sauve_dico():
    """
    permet de sauvegarder ou de récupérer le dictionnaire 
    du code b64
    """
    d={
    0: 'A', 17: 'R', 34: 'i', 51: 'z',
     1: 'B', 18: 'S', 35: 'j', 52: '0',
     2: 'C', 19: 'T', 36: 'k',53: '1', 
     3: 'D', 20: 'U', 37: 'l', 54: '2', 
     4: 'E', 21: 'V', 38: 'm', 55: '3', 
     5: 'F', 22: 'W', 39: 'n', 56: '4', 
     6: 'G', 23: 'X', 40: 'o', 57: '5', 
     7: 'H', 24: 'Y', 41: 'p', 58: '6', 
     8: 'I', 25: 'Z', 42: 'q', 59: '7', 
     9: 'J', 26: 'a', 43: 'r', 60: '8', 
     10: 'K', 27: 'b', 44: 's', 61: '9', 
     11: 'L', 28: 'c', 45: 't', 62: '+', 
     12: 'M', 29: 'd', 46: 'u', 63: '/', 
     13: 'N', 30: 'e', 47: 'v', 14: 'O', 
     31: 'f', 48: 'w', 15: 'P', 32: 'g', 
     49: 'x', 16: 'Q', 33: 'h', 50: 'y',
     'complement': '\\'}
    fichier="dico_b64.txt"
    chemin_b64=r"H:\Doc_jspit\GitHub\TP_S2"     
    os.chdir(chemin_b64)
    with open(fichier,'wb') as f:
        pickle.dump(d,f)
    
    # verif recup
    with open(fichier,'rb') as f:
        test=pickle.load(f)
    print("test vaut ", test)
    


fichier="code_b64.txt"
chemin_b64=r"H:\Doc_jspit\GitHub\TP_S2"

def recup_def_b64():
    """
    Cette fonction retourne les valeurs du code64 normalisé sous forme de dictionnaire
    """
    d={}
    fichier="code_b64.txt"
    chemin_b64=r"H:\Doc_jspit\GitHub\TP_S2"
    os.chdir(chemin_b64)
    with open(fichier) as f:
        recup=f.read()
    recup=recup.split()
    recup=recup[8:] # on supprime l'en tête 
    recup_2=recup[:]
    # on supprime les données binaires
    for i in recup:
        if len(i)==6:
            recup_2.remove(i)
    # creation du dictionnaire
    for i in recup_2:
        if i.isdigit():
            d[int(i)]=recup_2[recup_2.index(i)+1]
    return d  # attention, il manque le complément (=)
    

        

        


    # pour analyse du code on doit supprimer la ligne 1


recup_def_b64()
chaine="abcdefgh"

def otp_chiffre(chaine):
    """
    """
    # la longueur de la chine est N
    pass

def code_B64(chaine):
    pass


def creation_caracteres(N):
    """
    Crée autant de caractères 0 <= carac <= 255
    """
    l_temp=[]
    for i in range(N):
        l_temp.append(chr(randint(0,255)))
    return "".join(l_temp)
    print(l_temp)

#print("\n",creation_caracteres(100))
print(d)
sauve_dico()