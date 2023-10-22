"""
Even Fibonacci Numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2 , the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
def evenFibonacciNumbers(n)->list:

    liste = []

    for i in range(n):
        if i < 2:
            liste.append(i + 1)
        else:
            liste.append(liste[i - 1] + liste[i - 2])
    print(f"Voici la liste des nombres de fibinacci:\n{liste}")
    return [x for x in liste if x%2==0]

n =int(input("Donner le nombre de la suite fibo que tu souhaite afficher\n"))
print(f"Voici la liste des nombre de fibinacci pairs:\n{evenFibonacciNumbers(n)}")
print(f"Voici la somme des nombre de fibinacci pairs:\n{sum(evenFibonacciNumbers(n))}")