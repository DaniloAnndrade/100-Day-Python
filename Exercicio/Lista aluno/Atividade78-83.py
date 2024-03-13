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

lista4 = []
wh2 = False

while not wh2:
    i = int(input("Digite um numero:"))
    lista4.append(i)
    j = input("Deseja continuar:[S/N]").upper()
    if j == 'N':
        wh2 = True

if 5 in lista4:
    print("Essa lista, foi digitado o numero 5!")
else:
    print("Esta lista, Não teve o digito 5!")

lista4.sort(reverse=True)
print(lista4) 


# exercício 82

lista5 = []
k = lista5[:]
l = lista5[:]
wh3 = False

while not wh3:
    m = int(input("Digite um numero:"))
    lista5.append(m)
    if m % 2 == 0:
        k.append(m)
    if m % 2 == 1:
        l.append(m)
    n = input("Gostaria de continuar:[S/N]").upper()
    if n == 'N':
        wh3 = True

print(f"\nA lista teve esses numeros{lista5}")
print(f"Foram {k} de numeros pares.")
print(f"Foram {l} de numeros impares.")

    
