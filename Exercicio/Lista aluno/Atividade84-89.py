# exercício 84

dado = []
pepe = []
totalmaior = totamenor = 0
wh = False

while not wh:
    pepe.append(str(input("Nome:")))
    pepe.append(int(input("Peso:")))
    if len(dado) == 0 :
        totalmaior = totamenor = pepe[1]
    else:
        if pepe[1] > totalmaior:
            totalmaior = pepe[1]
        if pepe[1] < totamenor:
            totamenor = pepe[1]

    dado.append(pepe[:])
    pepe.clear()    
    a = str(input("Continuar:[S/N]")).upper()
    if a == 'N':
        wh = True


print(f"Pessoas cadastradas:{len(dado)}")  
print(f"O maior peso foi {totalmaior},", end="")
for b in dado:
    if b[1] == totalmaior:
        print(f"de {b[0]}..", end="")
print(f"\nO menor peso foi {totamenor},", end="")
for c in dado:
    if c[1] == totamenor:
        print(f"de {c[0]}..", end="")

# exercício 85
        
lista = [[],[]]

wh2 = False

while not wh2:
    pos = int(input("\n\nDigite um numero:"))
    if pos % 2 == 0:
        lista[0].append(pos)
    elif pos % 2 == 1:
        lista[1].append(pos)
    cont = str(input("Gostaria de continuar:[S/N]")).upper()
    if cont == 'N':
        wh2 = True
    elif cont != 'S':
        print("Digito errado!!!")
    
lista[0].sort()
lista[1].sort()
print(f"Os numeros Pares foram {lista[0]}.")
print(f"Os numeros impares foram{lista[1]}.")

# exercício 86

lista2 = [[0,0,0],[0,0,0],[0,0,0]]

for a in range(0,3):
    for b in range(0,3):
        num = int(input(f"\n\nDigite um numero[{a}][{b}]:"))
        lista2[a][b] = num
for c in range(0,3):
    for d in range(0,3):
        print(f"[{lista2[c][d]:^5}]", end= "")
    print()


