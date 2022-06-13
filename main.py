n_k = input()

def symbol_Newtona(lon):
    from math import factorial
    n = int(lon[0])
    k = int(lon[1])
    return int(factorial(n)/(factorial(k) * factorial(n-k)))

list_of_numbers = n_k.split(' ')

print(symbol_Newtona(list_of_numbers))
