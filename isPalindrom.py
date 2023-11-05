def ispalindrom(ma_liste):
    # Utilisez le slicing pour extraire tous les éléments sauf les deux derniers
    nouveaux_elements = ma_liste[:-2]
    # Inversez les deux derniers éléments
    nouveaux_elements.extend(reversed(ma_liste[-2:]))
    # Réaffectez les éléments inversés à ma_liste
    ma_liste = nouveaux_elements
    if ma_liste[0:2] == ma_liste[-2:]:
        return True 