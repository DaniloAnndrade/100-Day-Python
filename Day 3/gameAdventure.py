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

#certo opção 2
if porta_ep1 == 1:
    print("Errou, perdeu o premio")
    print('Game over')
elif porta_ep1 == 2:
    print(f"Acertou, parabens{nome}")
    print('Proxima Etapa') 

#Se acerta continua para mais 3 opções
#certo opção azul. 
#Parabens, você ganhou um Balde de pipoca

else:
    print("Errou, perdeu o premio")
    print('Game over') 

