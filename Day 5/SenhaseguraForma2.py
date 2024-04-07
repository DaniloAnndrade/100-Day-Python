import random

letra_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numero_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
cara_1 = ["!", "@", "#", "$", "%", "&"]

letra = int(input("Letras:"))
numero = int(input("Numero:"))
cara = int(input("Caracteres:"))

senha= []
for letra_lop in range(letra):
    senha.append(random.choice(letra_1))

for numero_lop in range(numero):
    senha += random.choice(numero_1)   
for cara_lop in range(cara):
    senha += random.choice(cara_1)       

random.shuffle(senha)

senhas = ""
for senha_1 in senha:
    senhas += senha_1

print(senhas)