nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
length = len(nome)

if nome.strip() and idade.strip():
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if " " in nome:
        print(f'O nome {nome} contém espaços')
    else:
        print(f'O nome {nome} não contém espaços')
    
    print(f'O nome {nome} contém {length} letras')
    print(f'A primeira letra do nome {nome} é: {nome[0]}')
    print(f'A última letra do nome {nome} é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')