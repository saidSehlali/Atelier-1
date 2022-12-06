# Fonction qui renvoie la puissance d'un nombre X

def puissance(X,n):
    power = 1
    for i in range(n):
        power *= X
    return power
