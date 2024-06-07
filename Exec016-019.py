#Exec 016:

print('Números Inteiros de números fracionados!')

import math

num = float(input('Digite um número fracionado: '))
num1 = math.trunc(num)

print(f'O número inteiro de {num} é: {num1}')

#Exec 017:

import math

print('Calculadora de Hipotenusa!')

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hp = float((co**2) + (ca**2))
hp2 = math.sqrt(hp)

print(f'O resultado do cálculo da hipotenusa entre {co} e {ca} é: {math.trunc(hp2)}')

#Exec 018:

print('Seno, Cosseno e Tangente!')

import math

an = float(input('Digite o seu ângulo: '))
se = float(math.sin(math.radians(an)))
cs = float(math.cos(math.radians(an)))
tg = float(math.tan(math.radians(an)))

print(f'O seno desse ângulo é : {se:.2f}')
print(f'O cosseno desse ângulo é : {cs:.2f}')
print(f'A Tangente desse ângulo é : {tg:.2f}')

#Exec 019:

import random

print('Aluno sorteado!')

m = input('Primeiro Aluno: ')
l  = input('Segundo Aluno: ')
g = input('Terceiro aluno: ')
k = input('Quarto aluno: ')

lista = [m, l, g, k]

sort = random.choice(lista)

print(f'O aluno sorteado para apagar o quadro é: {sort}')


