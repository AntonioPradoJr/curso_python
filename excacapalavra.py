secreta = 'palavra'

palavra_adivinhada = ""
contagem = 0

while palavra_adivinhada != secreta:
    letra_digitada = input('Digite uma letra: ')
    for letra in secreta:
        if letra_digitada in letra:
            palavra_adivinhada += letra
        else:
            palavra_adivinhada += '*'
        continue
    print(palavra_adivinhada)
    


        

