primeiro_valor = input('Digite o Primeiro valor: ')
segundo_valor = input('Digite o Segundo Valor: ')

maior_string = f'{primeiro_valor} é maior que {segundo_valor}'
menor_string = f'{primeiro_valor} é menor que {segundo_valor}'


if primeiro_valor > segundo_valor:
    print(maior_string)
elif primeiro_valor < segundo_valor: 
    print(menor_string)
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais')



