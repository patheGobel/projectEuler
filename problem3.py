"""Largest Prime Factor
    Problem 3
    The prime factors of 13195 are 5,7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

import random
import math

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

def largestPrimeFactorOfTheNumber(a):

  x=math.sqrt(a)
  x=int(x)
  while (x>3):
    if (x-1)%6==0 or (x+1)%6 == 0:
      if ((x)%2!=0) and (x%5!=0):
        if a%(x)==0:
          if isPremier(x):
            return x
            break
    x-=1

#600851475143
n=600851475143
print(f"the largest prime factor of the {n} is {largestPrimeFactorOfTheNumber(n)}")