"""
Auteur : JP SPITONI
IUT Annecy
Département réseaux et télécommunication
Le 30/03/2020
Ce programme est un exercice proposé aux alternants RT1

Il s'agit de générer un mot de passe avec un nombre de caractères N choisi par l'utilisateur. 
le premiere fonction est : "mdp_base()". Elle génére un mot de passe de N caractères pris au hazard dans la liste TOTAL qui
est un mélange de minuscules, majuscules de chiffres et de caractères spéciaux pris dans la liste "CARACTERE". 

"""

import string
import random

# definition des constantes utiles pour la suite
MAJUS=list(string.ascii_uppercase)
MINUS =list(string.ascii_lowercase)
LETTRE = MAJUS + MINUS
DIGIT=list(string.digits)
CARACTERE=list("&#{}[]@()^%!?/$")
TOTAL=LETTRE + DIGIT + CARACTERE

def mdp_base(N):
    """
    cette fonction va nour retourner un mot de passe de longueur N
    Chacun des caractères du mot de passe est pris au hasard dans
    TOTAL
    :param N: entier nb de caratères du mdp
    :return: une chaine qui est le mot de passe "".join(L)
    """
    L=[] # liste des caractères du mot de passe
    for i in range(N):
        L.append(random.choice(TOTAL))
    return "".join(L)

def compte(temp):
    """
    cette fonction est capable de compter le nombre d'occurences
    de chacun des types de caractères suivants :
    MAJUS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MINUS = 'abcdefghijklmnopqrstuvwxyz'
    DIGIT = '0123456789'
    CARACTERE = '&#{}[]@()\^%!?/$'
    Le tout sera mis dans un dictionnaire d.
    Exemple :
    temp=['a','v','@', '5','R','j']
    d={"MINUS": 3, "MAJUS": 1, "DIGIT": 1, "CARACTERE": 1}
    :param temp: est une liste contenant les caractères du mot de passe
    :return: un dictionnaire avec les occurences de chacun des types cités plus haut
    """
    d = {"MINUS": 0, "MAJUS": 0, "DIGIT": 0, "CARACTERE": 0}
    for caractere in temp:
        if caractere in MINUS:
            d["MINUS"] = d["MINUS"] + 1
        elif caractere in MAJUS:
            d["MAJUS"] = d["MAJUS"] + 1
        elif caractere in DIGIT:
            d["DIGIT"] = d["DIGIT"] + 1
        elif caractere in CARACTERE:
            d["CARACTERE"] = d["CARACTERE"] + 1
    return d

def type_caractere(caractere):
    """
    cette fonction prend le caractère fourni en paramètre
    elle retourne son type parmi ces quatre valeurs
    "MAJUS", "MINUS", "DIGIT", "CARACTERE"
    :param caractere: c'est le caractère passé à la fonction. On veut trouver son type
    :return: le type du caractère "caractere"
    """
    dico = {1: "MAJUS", 2: "MINUS", 3: "DIGIT", 4: "CARACTERE"}
    # on regarde de quel type est du caractère
    # ttype = 1 => MAJUS
    # ttype = 2 => MINUS
    # ttype = 3 => DIGIT
    # ttype = 4 => CARACTERE
    if caractere in MAJUS:
        ttype = 1
    elif caractere in MINUS:
        ttype = 2
    elif caractere in DIGIT:
        ttype = 3
    elif caractere in CARACTERE:
        ttype = 4
    return dico[ttype]

def change_caractere1(liste):
    """
    la liste doit contenir un nombre N de caractères issue du même jeu
    - soit issu de MAJUS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    - soit issu de MINUS = 'abcdefghijklmnopqrstuvwxyz'
    - soit issu de DIGIT = '0123456789'
    - soit issu de CARACTERE = '&#{}[]@()^%!?/$+*'
    on doit changer le premier caractère de la liste
    pour qu'il soit d'un type différent
    Exemple : Liste=['A', 'B', 'C', 'D']. On doit changer le 'A' par un caractères autre qu'une majuscule
    cette focntion doit retourner la liste 'liste' avec le premier caractère changé
    liste retournés => ['k', 'B', 'C', 'D'] ou bien ['@', 'B', 'C', 'D'] ou bien ['@', 'B', 'C', 'D']
    :param liste: liste de N caractères de même type
    :return: liste, memoire
    liste est la liste avec le premier caractère qui a été changé
    memoire contient une chaine qui est soit "MAJUS" ou "MINUS" ou "DIGIT" ou alors"CARACTERE"
    La chaine memoire permet de savoir quels était le type du prmier caractère avant de le changer
    Exemple : liste = ['A', 'B', 'C', 'D'] => memoire = "MAJUS"
    si liste =['0', '7', '9', '4'] => memoire = "DIGIT"
    etc
    """

    # le dictionnaire d a comme clé le type de caractère et comme valeur l'association de tout les autres
    # types sauf celui de a clé.
    d={
        "MAJUS":MINUS+CARACTERE+DIGIT,
       "MINUS": MAJUS+CARACTERE+DIGIT,
       "DIGIT":MAJUS+MINUS+CARACTERE,
       "CARACTERE":MINUS+MAJUS+DIGIT
    }
    carac0=liste[0]
    type_carac0=type_caractere(carac0)
    # on veut changer ce type
    if type_carac0 == "MAJUS" :
        carac0=random.choice(d["MAJUS"])
        memoire ="MAJUS"
    elif type_carac0 == "MINUS" :
        carac0 = random.choice(d["MINUS"])
        memoire ="MINUS"
    elif type_carac0 == "DIGIT" :
        carac0 = random.choice(d["DIGIT"])
        memoire = "DIGIT"
    elif type_carac0 == "CARACTERE" :
        carac0 = random.choice(d["CARACTERE"])
        memoire = "CARACTERE"
    liste.pop(0)
    liste.insert(0,carac0)
    return liste, memoire



def mdp_gene(N,dec):
    """
    fonction qui génére un mot de passe
    :param N entier
    :param dec entier
    :return:
    """
    mdp=mdp_base(N)
    mdp=list(mdp)
    mdp_final=list()
    L=[]
    for i in range(0,N,dec):
        temp=mdp[i:i+dec]
        memoire = ""
        # dico qui compte le nombre de type de caractères
        # par tranche de "dec"
        d=compte(temp)
        if d['MINUS'] == dec and memoire != 'MINUS':
            liste_retour,memoire = change_caractere1(temp)
            L=L+temp
        elif d['MAJUS'] == dec and memoire != 'MAJUS':
            liste_retour, memoire = change_caractere1(temp)
            L=L+temp
        elif d['DIGIT'] == dec  and memoire != 'DIGIT':
            liste_retour, memoire = change_caractere1(temp)
            L=L+temp
        elif d['CARACTERE'] == dec and  memoire != 'CARACTERE':
            liste_retour, memoire = change_caractere1(temp)
            L=L+temp
        else:
            L=L+temp
    return L


if __name__=="__main__":
    a=mdp_gene(30,2)
    print(mdp_gene(20,2))
    print("".join(a))


    




