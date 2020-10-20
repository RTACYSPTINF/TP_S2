import datetime


# Récupère la date actuelle à partir de l'horloge système
date_courante = datetime.datetime.now()
annee = date_courante.year      # Extrait l'année actuelle de la date courante
mois = date_courante.month      # Extrait le mois de la date courante
jour = date_courante.day        # Extrait le jour de la date courante
heure = date_courante.hour      # Extrait l'heure de la date courante
minute = date_courante.minute   # Extrait les minutes


# Calcule le temps écoulé depuis le début de la séance de TP
heure_debut_TP = "18:30"    # <- à modifier en fonction de votre séance
try:
    pourcentage = ((heure*60 + minute) - (int(heure_debut_TP.split(":")[0])*60 + int(heure_debut_TP.split(":")[1]))) / 180*100
except:
    raise ValueError("L'heure de debut de TP doit respecté le format hh:mm")

# Affichage
print("Nous sommes aujourd'hui le", jour, mois, annee)
print("et il est", heure, minute)
print("Vous avez atteint", pourcentage, "pourcents des 3h de TP")

# Correction

# 2.1) Affichage simple
print("1> Suppression du retour chariot en fin de print")
print("Nous sommes aujourd'hui le", jour, "/", mois, "/", annee, end=" ")
print("et il est", heure, minute)

# 2.2) Concaténation de chaine
print("2> Retour chariot en fin de print remplacé par un espace")
chaine = "Nous sommes aujourd'hui le " + str(jour) + "/" + str(mois) + "/" + str(annee)
print(chaine, end=" ")
chaine = "et il est " + str(heure) + ":" + str(minute)
print(chaine)

# 2.3) Formatage de chaine avec transtypage
print("3> Formatage de chaîne avec transtypage")
chaine = "Nous sommes aujourd'hui le " + str(jour) + "/" + str(mois) + "/" + str(annee) + " " + \
    "et il est " + str(heure) + ":" + str(minute) + "\n" \
    "Vous avez atteint " + str(pourcentage) + " pourcents des 3h de TP"

print(chaine)

# 2.3) Formatage de chaine et gestion des nombres flottants
print("4> Formatage de chaine et gestion des nombres flottants")
chaine = "Nous sommes aujourd'hui le {}/{}/{} et il est {}:{}".format(jour, mois, annee, heure, minute) + "\n" + \
    "Vous avez atteint {:.2f}" .format(pourcentage) + " pourcents des 3h de TP"
print(chaine)