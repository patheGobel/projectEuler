"""Largest Prime Factor
    Problem 3
    The prime factors of 13195 are 5,7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

"""
def largestPrimeFactorOfTheNumber(a):
 
        if a/isPremier(a)==0:
            return isPremier(a)

def isPremier(a):
    b=a
    while b>3 :
        b=b-1

m=600851475143    
n = int(m/2)
print(f"the largest prime factor of the{m} is {largestPrimeFactorOfTheNumber(n)}") """

def isPremier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def largestPrimeFactorOfTheNumber(a):

    x=int(a/2)

    while x>3:
        if isPremier(x):

            if a%x==0:
                return x
                break
        x-=1
        


n=600851475143 
print(f"the largest prime factor of the {n} is {largestPrimeFactorOfTheNumber(n)}")


    
