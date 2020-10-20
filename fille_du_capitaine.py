"""
Ce problème est un classique. Un captaine et son second on une discussion qui prend la forme d'une énigme.
Voici le contenu de leurs échanges :

Dialogue entre le capitaine et son second
Capitaine : J'ai rencontré 3 filles et le produit de leurs âges est 2450.
Son second : Je ne peux pas déterminer leurs âges avec si peu d'information.
Capitaine : J'ajoute que la somme de leurs âges est égale au double du mien.
Son second : Je ne peux toujours pas !
Capitaine : Et enfin, la plus âgée est au moins aussi vieille que moi.
Son second : Ca y est !!! Maintenant je sais.

Trouver l'Age du capitaine??

Ce problème est un problème logique où intervient le dénombrement

2tapes de réalisation en python :

1) trouver tous les diviseurs de 2450
2) A l'aide de ces diviseurs, trouver tous les triplets de diviseurs dont le produit donne 2450
3) il faut maintenant éliminer tous les triplet dont le max est supérieur à 100 ans (réalité)

Les modules dont on va avoir besoin
itertools (import itertools) dont on pourra consulter la doc avec grand profit.

Les fonctions à écrire

def diviseur(N)
qui renvoie une liste avec tous les diviseurs de l'entier N (dans notre cas N=2450)

def age_possible(liste)
liste correspond à une liste avec tous les diviseurs possibles de N
renvoie une liste avec des triplés (tuple) dont le produit vaut N (2450 dans notre cas)

"""

import itertools
import operator

N=2450

def  diviseur(N):
    """
    input :
    N est un entier
    output :
    renvoie une liste qui contient tous les diviseurs de N
    La boucle for suffit quand elle atteind N/2 puisque aucun diviseur supposé ne saurait être supérieur à N/2
    """
    N_sup=N # plus grand diviseur de N qui est lui même
    cpt=0
    if N%2==0:
        N=int(N/2)
    else:
        N=int((N+1)/2)
    l_diviseurs_finale=[]
    for i in range(1,N+1):
        if N_sup%i==0:
            cpt+=1
            l_diviseurs_finale.append(i)
    return l_diviseurs_finale

l_diviseur=diviseur(N)
print(l_diviseur)


def age_possible(liste,N):
    """

    """
    a=list(itertools.combinations(liste,3))
    div_inter=[] # liste intermédiaire des triplés de diviseurs dont le max est plus petit que N
    div_final=[]
    # on ne garde parmis ces triplés que ceux dont le produit est égal à N (2450 dans notre exercice)
    for i in a:
        if max(i)<=100:
            div_inter.append(i)
    # On ne garde que les triplets dont le produit est égal à 2450
    for i in div_inter:
        r=1
        for j in i:
            r=r*j
        if r==2450:
            div_final.append(i)
    return div_final

l=age_possible(l_diviseur,N)
print(l)
for i in l:
    print(i)

def age_capitaine(N):
    """
    Dans les triples précedemment calculés, on va regarder les doublon sur l'ainée et on les supprime
    """
    div_N=diviseur(N)
    age_possib=age_possible(div_N,N)
    # on recherche le max de chacun des trplés de age_possib
    print(age_possib)
    age_fille_capitaine=[]
    for i in age_possib:
        age_fille_capitaine.append([i,sum(i)/2])
    print(age_fille_capitaine)
    return age_fille_capitaine


a=age_capitaine(N)
for i in a:
    print(i)







