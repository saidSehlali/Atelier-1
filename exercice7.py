# La fonction qui trouver la fréquence d'un caractère dans une chaîne

def frequenceChar(str1, char):
    count = 0
    for i in str1:
        if(i == char):
            count += 1
    return count

