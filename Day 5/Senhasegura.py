import random

#Definer as variaveis

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
        

