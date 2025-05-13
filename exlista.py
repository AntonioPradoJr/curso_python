import os
lista_compras = []

while True:
    print('Selecione uma opcao: ')
    print('[i]nserir [a]pagar [l]istar [s]air: ')
    opcao_escolhida = input('> ').lower().strip()

    if opcao_escolhida == 'i':
        os.system('clear')
        item = input('Digite o Item a ser inserido:\n> ')
        if item: 
            lista_compras.append(item)
            print(f'---{item} foi inserido na lista de compras.---')
        else:
            print('Item vazio')

    elif opcao_escolhida == 'a':
        os.system('clear')
        try:
            indice = int(input('Selecione o indice do item a ser deletado:\n> '))
            item_removido = lista_compras.pop(indice)
            print(f'---{item_removido} foi removido da lista.')
        except ValueError:
            print('---Opcao Inexistente---')
        except IndexError: 
            print('---Item não identificado na lista--')

    elif opcao_escolhida == 'l':
        os.system('clear')
        if not lista_compras:
            print('---Lista Vazia---')
        else:
            print('---------------------Lista de Compras---------------------')
            for indice,valor in enumerate(lista_compras):
                print(f'{indice} - {valor}')

    elif opcao_escolhida == 's':
        os.system('clear')
        print('Saindo...')
        break
    else:
        print('---Opcao Invalida---') 