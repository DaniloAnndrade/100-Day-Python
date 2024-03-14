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

