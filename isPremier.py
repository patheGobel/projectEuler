import math
import random
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