#Exec 005:

n1=float(input('Um valor: '))

s = 1 + n1
e = n1 - 1

print(f'O antecessor de {n1} é {e}, e o sucessor é {s}')

#Exec 006:

n2 = float(input('Digite um número: '))

m = n2 * 2
m2 = n2 * 3
r = n2 ** (1/2)

print(f'O dobro do número citado é {m}, o triplo é {m2} e a raiz quadrada é {r}!')

#Exec 007:

n3 = float(input('Insira a nota do aluno(a): '))
n4 = float(input('Insira outra nota do aluno(a): '))

n = (n3 + n4)/2

print(f'A média desse aluno é: {n:.1f}!')

#Exec 008:

c = float(input('Digite a metragem: '))

c1 = c * 100
c2 = c1 * 10

print(f'A metragem em cm é {c1}, já os mm são: {c2}')

#Exec 009:

d = int(input('Digite um número inteiro: '))

d1 = int(1 * d)
d2 = int(2 * d)
d3 = int(3 * d)
d4 = int(4 * d)
d5 = int(5 * d)
d6 = int(6 * d)
d7 = int(7 * d)
d8 = int(8 * d)
d9 = int(9 * d)
d10 =  int(10 * d)

print(f'A tabuada completa desse número é: {d1, d2, d3, d4, d5, d6, d7, d8, d9, d10}')

#Exec 010:

do = float(input('Insira a quantidade de reais que deseja para sua compra de dólares: '))

rel = float(do/3.27)

print(f'A quantidade de dólares que você consegue com seu saldo atual é: {rel:.2f}')

#Exec 011:

print('quanto de litros de tinta é necessário pra pintar a parede?')

l = float(input('Qual a altura dessa parede?'))
t = float(input('Qual a largura dessa parede?'))

f = float(l * t/2)

print(f'A quantidade de litros necessários é: {f:.2f}')

#Exec 012:

print('Desconto de 5%')

g = float (input('Qual o preço do produto? '))
gd = float(input('Qual a porcentagem de desconto? '))

g1 = float(gd / 100)
g2 = float(g1 * g)
g3 = float(g - g2)

print (f'O desconto que você terá é: {g2:.2f}, reduzindo o preço original para: {g3:.2f} ')

#Exec 013:

print('Aumento salarial :)')

j = float(input('Qual o Salário atual: '))
j1 = float(input('Qual a porcentagem de aumento: '))

j2 = float(j1 / 100)
j3 = float(j2 * j)
j4 = float(j + j3)

print(f'O seu aumento salarial será de {j3:.2f}, resultando em um total de: {j4:.2f}')
