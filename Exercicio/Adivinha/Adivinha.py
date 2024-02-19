import random;

lista = ['bolo','chocolate','biscoito']

es = random.choice(lista)

display = []
for cont in range(len(es)):
    display += '_'
print(display)

pessoa = input("\nDigite uma letra:").lower()

for posi in range(len(es)):
    var = es[posi]
    if var == pessoa:
        display[posi] =  var
    
print(display)


