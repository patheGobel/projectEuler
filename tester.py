from math import sqrt
def largestPalindrome3Digit(n):
    n = str(n)
    if n[0:2] == n[:-2]:
        print("palindrome")

largestPalindrome3Digit(899998)

"""
89 99 98
89 88 98
89 77 98
89 66 98
.. .. ..
89 00 98
87 99 78 
.. .. ..
87 00 78 
86 00 68
80 00 08
"""