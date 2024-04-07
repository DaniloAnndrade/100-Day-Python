numero = int(input("Digite um numero:"))

soma = 0
for lop in range(0, numero+1,2):
    soma += lop
    print(f"os numeros são pares{lop}")

print(soma)