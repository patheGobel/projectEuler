"""Largest Prime Factor
    Problem 3
    The prime factors of 13195 are 5,7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

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
  while (x>3):
    if (x-1)%6==0 or (x+1)%6 == 0:
      if ((x)%2!=0) and (x%5!=0):
        if isPremier(x):
          if a%(x)==0:
            return x
            break
          #print(f"{x} est un un nombre premier qui divise {a}")
    x-=1

#600851475143
n=600851475143
print(f"the largest prime factor of the {n} is {largestPrimeFactorOfTheNumber(n)}")