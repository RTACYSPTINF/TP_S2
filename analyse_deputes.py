
import os
import numpy as np
import matplotlib.pyplot as plt


# on se place dans le répertoire où se trouve le fichier .csv des députés

os.chdir("H:\Doc_jspit\Travail-2010-2011\cours-TD-TP_JP\cours\Algo-RT1-Python\python_avance_S2\deputes")

print(os.getcwd())


with open("nosdeputes.fr_deputes_en_mandat_2018-06-11.csv","r",encoding='utf-8') as f:
    liste_deputes=f.readlines()
    
#print(type(a))

# on split chaque element de la liste
liste_deputes_nouvelle=[]
for i in liste_deputes:
    temp=i.split(';')
    liste_deputes_nouvelle.append(temp)

    
    
    
# liste des items de la première ligne
liste_items=[]
liste_items=liste_deputes[0].split(";")



    
# recherche parti politique "groupe_sigle"
# recherche de l'indice

indice_groupe_sigle=liste_deputes_nouvelle[0].index('groupe_sigle')
print(indice_groupe_sigle)
partis_politique=[]
for i in liste_deputes_nouvelle:
    partis_politique.append(i[indice_groupe_sigle])
partis_politique.pop(0)
    
# combien de partis politiques représentés à l'assemblée

Nb_partis=len(set(partis_politique))

# liste des partis politique
liste_partis=set(partis_politique)


# on cré un dictionnaire dico_partis dans lequel comme clé on trouve le parti et comme valeur le pourcentage du parti par ra^port à tous les partis
dico_partis={}
dico_partis_pour_cent={}
Nb_deputes=len(partis_politique)
for i in liste_partis:
    temp=partis_politique.count(i)
    dico_partis[i]=temp
    temp=temp/Nb_deputes
    dico_partis_pour_cent[i]=temp
    
    
s=0    
for i in dico_partis:
   s=s+dico_partis[i]
X=[]
Y=[]

for i in dico_partis:
    X.append(i)
    Y.append(dico_partis[i])
 

# diagramme camenbert
labels =X
sizes = Y


plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.title('Repartition des partis politique')
plt.savefig('PieChart01.png')
plt.show()


# pourcentage hommes femmes global
# recherche de l'index "sexe"
index_sexe=liste_items.index('sexe') 
femme=0
homme=0
liste_dep_temp=liste_deputes_nouvelle.pop(0)
for i in liste_deputes_nouvelle:
    if i[index_sexe]=='F':
        femme+=1
    else:
        homme+=1
        
# pourcentage homme femme total
homme_pourcent=homme/(femme+homme)
femme_pourcent=femme/(femme+homme)

# camenbert H/F

# diagramme camenbert
labels =['hommes', 'femmes']
sizes = [homme_pourcent,femme_pourcent]


plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.title('Repartition H/F global tous partis confondus')
plt.savefig('PieChart01.png')
plt.show()


# femmes hommes par parti politique
# dico_h_f_partis{'LREM':(Hlrem,Flrem)}
dico_h_f_partis={}

for i in liste_partis:
    print(i)
    F=0
    H=0
    for j in liste_deputes_nouvelle:
        if j[index_sexe]=='F' and j[indice_groupe_sigle]==i:
            F+=1
        elif j[index_sexe]=='H' and j[indice_groupe_sigle]==i :
            H+=1
    dico_h_f_partis[i]=(H,F)
    
# on trace le diagramme baton


N = len(liste_partis)
menMeans=[]
womenMeans=[]
for i in dico_h_f_partis:
    temp=dico_h_f_partis[i]
    menMeans.append(temp[0])
    womenMeans.append(temp[1])
menMeans=tuple(menMeans)
womenMeans=tuple(womenMeans)        
        
        
menMeans = (30,25,18,12,10,14,163,78)
womenMeans = (17,7,12,4,7,6,150,24)
menStd = (0)*8
womenStd = (0)*8
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Repartition H/F par partis politique')
plt.xticks(ind, ('MODEM', 'UAI', 'NG', 'GDR', 'LFI', 'NI', 'LREM', 'LR'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Homme', 'Femme'))

plt.show()
            
    




    
    
    











    






    
