# exercício 78
valor = []
maior = 0
menor = 0
for doc in range(0,5):
    valor.append(int(input("Digite um Valolr:")))
    if doc == 0:
        maior = menor = valor[doc]
    else:
        if valor[doc] > maior:
            maior =valor[doc]
        if valor[doc] < menor:
            menor = valor[doc]

print(valor)
print(f"\nO Menor valor foi {menor} na posições ",end="")
for a,b in enumerate(valor):
    if b == menor:
        print(f"{a}....",end="")

print(f"\nO Maior valor foi {maior} na posições " ,end="")
for c,d in enumerate(valor):
    if d == maior:
        print(f"{c}....", end="")

# exercício 79
        
print("\n\nExercicio 79")
  
lis2 = []
wh = False
while not (wh):
    e = int(input("Digite um numero:"))
    if e not in lis2:
        lis2.append(e)
        print("Valor, adicionado!!")
    else:
        print("Valor, ja Existente!!")
    esco = input("Gostaria de continuar?[S/N]").upper()
    if esco == 'N':
        wh = True
lis2.sort()
print(lis2)

# exercício 80

lista3 = []


for g in range(0,5):
    h = int(input(f"Digite o {g+1}° numero:"))
    if g == 0 or  h > lista3[-1]:
        lista3.append(h)
    else:
        pos = 0
        while pos < len(lista3):
            if h <= lista3[pos]:
                lista3.insert(pos,h)
                break
            pos += 1

print(lista3)

# exercício 81