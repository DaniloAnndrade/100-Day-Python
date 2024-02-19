import random

lista = ['bolo','maça','torta','mandioca','bolinho','mentos']
escolha = random.choice(lista)
quantidade = len(escolha)

print(quantidade)

# quantas lacunas
painel = []

for numero in range(quantidade):
    painel += '_'


 
#Chances

cod = []
ver = False

while not ver:
    print(painel)
    letra = input("Digite uma letra:").lower()

    for posicao in range(len(escolha)):
        local = escolha[posicao]
        if local == letra:
            painel[posicao]=local

    if '_' not in painel:
        ver =  True
        print("Você ganhou.")

    # soma de uma estrela
    if letra not in escolha:
        if cod.count('*') == 2:
            ver += True
            print("Perdeu")
        cod += '*'
        print(cod)