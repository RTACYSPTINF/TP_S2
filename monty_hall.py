import random


# utiliser cette classe permet de rendre le programme plus lisible
class Strategie:
    def __init__(self):
        self.garder=1
        self.changer=2

def jeux_unique(strategie):
    """

    :param strategie:
    :return:
    """
    portes = [0,1,2]
    portes_temp=portes[:]
    porte_voiture=random.choice(portes)  # la voiture est fixée derrière cette porte
    premier_choix_joueur= random.choice(portes) # le joueur à fait son premier choix
    portes_temp.pop(premier_choix_joueur) # les portes dispo après le premier choix du joueur

    # le presentateur supprime une porte :
    if porte_voiture in portes_temp:
        portes_temp=[porte_voiture]
    else:
        a=random.choice(portes_temp)
        portes_temp=[a]

    # a partir de là, le joueur conserve son choix (premier_choix_joueur)
    # ou bien il change porte_temp
    portes_fin=[premier_choix_joueur, portes_temp[0]]
    if strategie == 2 :
        choix_final = portes_fin[1]
    else:
        choix_final = premier_choix_joueur

    if choix_final == porte_voiture :
        return 1
    else :
        return 0

strat=Strategie()


def monty_hall_simu1(strat, nb_emissions):
    """

    :param stategie:
    :param nb_emissions:
    :return:
    """
    # avec une comprehension de liste
    return [1 if jeux_unique(strat)==1 else 0 for i in range(nb_emissions)]


def monty_hall_simu2(strat, nb_emissions):
    """

    :param stategie:
    :param nb_emissions:
    :return:
    """
    liste_final=[]
    for i in range(nb_emissions):
        liste_final.append(jeux_unique(strat))
    return liste_final



def main():
    strat=Strategie()  # on crée une instance de la classe Strategie
    nb_emission=10000
    # strategie je ne change pas (je garde la porte de mon premier choix)
    premier_choix=monty_hall_simu1(strat.garder, nb_emission)
    # Strategie je change
    second_choix=monty_hall_simu1(strat.changer,nb_emission)
    print("#############################################################")
    print("#############################################################")
    print(f" en conservant mon premier choix  (Stratégie = garder), je gagne {sum(premier_choix)} sur un toltal de {nb_emission}")
    print("----****************************************************-----")
    print(f" en changeant mon premier choix  (Stratégie = changer), je gagne {sum(second_choix)} sur un toltal de {nb_emission}")
    print("#############################################################")
    print("#############################################################")
    print(f" en conservant mon premier choix  (Stratégie = garder), je gagne {sum(premier_choix)/nb_emission*100:.2f} %, sur un toltal de {nb_emission}")
    print("----****************************************************-----")
    print(f" en changeant mon premier choix  (Stratégie = changer), je gagne {sum(second_choix)/nb_emission*100:.2f} %, sur un toltal de {nb_emission}")


if __name__=="__main__":
    main()
