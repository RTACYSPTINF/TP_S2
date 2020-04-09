

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 08:04:23 2018

@author: jspit
"""
import string
import os
import copy
import numpy as np
import math
import itertools
import operator # utilisé pour le tri d'une liste de tuple sur un des éléments




class Chiffrement:
    def __init__(self):
        print("initialisation de l'instance")
        self.minus=string.ascii_lowercase
        self.majusc=string.ascii_uppercase
    
    def is_doublon(self,chaine):
        """
        permet de renvoyer un booléen.
        Renvoit True si il y a présence d'un doublon dans la chaine
        sinon, renvoie True
        Exemple is_doublon('ABCDEFAG') renvoie True parce qu'il y a deux 'A'
        id_doublon('ABCDEF') renvoie False
        """
        for i in chaine:
            m=chaine.count(i)
            if m>1:
                return True
                break
        return False
            
    
    def cinq_carac(self,chaine):
        """On cherche à représenter une chaine sans espace, en majuscule par 
        groupe de 5 caracteres
        exemple, 'coucou comment vas tu' donnera : COUCO UCOMM ENTVA STU
        """
        chaine_finale=""
        # on converti la chaine en liste
        chaine=chaine.upper()
        liste_chaine=chaine.split()
        liste_chaine="".join(liste_chaine)
        # on supprime les espaces
        print(liste_chaine)
        
        for indice,valeur in enumerate(liste_chaine):
            if indice%5==4: # on insere un espace dans la chaine finale
                chaine_finale+=valeur+" "
            elif indice%50==49:
                chaine_finale+="\n"
            else :
                chaine_finale+=valeur
        return chaine_finale
    
    def cesar(self,chaine,decalage):
        """méthode qui permet à partir d'une chaine
        de donner une chaine décalée de du nombre entier 'decalage'
        Exemple pour la chaine 'coucou' avec un decalage de 2 on obtient 
        la chaine 'eqweqw'
        """
        #On crée deux dictionnaire qui donne chacun, la correspondance entre minuscule et valeur unicode puis
        #majuscule et valeur unicode
        dico_minus={}
        dico_majusc={}
        for i in self.minus:
            dico_minus[i]=ord(i)
        for i in self.majusc:
            dico_majusc[i]=ord(i)
        # on ramène le décalage à une valeur raisonnablecomprise entre 0 et 26
        decalage=decalage%26
        
        code_final=""  #♦ on prepare la chaine finale qu'on relplie au fur et à mesure
        for i in chaine:
            if i in dico_minus:
                if (ord(i)+decalage) > ord('z'):
                    N=97+dico_minus[i]+decalage-(122+1)
                    code_final+=chr(N)
                else:
                    N=(dico_minus[i]+decalage)
                    code_final+=chr(N)
            if i in dico_majusc:
                if (ord(i)+decalage)>ord('Z'):
                    N=65+dico_majusc[i]+decalage-(90+1)
                    code_final+=chr(N)
                else:
                    N=(dico_majusc[i]+decalage)
                    code_final+=chr(N)
        code_final=self.cinq_carac(code_final)
        return code_final
        
        
    def atbash_chiffre(self,chaine):
        """
        Ressources : http://www.bibmath.net/crypto/index.php?action=affiche&quoi=ancienne/atbash
        Méthode qui permet de chiffrer avec une technique utilisée par les hébreux 
        500 ans avant JC. C'est une technique de substition.
        Le principe est d'utiliser l'alphabet comme un mirroir
        ABCDEFGHIJKLMNOPQRSTUVWXYZ  alphabet normal
        ZYXWVUTSRQPONMLKJIHGFEDCBA  alphabet mirroir.
        Le A sera permuté avec le Z, Le B avec le Y, ainsi de suite jusqu'au Z permuté avec le A.
        """
        chaine_alpha=string.ascii_uppercase
        # on converti la chaine en lettres  majuscules
        temp=chaine.split()
        chaine="".join(temp)
        chaine=chaine.upper()
        # dict_direct=dictionnaire qui contient comme clé les lettre dans l ordre alaphabetique
        # et comme valeurs, l'equivalent mirroir
        dico_direct={}  # création du dictionnaire vide
        dico_inverse={}
        # on crée 2 listes alpha_directe et alpha_inverse
        alpha_directe=list(chaine_alpha) # ceci est la liste directe
        alpha_inverse=copy.deepcopy(alpha_directe)
        alpha_inverse.reverse()
        # création du dico directe
        for indice,valeur in enumerate(chaine_alpha):
            dico_direct[valeur]=alpha_inverse[indice]
        # création du dico inverse
        for indice,valeur in enumerate(alpha_inverse):
            dico_inverse[valeur]=alpha_directe[indice]
        #On va chiffrer la chaine qui est en majuscule
        chaine_chiffre=""
        for i in chaine:
            chaine_chiffre+=dico_inverse[i]
        # on crée des groupe de cinq lettres
        temp=self.cinq_carac(chaine_chiffre)
        return temp
    
    
    def atbash_dechiffre(self,chaine):
        """
        Ressources : http://www.bibmath.net/crypto/index.php?action=affiche&quoi=ancienne/atbash
        Méthode qui permet de chiffrer avec une technique utilisée par les hébreux 
        500 ans avant JC. C'est une technique de substition.
        Le principe est d'utiliser l'alphabet comme un mirroir
        ABCDEFGHIJKLMNOPQRSTUVWXYZ  alphabet normal
        ZYXWVUTSRQPONMLKJIHGFEDCBA  alphabet mirroir.
        Le A sera permuté avec le B, Le B avec le Y, ainsi de suite jusqu'au Z permuté avec le A.
        REMARQUE : on peut noté qu'avec le systeme de chiffrement de Atbash, 
        le chiffrement et le déchiffrement font appel au même agorithme. 
        Donc, l'algo de déchiffrement est totalement inutile
        """
        chaine_alpha=self.majusc
        # on converti la chaine en lettres  majuscules
        temp=chaine.split() # on eclate la chaine
        chaine="".join(temp)# on reconstruit la chaine sans les espaces
        chaine=chaine.upper()
        # dict_direct=dictionnaire qui contient comme clé les lettre dans l ordre alaphabetique
        # et comme valeurs, l'equivalent mirroir
        dico_direct={}  # création du dictionnaire vide
        dico_inverse={}
        # on crée 2 listes alpha_directe et alpha_inverse
        alpha_directe=list(chaine_alpha) # ceci est la liste directe
        alpha_inverse=copy.deepcopy(alpha_directe)
        alpha_inverse.reverse()
        # création du dico directe
        for indice,valeur in enumerate(chaine_alpha):
            dico_direct[valeur]=alpha_inverse[indice]
        # création du dico inverse
        for indice,valeur in enumerate(alpha_inverse):
            dico_inverse[valeur]=alpha_directe[indice]
        #On va chiffrer la chaine qui est en majuscule
        chaine_chiffre=""
        for i in chaine:
            chaine_chiffre+=dico_inverse[i]
        return chaine_chiffre
    
    
    def subsitution_chaine(self,cle):
        """
        cette fonction permet de créer une substitution précédée d'une clé connue.
        Exemple :
        avec la clé MATHWEB
        on passe de 
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        à
        MATHWEBCDFGIJKLNOPQRSUVXYZ
        dans cette méthode, on va utiliser la méthode is_doublon(self, chaine)
        
        ATTENTION : la clé ne doit pas avoir de doublon.
        """
        alpha=self.majusc
        alpha=list(alpha)
        cle=cle.upper()
        # on va substituer à cet alphabet les lettres de la clé
        for i in cle:
            if i in alpha:
                alpha.remove(i)
        alpha="".join(alpha)
        return cle+alpha
                
        
        
        
        
    
    def vigenere_chiffre(self,chaine_a_chiffrer, cle_chiffrement):
        """
        Ressources : http://www.bibmath.net/crypto/index.php?action=affiche&quoi=poly/vigenere
        Methode qui permet de chiffrer une chaine de caracteres.
        L'idée de Vigenère cconsiste utiliser un chiffre de César, 
        mais où le décalage utilisé change de lettres en lettres. 
        Pour cela, on utilise une table composée de 26 alphabets, 
        écrits dans l'ordre, mais décalés de ligne en ligne d'un caractère. 
        On écrit encore en haut un alphabet complet, pour la clé, et à gauche, 
        verticalement, un dernier alphabet, pour le texte à coder :
            
        ---------------------------
        ABCDEFGHIJKLMNOPQRSTUVWXYZ        
        ___________________________
        A=ABCDEFGHIJKLMNOPQRSTUVWXYZ
        B=BCDEFGHIJKLMNOPQRSTUVWXYZA
        C=CDEFGHIJKLMNOPQRSTUVWXYZAB
        D=DEFGHIJKLMNOPQRSTUVWXYZABC
        E=EFGHIJKLMNOPQRSTUVWXYZABCD
        F=FGHIJKLMNOPQRSTUVWXYZABCDE
        G=GHIJKLMNOPQRSTUVWXYZABCDEF
        H=HIJKLMNOPQRSTUVWXYZABCDEFG
        I=IJKLMNOPQRSTUVWXYZABCDEFGH
        J=JKLMNOPQRSTUVWXYZABCDEFGHI
        L=KLMNOPQRSTUVWXYZABCDEFGHIJ
        L=LMNOPQRSTUVWXYZABCDEFGHIJK
        M=MNOPQRSTUVWXYZABCDEFGHIJKL
        N=NOPQRSTUVWXYZABCDEFGHIJKLM
        O=OPQRSTUVWXYZABCDEFGHIJKLMN
        P=PQRSTUVWXYZABCDEFGHIJKLMNO
        Q=QRSTUVWXYZABCDEFGHIJKLMNOP
        R=RSTUVWXYZABCDEFGHIJKLMNOPQ
        S=STUVWXYZABCDEFGHIJKLMNOPQR
        T=TUVWXYZABCDEFGHIJKLMNOPQRS
        U=UVWXYZABCDEFGHIJKLMNOPQRST
        V=VWXYZABCDEFGHIJKLMNOPQRSTU
        W=WXYZABCDEFGHIJKLMNOPQRSTUV
        X=XYZABCDEFGHIJKLMNOPQRSTUVW
        Y=YZABCDEFGHIJKLMNOPQRSTUVWX
        Z=ZABCDEFGHIJKLMNOPQRSTUVWXY
        
        Pour coder le message on choisit une clé quelconque, par exemple :
        CLEDEMO
        La chaine à chiffrer est : je suis etudiant en RT et jaime ca
        On cancatène la chaine à chiffrer :JESUISETUDIANTENRTETJAIMECA
        On complète la clé autant de fois que nécessaire pour atteindre 
        la longueur de la chaine :
         JESUISETUDIANTENRTETJAIMECA
         CLEDEMOCLEDEMOCLEDEMOCLEDEM
         dans notre exemple la clé CLEDEMO est recopiée presque 4 fois
         Pour chiffrer la premiere lettre qui est un J, on prend la lettre de la clé qui 
         est en dessous du J
         et on trouve : C
         J--> C, on regarde dans la matrice et on a la lettre a la lettre L qui est l'intersection
         de la ligne indicée par J et de la colone indicée par C.
         On continu ainsi de suite pour chiffrer toute la chaine avec la même façon de procéder.
        """
        # on commence par concaténer la chaine à chiffrer et mettre le tout en majuscules
        temp=chaine_a_chiffrer.split()
        chaine_a_chiffrer="".join(temp)
        chaine_a_chiffrer=chaine_a_chiffrer.upper()
        # idem pour la clé
        temp=cle_chiffrement.split()
        cle_chiffrement="".join(temp)
        cle_chiffrement=cle_chiffrement.upper()
        # le masque de clé est la clé répétée autant de fois qu'il faut
        # pour atteindre la longueur de la chaine à chiffrer
        taille_chaine_a_chiffrer=len(chaine_a_chiffrer)
        taille_cle_de_chiffrement=len(cle_chiffrement)
        if taille_chaine_a_chiffrer > taille_cle_de_chiffrement:
            q=taille_chaine_a_chiffrer//taille_cle_de_chiffrement
            r=taille_chaine_a_chiffrer%taille_cle_de_chiffrement
            chaine_a_chiffrer=chaine_a_chiffrer
            cle_chiffrement=cle_chiffrement*q+cle_chiffrement[0:r]
        else : 
            chaine_a_chiffrer=chaine_a_chiffrer
            cle_chiffrement=cle_chiffrement[0:len(chaine_a_chiffrer)]
        #print(chaine_a_chiffrer)
        #print(cle_chiffrement)
        # création de deux listes pour mettre en correspondance,
        # les lettres de la chaine à chiffrer avec celles de la clé de chiffrement
        liste_chaine_a_chiffrer=list(chaine_a_chiffrer)
        liste_cle_chiffrement=list(cle_chiffrement)
        #print(liste_chaine_a_chiffrer)
        #print(liste_cle_chiffrement)
        matrice={'A':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                 'B':'BCDEFGHIJKLMNOPQRSTUVWXYZA',
                 'C':'CDEFGHIJKLMNOPQRSTUVWXYZAB',
                 'D':'DEFGHIJKLMNOPQRSTUVWXYZABC',
                 'E':'EFGHIJKLMNOPQRSTUVWXYZABCD',
                 'F':'FGHIJKLMNOPQRSTUVWXYZABCDE',
                 'G':'GHIJKLMNOPQRSTUVWXYZABCDEF',
                 'H':'HIJKLMNOPQRSTUVWXYZABCDEFG',
                 'I':'IJKLMNOPQRSTUVWXYZABCDEFGH',
                 'J':'JKLMNOPQRSTUVWXYZABCDEFGHI',
                 'K':'KLMNOPQRSTUVWXYZABCDEFGHIJ',
                 'L':'LMNOPQRSTUVWXYZABCDEFGHIJK',
                 'M':'MNOPQRSTUVWXYZABCDEFGHIJKL',
                 'N':'NOPQRSTUVWXYZABCDEFGHIJKLM',
                 'O':'OPQRSTUVWXYZABCDEFGHIJKLMN',
                 'P':'PQRSTUVWXYZABCDEFGHIJKLMNO',
                 'Q':'QRSTUVWXYZABCDEFGHIJKLMNOP',
                 'R':'RSTUVWXYZABCDEFGHIJKLMNOPQ',
                 'S':'STUVWXYZABCDEFGHIJKLMNOPQR',
                 'T':'TUVWXYZABCDEFGHIJKLMNOPQRS',
                 'U':'UVWXYZABCDEFGHIJKLMNOPQRST',
                 'V':'VWXYZABCDEFGHIJKLMNOPQRSTU',
                 'W':'WXYZABCDEFGHIJKLMNOPQRSTUV',
                 'X':'XYZABCDEFGHIJKLMNOPQRSTUVW',
                 'Y':'YZABCDEFGHIJKLMNOPQRSTUVWX',
                 'Z':'ZABCDEFGHIJKLMNOPQRSTUVWXY',
                 }
        # on commence le chiffrement
        dico_colone={} # dico qui donne la carrespondance entre valeur colone et indice colone
        for indice,valeur in enumerate(string.ascii_uppercase):
            dico_colone[valeur]=indice
        liste_chiffrement=[] # liste qui contient 
        for indice,valeur in enumerate(chaine_a_chiffrer):
            X=valeur # lettre de la ligne
            Y=cle_chiffrement[indice]# lettre de la colone
            # il nous faut indice de la colone indice_colone
            #print(X,"  ",Y)
            # X est la valeur de la lettre en ligne
            # Y est la valeur de la lettre en colone, il nous reste à treouver son indice
            # pour utiliser la matrice
            # or l'indice de Y est le meme que celui de X
            # il est donné par la variable 'indice'
            temp=indice
            lettre_chiffres=matrice[X][dico_colone[Y]]
            liste_chiffrement.append(lettre_chiffres)
        final_chiffrement="".join(liste_chiffrement)
        final_chiffrement=self.cinq_carac(final_chiffrement)
        return final_chiffrement
          
         
    def vigenere_dechiffre(self,chaine_a_chiffrer, cle_chiffrement):
        """
        Ressources : http://www.bibmath.net/crypto/index.php?action=affiche&quoi=poly/vigenere
        Methode qui permet de chiffrer une chaine de caracteres.
        L'idée de Vigenère cconsiste utiliser un chiffre de César, 
        mais où le décalage utilisé change de lettres en lettres. 
        Pour cela, on utilise une table composée de 26 alphabets, 
        écrits dans l'ordre, mais décalés de ligne en ligne d'un caractère. 
        On écrit encore en haut un alphabet complet, pour la clé, et à gauche, 
        verticalement, un dernier alphabet, pour le texte à coder :
            
        ---------------------------
          ABCDEFGHIJKLMNOPQRSTUVWXYZ        
        ___________________________
        A=ABCDEFGHIJKLMNOPQRSTUVWXYZ
        B=BCDEFGHIJKLMNOPQRSTUVWXYZA
        C=CDEFGHIJKLMNOPQRSTUVWXYZAB
        D=DEFGHIJKLMNOPQRSTUVWXYZABC
        E=EFGHIJKLMNOPQRSTUVWXYZABCD
        F=FGHIJKLMNOPQRSTUVWXYZABCDE
        G=GHIJKLMNOPQRSTUVWXYZABCDEF
        H=HIJKLMNOPQRSTUVWXYZABCDEFG
        I=IJKLMNOPQRSTUVWXYZABCDEFGH
        J=JKLMNOPQRSTUVWXYZABCDEFGHI
        L=KLMNOPQRSTUVWXYZABCDEFGHIJ
        L=LMNOPQRSTUVWXYZABCDEFGHIJK
        M=MNOPQRSTUVWXYZABCDEFGHIJKL
        N=NOPQRSTUVWXYZABCDEFGHIJKLM
        O=OPQRSTUVWXYZABCDEFGHIJKLMN
        P=PQRSTUVWXYZABCDEFGHIJKLMNO
        Q=QRSTUVWXYZABCDEFGHIJKLMNOP
        R=RSTUVWXYZABCDEFGHIJKLMNOPQ
        S=STUVWXYZABCDEFGHIJKLMNOPQR
        T=TUVWXYZABCDEFGHIJKLMNOPQRS
        U=UVWXYZABCDEFGHIJKLMNOPQRST
        V=VWXYZABCDEFGHIJKLMNOPQRSTU
        W=WXYZABCDEFGHIJKLMNOPQRSTUV
        X=XYZABCDEFGHIJKLMNOPQRSTUVW
        Y=YZABCDEFGHIJKLMNOPQRSTUVWX
        Z=ZABCDEFGHIJKLMNOPQRSTUVWXY
        
        Pour coder le message on choisit une clé quelconque, par exemple :
        CLEDEMO
        La chaine à chiffrer est : je suis etudiant en RT et jaime ca
        On cancatène la chaine à chiffrer :JESUISETUDIANTENRTETJAIMECA
        On complète la clé autant de fois que nécessaire pour atteindre 
        la longueur de la chaine :
         JESUISETUDIANTENRTETJAIMECA
         CLEDEMOCLEDEMOCLEDEMOCLEDEM
         dans notre exemple la clé CLEDEMO est recopiée presque 4 fois
         Pour chiffrer la premiere lettre qui est un J, on prend la lettre de la clé qui est en dessous du J
         et on trouve : C
         J--> C, on regarde dans la matrice et on a la lettre a la lettre L qui est l'intersection
         de la ligne indicée par J et de la colone indicée par C.
         On continu ainsi de suite pour chiffrer toute la chaine avec la même façon de procéder.
        """
        # on commence par concaténer la chaine à chiffrer et mettre le tout en majuscules
        #########################################################################
        #########################################################################
        # MISE EN FORME DE LA CHAINE ET DE LA CLE
        #########################################################################
        #########################################################################
        temp=chaine_a_chiffrer.split()
        chaine_a_chiffrer="".join(temp)
        chaine_a_chiffrer=chaine_a_chiffrer.upper()
        # idem pour la clé
        temp=cle_chiffrement.split()
        cle_chiffrement="".join(temp)
        cle_chiffrement=cle_chiffrement.upper()
        # le masque de clé est la clé répétée autant de fois qu'il faut
        # pour atteindre la longueur de la chaine à chiffrer
        taille_chaine_a_chiffrer=len(chaine_a_chiffrer)
        taille_cle_de_chiffrement=len(cle_chiffrement)
        if taille_chaine_a_chiffrer > taille_cle_de_chiffrement:
            q=taille_chaine_a_chiffrer//taille_cle_de_chiffrement
            r=taille_chaine_a_chiffrer%taille_cle_de_chiffrement
            chaine_a_chiffrer=chaine_a_chiffrer
            cle_chiffrement=cle_chiffrement*q+cle_chiffrement[0:r]
        else : 
            chaine_a_chiffrer=chaine_a_chiffrer
            cle_chiffrement=cle_chiffrement[0:len(chaine_a_chiffrer)]
        #print(chaine_a_chiffrer)
        #print(cle_chiffrement)
        # création de deux listes pour mettre en correspondance,
        # les lettres de la chaine à chiffrer avec celles de la clé de chiffrement
        liste_chaine_a_chiffrer=list(chaine_a_chiffrer)
        liste_cle_chiffrement=list(cle_chiffrement)
        print("chaine chiffrée  ",liste_chaine_a_chiffrer)
        print(" liste clé de chiffrement  ",liste_cle_chiffrement)
        #########################################################################
        #########################################################################
        #  FIN DE LA MISE EN FORME DE LA CHAINE ET DE LA CLE
        #########################################################################
        #########################################################################
        matrice={'A':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                 'B':'BCDEFGHIJKLMNOPQRSTUVWXYZA',
                 'C':'CDEFGHIJKLMNOPQRSTUVWXYZAB',
                 'D':'DEFGHIJKLMNOPQRSTUVWXYZABC',
                 'E':'EFGHIJKLMNOPQRSTUVWXYZABCD',
                 'F':'FGHIJKLMNOPQRSTUVWXYZABCDE',
                 'G':'GHIJKLMNOPQRSTUVWXYZABCDEF',
                 'H':'HIJKLMNOPQRSTUVWXYZABCDEFG',
                 'I':'IJKLMNOPQRSTUVWXYZABCDEFGH',
                 'J':'JKLMNOPQRSTUVWXYZABCDEFGHI',
                 'K':'KLMNOPQRSTUVWXYZABCDEFGHIJ',
                 'L':'LMNOPQRSTUVWXYZABCDEFGHIJK',
                 'M':'MNOPQRSTUVWXYZABCDEFGHIJKL',
                 'N':'NOPQRSTUVWXYZABCDEFGHIJKLM',
                 'O':'OPQRSTUVWXYZABCDEFGHIJKLMN',
                 'P':'PQRSTUVWXYZABCDEFGHIJKLMNO',
                 'Q':'QRSTUVWXYZABCDEFGHIJKLMNOP',
                 'R':'RSTUVWXYZABCDEFGHIJKLMNOPQ',
                 'S':'STUVWXYZABCDEFGHIJKLMNOPQR',
                 'T':'TUVWXYZABCDEFGHIJKLMNOPQRS',
                 'U':'UVWXYZABCDEFGHIJKLMNOPQRST',
                 'V':'VWXYZABCDEFGHIJKLMNOPQRSTU',
                 'W':'WXYZABCDEFGHIJKLMNOPQRSTUV',
                 'X':'XYZABCDEFGHIJKLMNOPQRSTUVW',
                 'Y':'YZABCDEFGHIJKLMNOPQRSTUVWX',
                 'Z':'ZABCDEFGHIJKLMNOPQRSTUVWXY',
                 }
        # on commence le dechiffrement
        chaine_finale=[]
        for indice,valeur in enumerate(cle_chiffrement):
            a=matrice[valeur]
            print(a,"   ",indice,"    ",valeur)
            temp=chaine_a_chiffrer[indice]
            # on calcule l indice de la lettre a dechiffer dans la variable a
            print("tremp vaut : ",temp)
            t=a.index(temp)
            chaine_finale.append(self.majusc[t])
        chaine_finale="".join(chaine_finale)
        return chaine_finale
        
    
             
            
            
            
    def chiffre_ubchi(self,phrase,cle):
        """
        voir : http://www.bibmath.net/crypto/index.php?action=affiche&quoi=debvingt/ubchi
        Le chiffre UBCHI est une succession de deux transpositions rectangulaires avec 
        la même clé. Prenons un exemple. Nous voulons chiffrer 
        "ACHEMINEMENT DE MUNITIONS" avec le mot clé VERDUN. On commence par écrire 
        la clé dans un tableau, et on recopie le texte comme ci-dessous. On numérote 
        chaque colonne suivant l'ordre alphabétique des lettres de la clé :
        """  
        # création d'une liste qui donne les numéros de placement par ordre alphabétique
        # exemple 'UNETE' donne liste_num_alpha-->[5,3,1,4,2]
        pass
        
        
            
    
         
        
        
    def test_cle_sans_doublon(self,cle):
        """
        ressources : http://www.bibmath.net/crypto/index.php?action=affiche&quoi=debvingt/ubchi
        permet de vérifier qu'aucune lettre du mot clé est en doublon
        retourne True si aucune lettres en double
        retourne False si lettre en double
        """   
        # on vérifie que la clé n'a pas de caractères en double
        # suppression des espaces
        cle_temp=cle.split()
        cle = "".join(cle_temp)
        liste_cle=cle.upper() # mise en majuscule
        liste_cle=list(liste_cle)
        for indice,lettre in enumerate(liste_cle):
            cle_temp=copy.deepcopy(liste_cle)
            cle_temp.pop(indice)
            print(indice, lettre)
            print(cle_temp)
            if lettre in cle_temp:
                print(lettre)
                return False
                break
        return True
            # on crée une sous liste sans la lettre 'lettre'    
        
        
    def num_lettre_alphabet(self,lettre):
        """
        le but est de donner le numéro de la position de la lettre dans l'alphabet. 
        On ne traite que des cas où lla lettre est en majuscule.
        Par exemple la lettre 'a' a la position 1
        la lettre 'c' a la position 3
        """
        if lettre in list(string.ascii_uppercase):
            return  ord(lettre)-ord('A')+1   
        
        
    def position_cara(self,chaine):
        """
        permet de donner la position de chaque lettre de la chaine cle en fonction
        de sa position dans l'alphabet.
        Par exemple : chaine='ATUOAER' on obtient unbe liste de tuple :
        [('A',1),('T',6),('U',7),('O',4),('A',2),('E',3),('R',5),]
        liste_finale représente une liste de Tuple avec la position alpha et numérique
        cle='ATUOAER' on trouve :
        liste_finale
        [('A', 1), ('T', 20), ('U', 21), ('O', 15), ('A', 1), ('E', 5), ('R', 18)]
        """    
        # on supprime les espaces éventuels
        # et on met tous les caractères en majuscule dans chaine
        chaine=chaine.upper()
        chaine=list(chaine)
        
        # comptage des occurences
        occurences={}
        for i in chaine:
            occurences[i]=occurences.get(i,0)+1
        print("comptage occurences : ",occurences )
        # fin de comptage des occurences    
        
        # dico_final donne la liste des tuples des occurences
        # exemple chaine ='AACCBB' donne
        # {'A':[(''A',1), ('A',2)], 'B':[('B',3), ('B',4)], 'C': [('C',5), ('C',6)]}
        majuscule=self.majusc
        dico_final={}
        cpt=1
        for i in majuscule:
            temp=[]
            #cpt=1
            for j in chaine:
                if j==i:
                   temp.append((i,cpt))
                   cpt+=1
                dico_final[i]=temp
        print("dico final : ",dico_final )
        # suppression des valeur egale à []
        # on crée une copie de dico_final appelée dico_final_copy
        #  ATTENTION de faire une deepcopy pour eviter les pbs de référence partagées
        dico_final_copy=copy.deepcopy(dico_final)
        for k,v in dico_final_copy.items():
            if v==[]:
                dico_final.pop(k)
         
         # l = liste de 0 de logueur identique à "chaine"       
        l=[0 for i in range(len(chaine))] 
        alpha=string.ascii_uppercase 
        # liste des caractères alphabetique majuscule ordonnée
        alpha=list(alpha)      
        for lettre in alpha:
            for i,v in enumerate(chaine):
                if v==lettre:
                    l[i]=dico_final[v][0][1]
                    dico_final[v].pop(0)
        # création de la liste de tuple finale
        liste_definitive=[]
        for a,b in zip(chaine,l):
            liste_definitive.append((a,b))
        return liste_definitive
        #return dico_final_copy,l,liste_definitive
        
            
                
    def crea_matrice_chiffrement(self, cle, phrase):
        """
        exemlpe :
        cle=verdun --> ('V','E','R','D','U','N')
        chiffre=(6,2,4,1,5,3)
        phase='ATTAQUE IMMINENTE' --> 'ATTAQUEIMMINENTE'
        donne en matrice
        
        V E R D U N
        6 2 4 1 5 3
        A T T A Q U
        E I M M I N
        E N T E
        
        donc une matrice 5x6 avec les deux dernières cases vides. On peut aussi
        voir cette matrice comme 5 listes de 6 caractères (le nb de caractères 
        étant fixé par la taille de la clé
        pour trouver la taille de la matrice : le nombre de colones est imposée 
        par la taille de la clé
        """
        # on commence par récupérer la liste de tuple de lettres de la cle
        # et dd la numérotation  de chacune des lettres
        cle=cle.upper()
        pos_lettre_cle=self.position_cara(cle)
        print(pos_lettre_cle)  
        taille_mat=self.taille_matrice(cle,phrase)
        print("taille mat = ",taille_mat)
        nb_lignes=taille_mat[0]
        nb_colonnes=taille_mat[1]
        espaces_vides=taille_mat[2]
        print(f"pour une clé égame à : {cle}")
        print(f"pour une phrase qui vaut : {phrase}")
        print(f"le nb de lignes de la matrices est :{nb_lignes}")
        print(f"le nb de colonnes de la matrices est :{nb_colonnes}")
        print(f"le nb d'espaces vides de la matrices est :{espaces_vides}")
        # on decoupe la chaine en élément de longueur nb_colonnes
        recup_position_carac=self.position_cara(cle)
        print("position caracteres",recup_position_carac)
        ligne_chiffres=[]
        
        for i in recup_position_carac:
            print(i)
            ligne_chiffres.append(str(i[1]))
        print("ligne_chiffre= ",ligne_chiffres)
        
        
        recup_chaine=self.n_carac(phrase, nb_colonnes)
        recup_chaine=recup_chaine.split()
        recup_chaine.insert(0,cle)
        for i,v in enumerate(recup_chaine):
            print("cocuocu     ",i,v)
            recup_chaine[i]=list(recup_chaine[i])
        recup_chaine.insert(1,ligne_chiffres)
        vide=taille_mat[2]
        print(vide) # vide donne le nombre de cases vides dans la matrice
        # on remplie les cases vides par la chione 'vide'
        temp=recup_chaine[taille_mat[0]-1]
        for i in range(vide):
            temp.insert(len(temp),'rien')
        print(temp)
        recup_chaine[taille_mat[0]-1]=temp
        mat_inter=copy.deepcopy(recup_chaine)      
        
        # On commence le chiffrement, on lit chacun des carctères dans l'ordre de numérotation des colonnes
        mat_inter.pop(0)
        mat_inter.pop(0)
        mat_chiffr=[]
        print("mat inter", mat_inter)
        chiffre_colonne=recup_chaine[1]
        for numero in range(1,taille_mat[1]+1):
            temp=[]
            print(type(str(numero)))
            # on recupere  index du numero
            indexe=chiffre_colonne.index(str(numero))
            print("indexe=   ",indexe)
            for j in mat_inter:
                if j[indexe] != 'rien':
                    temp.append(j[indexe])
            mat_chiffr.append(temp)
            chaine_chiffree=""
            for i in mat_chiffr:
                temp="".join(i)
                
                
            
            
            
            
            
        
        
         
        return recup_chaine,mat_chiffr
        
        # création de la matrice cle, chiffre, phase      
        

    def taille_matrice(self,cle,phrase):
        """
        cette fonction renvoie un tuple (l,c)
        où ligne est le nombre de lignes de la matrice de unchi
        et colonne est le nombre de colonnes de la matrice de ubchi
        enfin la variable vide répresente le nombre de cases vides de la matrice finale
        """
        phrase=phrase.upper()
        phrase=phrase.split()
        phrase="".join(phrase) # phrase en majuscule et sans espaces
        colonne=len(cle)
        ligne=0
        long_phrase=len(phrase)
        nb=colonne*2+long_phrase # nb éléments dans la matrice
        ligne=math.ceil(nb/colonne)
        total_mat=ligne*colonne
        vide = total_mat-(colonne*2+long_phrase)
        return ligne,colonne,vide
        
    def n_carac(self,chaine,n):
        """On cherche à représenter une chaine sans espace, en majuscule par 
        groupe de 5 caracteres
        exemple, 'coucou comment vas tu' donnera : COUCO UCOMM ENTVA STU
        """
        chaine_finale=""
        # on converti la chaine en liste
        chaine=chaine.upper()
        liste_chaine=chaine.split()
        liste_chaine="".join(liste_chaine)
        # on supprime les espaces
        print(liste_chaine)
        
        for indice,valeur in enumerate(liste_chaine):
            if indice%n==n-1: # on insere un espace dans la chaine finale
                chaine_finale+=valeur+" "
            elif indice%50==49:
                chaine_finale+="\n"
            else :
                chaine_finale+=valeur
        return chaine_finale

