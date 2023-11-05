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


def largestPalindrome3Digit(nbr):
    ma_liste = [int(chiffre) for chiffre in str(nbr)]
    while ma_liste[0]!=0 and ma_liste[-1]!=0:
        for i in range(0,9):
            if not isPremier(nbr):
                decomperEnProduitDeFacteurPremier(nbr)
                #Je n'ai pas une idée de ce que cette partie ressemblera Mais je pense à une combinaison
                #Je pense que je dois décomposer et faire des combinaisons pour tester si le nombre est
                #produit de deux digits
                ma_liste[1]-=1
                ma_liste[-2]-=1
                if ma_liste[1]==0 and ma_liste[-2]==0:
                    ma_liste[1]=9
                    ma_liste[-2]=9
                    ma_liste[0]-=1
                    ma_liste[-1]-=1
m=9009
print(largestPalindrome3Digit(m))
