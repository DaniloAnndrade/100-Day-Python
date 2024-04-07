import random

letra = int(input("Letras:"))
numero = int(input("Numero:"))
cara = int(input("Caracteres:"))

<<<<<<< HEAD
numero = random.choice(['0','1','2','3','4','5','6','7','8','9'])
carac = random.choice(['!','@','#','$','%','&','*','_','-'])

#Definir os inpuitus

dig_letra = int(input("Digite a quantidade de letra:"))
dig_num = int(input("Digite a quantidade de numero:"))
dig_car = int(input("Diigite a quantidade de caracteres:"))
#contadores
con_l = 0
con_n = 0
con_c = 0
#o loopi

for senha_l in range(dig_letra):
    #Definer as variaveis
    letra = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
        'x','y','z'])
    numero = random.choice(['0','1','2','3','4','5','6','7','8','9'])
    carac = random.choice(['!','@','#','$','%','&','*','_','-'])         

    print(letra)
    print(numero)
    print(carac)
        
=======
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
>>>>>>> 4f17c2a068ff369e8b4e75b269efcb7ffd5be380

senha = random.choice([letra_1,numero_1,cara_1])
print(senha)
  
