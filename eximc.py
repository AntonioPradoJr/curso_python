nome = 'Luiz'
altura = 1.80
peso = 95
imc = peso / (altura)**2

print(nome, 'tem', altura, "de altura",)
print('pesa', peso, 'quilos', 'e seu IMC é')
print(imc)

print('-----------------------------------------------------')

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)

print('-----------------------------------------------------')
string = '{} tem {:.2f} de altura pesa {} quilos e seu IMC é {:.2f}'
formato = string.format(nome, altura, peso, imc)

print(formato)

print('-----------------------------------------------------')
string = '{1} tem {0:.2f} de altura pesa {3} quilos e seu IMC é {2:.2f}'
formato = string.format(altura, nome, imc, peso)

print(formato)

print('-----------------------------------------------------')
string = '{nome} tem {altura:.2f} de altura pesa {peso} quilos e seu IMC é {imc:.2f}'
formato = string.format(
    altura = altura, 
    nome = nome, 
    imc = imc, 
    peso = peso)

print(formato)