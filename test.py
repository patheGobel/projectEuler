from math import sqrt
def decompser(n):
    
    listePremier = [2,3,5,7,11,13,17,19]
    i=0

    listDesDiviseur = []
    quotient = n
    while i<len(listePremier):
        if quotient%listePremier[i]==0:
            while True:
                quotient = quotient//listePremier[i]
                listDesDiviseur.append(listePremier[i])
                if quotient%listePremier[i]!=0:
                    break
        i+=1
        if listePremier[i]>sqrt(n):
            break
    return listDesDiviseur

print(decompser(30))