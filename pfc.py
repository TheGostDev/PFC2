#On admet une fonction random qui génère une nombre aléatoire entre 0 et 2

#On définit une fonction pfc(coup, nbRound)
    #On initialise nbRound à 0
    #On initialise une variable round à 0
    #On initialise nbPoints à 0
    #On initialise le nbPointsRobot à 0
    #On initialise la variable idCoup
    #Affichage des règles : "Vous devez gagner avec la forme la plus forte ex: Pierre > Ciseau | Ciseau > Feuille | Feuille > Pierre"
    #"Vous devez remporter la partie en " + nbPoints + "."
    #Pour i allant de 0 à nbRound
        #Alors afficher("Round: ", round, " - Points: ", nbPoints)
        #On assigne la variable coup avec la fonction input
        #On initialise les différents coups possibles :
        #Si le coup joué est "Pierre"
            #Alors idCoup vaut 0
        #Sinon si le coup joué est "Feuille"
            #Alors idCoup vaut 1
        #Sinon si le coup joué est "Ciseau"
            #Alors idCoup vaut 2
        #Sinon
            #Afficher que le coup saisie n'existe pas
        #appel de la fonction random pour faire joué un robot
        #Si idCoup vaut 0 et que random vaut 0
            #Alors, afficher "manche null"
            #On incrémente round de 1
        #Sinon si idCoup vaut 0 et que random vaut 1
            #Alors, afficher "Vous remportez cette manche"
            #On incrémente round de 1
            #On incrémente nbPoints de 1
        #Sinon si idCoup vaut 0 et que random vaut 2
            #Alors, afficher "Vous perdez cette manche"
            #On incrémente round de 1
            #On incrémente nbPointsRobot de 1
        #Sinon si idCoup vaut 1 et que random vaut 0
            #Alors, afficher "Vous perdez cette manche"
            #On incrémente round de 1
            #On incrémente nbPointsRobot de 1
        #Sinon si idCoup vaut 1 et que random vaut 1
            #Alors, afficher "Manche null"
            #On incrémente round de 1
        #Sinon si idCoup vaut 1 et que random vaut 2
            #Alors, afficher "Vous remportez cette manche"
            #On incrémente round de 1
            #On incrémente nbPoints de 1
        #Sinon si idCoup vaut 2 et que random vaut 0
            #Alors, afficher "Vous remportez cette manche"
            #On incrémente round de 1
            #On incrémente nbPoints de 1
        #Sinon si idCoup vaut 2 et que random vaut 1
            #Alors, afficher "Vous perdez cette manche"
            #On icnrémente round de 1
            #On incrémente nbPointsRobot de 1
        #Sinon si idCoup vaut 2 et que random vaut 2
            #Alors, afficher "Manche null"
            #On incrément round de 1
        #Si nbPoints inférieur à nbPointsRobot
            #Alors, afficher ("Nombre de round: ", nbRound, " - Vos points: ", nbPoints, " - Points robot: ", nbPointsRobot, " - Résultat: Vous avez perdu le pierre feuille ciseau")
        #Sinon si nbPoints supérieur à nbPointsRobot
            #Alors, afficher ("Nombre de round: ", nbRound, " - Vos points: ", nbPoints, " - Points robot: ", nbPointsRobot, " - Résultat: Vous remportez le pierre feuille ciseau")
        #Sinon si nbPoints == nbPointsRobot
            #Alors, afficher ("Nombre de round: ", nbRound, " - Vos points: ", nbPoints, " - Points robot: ", nbPointsRobot, " - Résultat: Egalité")