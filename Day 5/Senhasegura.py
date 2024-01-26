import random

letra = int(input("Letras:"))
numero = int(input("Numero:"))
cara = int(input("Caracteres:"))

for letra_lop in range(letra):
    letra_1 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
)
    print(letra_1, end="")
for numero_lop in range(numero):
    numero_1 = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print(numero_1,end="")
for cara_lop in range(cara):
    cara_1 = random.choice(["!", "@", "#", "$", "%", "&"])
    print(cara_1,end="")

senha = random.choice([letra_1,numero_1,cara_1])
print(senha)
  
