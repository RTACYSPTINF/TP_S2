import string

def cesar(chaine, dec):
    """
    """
    liste_finale=[]
    chaine=chaine.upper()   
    alphabet=list(string.ascii_uppercase)
    for i in chaine:
        temp=(ord(i)-65+dec)%26
        print((ord(i)-65+dec)%26)
        carac_dec=chr(temp+65)
        liste_finale.append(carac_dec)
        print(liste_finale)


cesar("zab",-236)