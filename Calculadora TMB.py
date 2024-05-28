print('Calculadora de TMB')

s = input('Você é Homem ou Mulher?')

p = float (input('Qual seu Peso? '))
a = float (input('Qual sua Altura(em CM)? '))
i = float (input('Qual sua Idade? '))

c = float(66 + (13.7 * p) + (5 * a) - (6.8 * i))

c2 = float(665 + (9.6 * p) + (1.8 * a) - (4.7 * i))

if 'Homem' or 'homem':
    print(f'Seu gasto calórico(KCAL) diário é: {c}')
else:
    print(f'Seu gasto calórico(KCAL) diário é: {c2}')
