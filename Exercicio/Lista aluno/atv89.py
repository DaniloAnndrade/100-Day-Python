lista = list()
cont = 0
wh = False

while not wh:
    nome = str(input("Nome:"))
    n1 = float(input("1° Nota:"))
    n2 = float(input("2° Nota:"))
    med = (n1 + n2) / 2
    lista.append([nome, [n1,n2],med])
    op = str(input("Deseja continuar? [S/N]:")).upper()
    cont += 1
    if op == "N":
        wh = True 

print(f"\n{'Numero':<10}{'Nome':<5}{'Medio':>16}\n")
for i,a in enumerate(lista):
    
    print(f"{i+1:<7} {a[0]:<12} {a[2]:>8.1f}")

while True:
    ops= int(input("Mostrar as notas do aluno : [999 cancelar]"))
    if ops == 999:
        print("Serviço Finalizado")
        break
    if ops <= len(lista)-1:
        print(f"Nota de {lista[ops][0]} são {lista[ops][1]}")

print("<<Volte sempre")