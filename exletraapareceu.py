frase = 'Teste de contagem de letras'

i = 0

while i < len(frase):
    letra_atual = frase[i]
    print(letra_atual, frase.count(letra_atual))
    i += 1