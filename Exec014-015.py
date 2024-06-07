#Exec 014:

print('Conversor de Temperaturas')

c = float(input('Quantos graus em °C: '))

f = float(c * 1.8 + 32)

print(f'A temperatura convertida em °F é: {f:.2f}')

#Exec 015:

print('Aluguel de Carro!')

d = float(input('Quantos dias você andou com o carro: '))
k = float(input('Quantos KM você percorreu: '))

c1 = float(d * 60) + (k * 0.15)

print(f'A quantidade necessária para o pagamento é: R$ {c1:.2f}')
