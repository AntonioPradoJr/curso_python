nome = input('Digite seu nome: ')
count = 0
nome_novo = ''
while count < len(nome):
    letra = nome[count]
    nome_novo += f'{letra}*'
    count += 1

print(nome_novo)

