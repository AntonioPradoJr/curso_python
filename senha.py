key_press = input('Pressione [E]ntrar [S]air: ')
pass_press = input('Digite a senha: ')
password = '12345'

if (key_press == 'E' or key_press == 'e') and pass_press == password:
    print('Entrou')
else:
    print('Sair')