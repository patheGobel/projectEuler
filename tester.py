
def largestPalindrome3Digit(n):
    ma_liste = [int(chiffre) for chiffre in str(n)]
    if palindrome(ma_liste):
        print("palindrome")

def palindrome(ma_liste):
  # Utilisez le slicing pour extraire tous les éléments sauf les deux derniers
  nouveaux_elements = ma_liste[:-2]

  # Inversez les deux derniers éléments
  nouveaux_elements.extend(reversed(ma_liste[-2:]))

  # Réaffectez les éléments inversés à ma_liste
  ma_liste = nouveaux_elements
  if ma_liste[0:2] == ma_liste[-2:]:
    return True  

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