"""
Largest Palindrome Product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math import sqrt
import isPremier
import isPalindrom
import decomperEnProduitDeFacteurPremier

def largestPalindrome3Digit(n):


    ma_liste = [int(chiffre) for chiffre in str(n)]
    
    if isPalindrom(ma_liste):
        print("palindrome")
        if not isPremier(n):
            decomperEnProduitDeFacteurPremier(n)
            #Je n'ai pas une idée de ce que cette partie ressemblera Mais je pense à une combinaison
        else:
            ma_liste =  ma_liste[2]-1
            ma_liste =  ma_liste[-3]-1
            #Incrémenter le nombre pour aller trouver le n-1 palindrom suivant 
            
        ma_liste =  ma_liste[2]-1
        ma_liste =  ma_liste[-3]-1
        if ma_liste[2]<0 or ma_liste[-3]<0:
            ma_liste =  ma_liste[1]-1
            ma_liste =  ma_liste[-2]-1

            ma_liste[1]=9
            ma_liste[-2]=9 

        #Incrémenter le nombre pour aller trouver le n-1 palindrom suivant

#m= 89 99 98
m=9009
print(largestPalindrome3Digit(m))
