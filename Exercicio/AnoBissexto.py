# Digite o ano desejado
print("O ano é Bissexto?")
ano = int(input("Digite o ano:"))

# Ano é divisível por 4?
if ano % 4 == 0:
    # Ano é divisível por 100?
    if ano % 100 == 0:
        # Ano é divisível por 400?
        if ano % 400 == 0:
            print("Ano Bissexto!!", ano)
        else:print('Não é Bissexto')
    else:print('Ano Bissexto!!', ano)
else:print('Não é Bissexto')


