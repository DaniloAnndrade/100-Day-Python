import random

moeda = random.choice(['cara','coroa'])
user = str(input("Cara ou Coroa:")) 

print(moeda)
if moeda == user:
    print('Ganhou')
else:
    print('Perdeu')
