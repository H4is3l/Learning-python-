nome = input('Digite algo:')
print('O tipo primitivo é:', type(nome))
print('Só tem espaços:', nome.isspace())
print('é um número:', nome.isnumeric())
print('É alfabético:', nome.isalpha())
print('é alfanumérico:', nome.isalnum())
print('Está em maiúsculas:', nome.isupper())
print('Está em minúsculas:', nome.islower())
print('Está capitalizada:', nome.istitle())
