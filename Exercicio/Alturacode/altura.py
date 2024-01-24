
aluno = input("Digite as alturas:").split()

for n in range(0, len(aluno)):
    aluno[n] = int(aluno[n])

pes = 0

for lop in aluno:
    pes += lop 
print(f"Soma da altura {pes}")

cont = 0

for lop in aluno:
    cont += 1
print(f"Pessoas registradas {cont}")

media = 0

for lop in aluno:
    media =  pes / cont
print(f"Pessoas registradas {media}")
