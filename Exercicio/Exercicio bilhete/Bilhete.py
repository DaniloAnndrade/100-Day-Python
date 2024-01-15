conta = 0

print("-="*15)
print('  Bem vindo a Montanha Russa')
print("-="*15)
print("\nPor segurança, abaixo de 1.20 de \naltura, não podera participar.\n")
altura = float(input("Qual é a sua altura:"))
if altura >= 1.20:
    print("-="*15)
    print('  Tabela de valores')
    print("-="*15)
    print('\nInfantil - R$ 5 (abaixo de 12)\nMeia     - R$ 7 (abaixo de 12)\nAdulto   - R$ 12 (abaixo de 12)\n')
    bilhe = int(input("Digite a sua idade:"))
    if bilhe <= 12 :
        conta = 5
        print('Bilhete Infantil')
    elif bilhe <=18:
        conta = 7
        print('Bilhete Meia')

    elif bilhe >= 45 and bilhe <=55:
        conta = 0
        print("Entrada Franca")
    else:
        conta = 12
        print('Bilhete Adulto')

    print("Foto do Momento R$ 3")
    foto = str(input("Vai querer uma foto do momento? S ou N :"))
    if foto == 's' or foto == 'S':
        conta += 3
    print(f"\nO total e: R${conta}")
    


else:
    print('Por Segurança, voce não atenda a altura desejada')