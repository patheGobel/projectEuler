"""Multiples of 5 or 3 
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or below 1000
"""
liste1 = [3 * x for x in range(1, 10) if 3 * x < 10]
sum1 = sum(liste1)

liste2 = [5 * x for x in range(1, 10) if 5 * x < 10]
sum2 = sum(liste2)

print(sum1+sum2)
