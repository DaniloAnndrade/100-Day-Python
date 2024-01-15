import time
#Inicio

print('-='*20)
print('-=-=- Bem vindo ao jogo do Tesouro =-=-=')
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

