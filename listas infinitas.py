import random

soma = 0

while soma >= 0:

    numeros = []

    for i in range(5):
        ins = random.randint(1,10)
        numeros.append(ins)

    soma = sum(numeros)

    numeros_inv = list(reversed(numeros))
    
    print(numeros)
    print(max(numeros))
    print(min(numeros))
    print(soma)
    print(numeros_inv)

    
    if soma >= 50:
        break
