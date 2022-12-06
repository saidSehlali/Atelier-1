# Fonction qui calcul la factorielle d'un nombre donné
def factorielle(n):
    if(n < 0):
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
    return 1

# Fonction pour trouver la somme des series 1!/1 + 2!/2 + 3!/3 + 4!/4 + 5!/5

def sommeSerie(n):
    if(n <= 0):
        return "Le nombre doit être strectement positif"
    else:
        sum = 0
        for i in range(1,n+1):
            sum += factorielle(i-1)
        return sum
