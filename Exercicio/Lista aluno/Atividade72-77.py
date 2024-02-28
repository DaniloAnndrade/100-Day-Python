import random

print("Atividade 72\n")

tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print(tupla[0])

dig = int(input("O numero Digitado:"))
print(tupla[dig])


brasi = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás','Coritiba','América-MG')

print("Atividade 73\n")

for c in range(5):
    print(f"A colocação do time {brasi[c]} é {c+1}°")

print("Atividade 73 parte 2\n")

for a in range(16,20):
    print(f"A colocação do time {brasi[a]} é {a+1}°")

print("Atividade 73 parte 3\n")

alfabetica = sorted(brasi)

for b in alfabetica:
    print(b)

print("Atividade 73 parte 4\n")

for d in alfabetica:
    if d == "Bahia":
       print(f"A colocação do {alfabetica[c]} e {c}")

print("Atividade 74\n")

from random import randint

num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))


print(num)

print(f" \nO Maior numero e {max(num)}")

print(f"O Menor numero e {min(num)}")
       

print("Atividade 75\n")

bug = (int(input(f"Digite o numero :")),
       int(input(f"Digite o numero :")),
       int(input(f"Digite o numero :")),
       int(input(f"Digite o numero :")))
num9 = 0

print(bug)

for cb in range(len(bug)):
    if bug[cb] == 9:
        num9 += 1

    elif bug[cb] == 3:
        print(f"o numero 3 Esta na poeção °{cb+1}")

    elif bug[cb] % 2 == 0:
        print(f"O numero {bug[cb]} e par")

print(f"Foram {num9} numeros 9")

print("Atividade 76\n")

com = ("Lápis",1.75,
       "Borracha",2.0,
       "Caderno",15.90,
       "Estojo",25.00)

for crob in range(0, len(com)):
    if crob % 2 == 0:
        print(f'{com[crob]:.<30}', end="")
    if crob % 2 == 1:
        print(f'R${com[crob]:>7}')


print("Atividade 77\n")

bags = ("Pato","Cachorro","Cavalo","Gato","Periquito")

for pet in bags:
    print(f"Na palavra {pet}", end="")
    for letras in pet:
        if letras in 'aeiou':
            print(letras, end=" ",)

