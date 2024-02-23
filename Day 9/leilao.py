
ganhador = []

prod = input("\nDigite o nome produto:")
ini = float(input("Valor inicial do produto:"))
quan = int(input("Quantidade de gente:"))

maior = ini

fim = False
cont = 0
while not fim:
    nome = input("\nDigite seu nome:").upper()
    lance = float(input("Digite seu lançe:"))
    if lance > maior:
        ganhador = nome
        maior = lance
    cont += 1
    if cont == quan:
        print(f"\nO ganhador e  {ganhador} Adiquiriu um {prod} o lance foi de {maior}")
        fim = True