import random

tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print(tupla[0])

dig = int(input("O numero Digitado:"))
print(tupla[dig])


brasi = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás','Coritiba','América-MG')

print("Atividade 2\n")

for c in range(5):
    print(f"A colocação do time {brasi[c]} é {c+1}°")

print("Atividade 2 parte 2\n")

for a in range(16,20):
    print(f"A colocação do time {brasi[a]} é {a+1}°")

print("Atividade 2 parte 3\n")

alfabetica = sorted(brasi)

for b in alfabetica:
    print(b)

print("Atividade 2 parte 4\n")

for d in alfabetica:
    if d == "Bahia":
       print(f"A colocação do {alfabetica[c]} e {c}")

print("Atividade 3\n")

from random import randint

num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))


print(num)

print(f" \nO Maior numero e {max(num)}")

print(f"O Menor numero e {min(num)}")
       

print("Atividade 4\n")

bug = (0,0,0,0)

for ca in range(len(bug)):
       dg = int(input(f"Digite o numero {ca+1}:"))
       bug[ca] = dg
print(bug)