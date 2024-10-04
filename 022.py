#Exec022:

nome = input('Digite seu nome completo: ')
nome1 = input('Digite seu primeiro nome: ')

s = str(len(nome.split( )))

print(nome.upper())
print(nome.lower())
print(s.strip())
print(len(nome1.strip( )))

#Exec023:

num = input('Digite um número inteiro qualquer: ')

k = len(num)

unidades = []
dezenas = []
centenas = []
milhares = []

unidades = num[-1]

if k > 1:
    dezenas = num[-2]
if k > 2:
    centenas = num[-3]
if k > 3:
    milhares = num[-4]

print(f'Unidades: {unidades}')
print(f'Dezenas: {dezenas}')
print(f'Centenas: {centenas}')
print(f'Milhares: {milhares}')

#Exec024:

frase = input('Digite o nome da sua cidade: ')

palavras = ['santo','Santo','Santos','santos','Santa','santa']

procura = False

for palavra in palavras:

     if frase.find(palavra)!= -1:
        procura = True
        break
     
if procura:
    print('Possui Santo(s) no nome!')

else:
    print('Não possui Santo(s) no nome!')
