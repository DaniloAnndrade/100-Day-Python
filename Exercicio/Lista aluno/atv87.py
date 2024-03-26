# exercício 87
    
lista3 = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
terceira = 0
linha2 = 0

for e in range(0,3):
    for f in range(0,3):
        nls = int(input(f"Digite um numero [{e}][{f}]:"))
        if nls % 2 == 0:
            soma+= nls
        lista3[e][f] = nls

for a in range(0,3):
    for b in range(0,3):
        print(f"[{lista3[a][b]}]", end="")
    print()

print(f"A soma dos numeros pares e {soma}.")

for a in range(0,3):
    terceira += lista3[a][2]
print(f"A soma dos terceritos numeros e {terceira}.")
    
for b in range(0,3):
    if b == 0:
        linha2 = lista3[1][b]
    elif lista3[1][b] > linha2:
        linha2= lista3[1][b]
print(f"O Maior numero da linha dois e {linha2}.")