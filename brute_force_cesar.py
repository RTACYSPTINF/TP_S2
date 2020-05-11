# message à déchiffrer, on sait qu'il a été chiffré par la méthode de cesar
# on fait une recherche brute force
#○de 'A' à 'Z' on va de 65 à 90 inclus

import string
MAJUSCULE=list(string.ascii_uppercase)
message_chiff="RMACQADMVCRIQDCRIQDIQVKC"
#message_chiff=string.ascii_uppercase

def brute_force_cesar(message_chiffre):
    """
    help
    """
    d={}
    for i in range(0,26,1):
        d[i]=MAJUSCULE[i]
    L_message_chiff=list(message_chiff)
    liste_finale=[]
    for i in range(26):
        l_temp=[]
        for j in L_message_chiff:
            temp=d[((ord(j)-65+i+1)%26-1)%26]
            l_temp.append(temp)
        print("".join(l_temp))

if __name__=="__main__":
    brute_force_cesar(message_chiff)
    


