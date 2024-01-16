import random

escolha = ""

#O pc gera o numero random

pc = random.choice(['Pedra','Papel','Tesoura'])
print(pc)
#Usuario digita a sua opição
print('-='*15)
print('Jogo de Pedra Papel Tesoura!!!')
print('-='*15)
print("0 - Pedra\n1 - Papel\n2 - Tesoura")
print('-='*15)

op = int(input("Digite sua jogada:"))

#Logica de cada opção
if op == 0:
    print('\nEscolheu Pedra')
    escolha = "Pedra"
elif op == 1:
    print('\nEscolheu Papel')
    escolha = "Papel"
elif op == 2:
    print('\nEscolheu Tesoura')
    escolha = "Tesoura"
else:
    print('\nopção invalida')

print(f"\nA a sua escolha foi {escolha}")
print(f"A Maquina escolheu {pc}")

if escolha == pc :
    print("\nEmpatou")
elif escolha == "Pedra" and pc == "Tesoura" :
    print("\nVocê ganhou")
elif escolha == "Tesoura" and pc == "Pedra":
    print("\nVocê perdeu")
elif escolha == "Tesoura" and pc == "Papel":
    print("\nVocê ganhou")
elif escolha == "Papel" and pc == "Tesoura":
    print("\nVocê perdeu")
elif escolha == "Papel" and pc == "Pedra":
    print("\nVocê ganhou")
elif escolha == "Pedra" and pc == "Papel":
    print("\nVocê perdeu")



#Resultado