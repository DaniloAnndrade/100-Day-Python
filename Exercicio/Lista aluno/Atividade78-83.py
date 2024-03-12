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
        
# exercício 78