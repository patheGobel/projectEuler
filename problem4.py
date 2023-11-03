"""
Largest Palindrome Product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largestPalindrome3Digit(n):
    n = str(n)
    if n[0:2] == n[:-2]:
        print("palindrome")
        if isPremier():
           #Incrémenter le nombre pour aller trouver le n palindrom suivant 
        else:
            decompser(n)
    else : 
        print("not palindrome")

        
def decompser(n):
    listePremier = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941]
    i=0
    pgd=1
    while n%listePremier[i]==0:
        i+=1
        pgd= pgd*listePremier[i]
    return pgd

m= 899998
print(largestPalindrome3Digit(m))
