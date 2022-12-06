# Fonction qui calcul la factorielle d'un nombre donné
def factorielle(n):
    if(n > 0):
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
    return 1    
