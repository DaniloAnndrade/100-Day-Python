import random;

lista = ['bolo','chocolate','biscoito']

es = random.choice(lista)

pessoa = input("Digite uma letra:").lower()

for var in es:
    if var == pessoa:
        print("Acerteu!")
    else:
        print("Errou!")