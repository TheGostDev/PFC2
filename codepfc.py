import random

def pfc(nbRound):
    round = 0
    nbPoints = 0
    nbPointsRobot = 0
    idCoup = None
    print("Vous devez gagner avec la forme la plus forte ex: Pierre > Ciseau | Ciseau > Feuille | Feuille > Pierre")
    for i in range(nbRound):
        print("Round: ", round , " - Points: ", nbPoints)
        coup=input("Coup que vous voulez jouer:")
        if(coup == "Pierre"):
            idCoup = 0
        elif(coup == "Feuille"):
            idCoup = 1
        elif(coup == "Ciseaux"):
            idCoup == 2
        else:
            print("Le coup saisie n'existe pas")
        rdm = random.randint(0,2)
        if(idCoup == 0 and rdm == 0):
            print("Manche null")
            round = round + 1
        elif(idCoup == 0 and rdm == 1):
            print("Vous remportez cette manche")
            round = round + 1
            nbPoints = nbPoints + 1
        elif(idCoup == 0 and rdm == 2):
            print("Vous perdez cette manche")
            round = round + 1
            nbPointsRobot = nbPointsRobot + 1
        elif(idCoup == 1 and rdm == 0):
            print("Vous perdez cette manche")
            round = round + 1
            nbPointsRobot = nbPointsRobot + 1
        elif(idCoup == 1 and rdm == 1):
            print("Manche null")
            round = round + 1
        elif(idCoup == 1 and rdm == 2):
            print("Vous remportez cette manche")
            round = round + 1
            nbPoints = nbPoints + 1
        elif(idCoup == 2 and rdm == 0):
            print("Vous remportez cette manche")
            round = round + 1
            nbPoints = nbPoints + 1
        elif(idCoup == 2 and rdm == 1):
            print("Vous perdez cette manche")
            round = round + 1   
            nbPointsRobot = nbPointsRobot + 1
        elif(idCoup == 2 and rdm == 2):
            print("Manche null")
            round = round + 1
    if(nbPoints < nbPointsRobot):
        print("Nombre de round: ", nbRound, " - Vos points: ", nbPoints, " - Points robot: ", nbPointsRobot, " - Résultat: Vous avez perdu le pierre feuille ciseau")
    if(nbPoints > nbPointsRobot):
        print("Nombre de round: ", nbRound, " - Vos points: ", nbPoints, " - Points robot: ", nbPointsRobot, " - Résultat: Vous remportez le pierre feuille ciseau")
    if(nbPoints == nbPointsRobot):
        print("Nombre de round: ", nbRound, " - Vos points: ", nbPoints, " - Points robot: ", nbPointsRobot, " - Résultat: Egalité")

pfc(3)