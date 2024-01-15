import time
#Inicio

print('-='*20)
print('-=-=- Bem vindo ao jogo do Tesouro =-=-=')
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print('-='*20)


#Digite seu nome

nome = str(input("\nPor favor, Digite seu nome:"))

#Escolha uma das 3 opções
time.sleep(2)
print(f'\nBem vindo, {nome}, nesse jogo você pode\nganha um grande premio')
print('\nEscreva o numero de uma das opções:\n 1 - Porta do Biscoito\n 2 - Porta do docé de coco\n 3 - Porta da Balinha\n ')
print('-='*20)
time.sleep(2)
porta_ep1 = int(input("Digite o numero da porta:"))

time.sleep(2)
#certo opção 2
if porta_ep1 == 1:
    print("\nA Resposta esta!!!")
    time.sleep(2)
    print("Errada, perdeu o premio")
    print('Game over')
elif porta_ep1 == 2:
    print("\nA Resposta esta!!!")
    time.sleep(2)
    print(f"certa, parabens {nome}!!")
    print('Proxima Etapa') 
    time.sleep(2)

#Se acerta continua para mais 3 opções.
    
    print(f'\nAgora, {nome}, Escolha a cor Certa e \nganhe o Grande premio')
    print('\nEscreva o nome da Cor:\n Azul \n Verde \n Amarelo\n ')
    print('-='*20)

    porta_ep2 = str(input("Digite o nome da cor escolhida:"))

#certo opção azul. 
    
    if porta_ep2 == "azul":
        print("\nA Resposta esta!!!")
        time.sleep(2)
        print(f"certa, Parabens {nome}!!")
#Parabens, você ganhou um Balde de pipoca.
        print("Você acaba de ganhar, um!!!")
        time.sleep(2)
        print("POTE DE PIPOCA, !!!!!!!")
        time.sleep(1)
        print("Aproveite")      

    elif porta_ep2 == "verde":
        print("\nA Resposta esta!!!")
        time.sleep(2)
        print("Errada, perdeu o premio")
        print('Game over') 
    else:
        print("\nA Resposta esta!!!")
        time.sleep(2)
        print("Errada, perdeu o premio")
        print('Game over') 

else:
    print("\nA Resposta esta!!!")
    time.sleep(2)
    print("Errada, perdeu o premio")
    print('Game over') 

