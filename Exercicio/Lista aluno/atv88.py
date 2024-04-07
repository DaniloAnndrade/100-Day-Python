from random import randint
from time import sleep

lista = list()
jogo = list()
wh = False
quant = int(input("Digite a quantidade de sequencia numeros sorteados:"))
cont = 1


for  a in range(quant):
    while not wh:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            wh = True
    cont = 0
    wh = False
    lista.sort()
    jogo.append(lista[:])
    lista.clear()

for b in range(quant):
    print(f"A Sequencia {b+1}° e de {jogo[b]}")
    sleep(2)


