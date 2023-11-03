"""
Largest Palindrome Product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math import sqrt
import random
import math

def largestPalindrome3Digit(n):
    ma_liste = [int(chiffre) for chiffre in str(n)]
    if palindrome(ma_liste):
        print("palindrome")
        if isPremier(n):
           #Incrémenter le nombre pour aller trouver le n palindrom suivant
        else:
            decompser(n)
    else : 
        print("not palindrome")


def palindrome(ma_liste):
    # Utilisez le slicing pour extraire tous les éléments sauf les deux derniers
    nouveaux_elements = ma_liste[:-2]
    # Inversez les deux derniers éléments
    nouveaux_elements.extend(reversed(ma_liste[-2:]))
    # Réaffectez les éléments inversés à ma_liste
    ma_liste = nouveaux_elements
    if ma_liste[0:2] == ma_liste[-2:]:
        return True  


def isPremier(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Étape 1 : Écriture de n-1 comme 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Étape 2 : Effectuer le test de Miller-Rabin k fois
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

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

#m= 89 99 98
m=9009
print(largestPalindrome3Digit(m))
