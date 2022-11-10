def morpionBase(x):
    x = 0 #Initialisation len tab
    i = 0 #Initialisation variable de boucle
    tabX = [] #Initialisation tableau x
    tabF = [] #Initialisation du tableau final
    while i < x: #Fonction tant que i < x
        #Alors, on ajoute 1 valeur de x à tab et on incrémente i de 1
        tabX = tabX.append(i)
        
        i = i + 1
    tabF = tabX
    return tabF

print(morpionBase(10))