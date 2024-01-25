aluno = input("Nota Aluno:").split()
for n in range(0, len(aluno)):
    aluno[n] = int(aluno[n])


nota = 0

for score in aluno:
    if score > nota:
        nota = score

print(f"a nota maior foi {nota}")


