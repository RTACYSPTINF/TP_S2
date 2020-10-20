from PIL import Image
import os
import operator


"""
Les chemins et fichiers suivants sont 
à adapter en fonction de chacun
"""
chemin=r'H:\Doc_jspit\Travail-2010-2011\cours-TD-TP_JP\cours\Algo-RT1-Python\python_avance_S2\steganographie\codage_image_steganographie'
os.chdir(chemin)
fichier='lena.png'
texte="La prise du batiment se fera demain à 16h avec toutes les équipes!!!"



im1=Image.open(fichier)
###########################################
##### Lecture d'une image
###########################################
def lire_image(chemin, image):
    os.chdir(chemin)
    im1=Image.open(image)
    im1.show()
    return im1

def filtre_gauche(N):
    """
    Prend le nombre N 0 <= N <= 255
    effectue un masque avec 1111 0000
    ce qui permet de ne conserver que les 4 bits de poids forts
    """
    masque=0b11110000
    return operator.and_(masque,N)

def ecrire_taille_texte(im,texte):
    """
    image est une image du style image=Image.open('fichier.png')
    im : est une image sur laquelle on va appliquer les changements
    im : résulte de Image.open('lena.png')
    texte : contient la chaine à cacher dans l'image
    """
    N=8 # nb de quartets réservés
    #taille=len(texte)
    # mise à zero des 8 premiers quartets rouges (R)
    im1=lire_image(chemin,fichier)
    im2=lire_image(chemin,fichier)

    ######### mise à zero des 8 premiers quartets R
    msq=0b11110000
    for i in range(N):
        r,g,b=im2.getpixel((i, 0))
        im2.putpixel((i,0), (operator.and_(r,msq),g,b))

    ######### écriture de la longeur de la chaine dans les 8 premiers quartets R
    # longueur de la chaine dans la variable long
    long=len(texte)
    #long=3561
    n_bits_long_chaine=len(bin(long))-2
    # n_R représente le nombre de R utiles pour écrire la taille du texte
    # exemple si n_bits_long_chaine vaut 15, il faut 3 4 4 4 donc 
    # R7 = xxxx 4 bits poids fort
    # R6 = xxxx 4 bits suivants
    # R5 = xxxx 4 bits suivants
    # R4 = xxxx x3 derniers bits
    nb_R = n_bits_long_chaine // 4 +1 # nb quartets utiles
    # on commence par le R7 et on redescend vers R0 si besoin
    for i in range(N-1,N-1-nb_R,-1):
        r,g,b=im2.getpixel((i,0))
        masque=operator.lshift(0b1111, 4*(N-1-i)) 
        nb=operator.and_(long,masque)
        nb=operator.rshift(nb,4*(N-1-i)) # on décale d'un multiple de 4 bits pour chaque valeur
        r=operator.or_(r,nb)
        im2.putpixel((i,0), (r,g,b))
    return im2

    

def recup_taille_texte(image):
    N=8
    masque=0b00001111
    taille=0 # nombre qui donne la taille du texte
    rec=[]
    for i in range(N):
        r,g,b=image.getpixel((i,0))
        rec.append(operator.and_(r,0b00001111))
    nb_final=0
    for i,v in enumerate(rec):
        nb_final+=operator.lshift(v,4*(N-1-i))
    return nb_final  # recupération de la valeur finale (taille du texte)
        
    
def ecrire_texte(image, texte):
    """
    Fonction qui permet d'écrire le texte dans les quartets R après le quartet N°7 (donc au 9ieme quartet)
    le 8 premiers qurtets sont réservés à la taille du texte
    """
    N=8
    texte="La prise du batiment se fera demain à 16h avec toutes les équipes!!!"
    liste_lettres=[]
    for i in texte:
        a0=operator.and_(ord(i), 0b1111) # bits de poids faible de la lettre
        a1=operator.rshift(operator.and_(ord(i), 0b11110000),4) # bits de poids forts de la lettre
        liste_lettres.append(a1)
        liste_lettres.append(a0)
    print(liste_lettres)
    print(len(liste_lettres))
    # ecrire les résultat dans les 4 bits de poids faible de cahque R de chaque pixel
    taille_liste_lettres=len(liste_lettres)
    print("liste lettre :",taille_liste_lettres)

    ############# Mise à zeros des quartets de poids faible de r
    cpt=0
    for y in range(1,512):
        for x in range(0,512):
            if cpt==taille_liste_lettres*2-1:
                break
            r,g,b=image.getpixel((x,y))
            r=operator.and_(r, 0b11110000)
            
            image.putpixel((x,y), (r, g, b))
            cpt+=1

#######################   ecriture dans les quartets de poids faibles de R des lettres du texte
    cpt=0
    for y in range(1,512):
        for x in range(0,512):
            #print(x,y)
            if cpt==taille_liste_lettres:
                break
            r,g,b=image.getpixel((x,y))
            r=operator.or_(liste_lettres[cpt], r)
            image.putpixel((x,y), (r, g, b))
            cpt+=1
    return image
            
def dechiffre_image(image):
    """
    Permet de récupérer le texte caché dans l'image
    Le texte est caché à partir de la ligne 2
    Il faut tout d'abord récupérer la taille du texte caché
            recup_taille_image(image)
    """
    taille=recup_taille_texte(image) #récupère la taille du texte sous forme d'entier décimal
    liste_recup=[]
    print("taille = :" ,taille)
    cpt=0
    for y in range(1,512):
        for x in range(0,512):
            #print(x,y)
            if cpt==taille*2:
                break
            r,g,b=image.getpixel((x,y))
            liste_recup.append(operator.and_(0b00001111, r))
            cpt+=1
    print(liste_recup)
    
    Lf=[]
    for i in range(0,len(liste_recup),2):
        print(i)
        temp=operator.lshift(liste_recup[i],4)+liste_recup[i+1]
        Lf.append(temp)
    print(Lf)
    Chaine=[]
    for i in Lf:
        Chaine.append(chr(i))
    return "".join(Chaine)








        


        
      
    


    
  
        


def main():
    im1=lire_image(chemin,fichier)
    im2=ecrire_taille_texte(im1,texte)
    print(recup_taille_texte(im2))
    im3=ecrire_texte(im2,texte)
    print(dechiffre_image(im3))
    






if __name__=="__main__":
    main()


