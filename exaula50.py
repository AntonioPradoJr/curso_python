num_user = input('Digite um número: ')
check_inteiro = num_user.isdigit()


if check_inteiro:
    check_resto = int(num_user)%2
    check_par = check_resto == 0
    if check_par:
        print('par')
    else:
        print('impar')
else: 
    print('Não digitou um Número Inteiro')



