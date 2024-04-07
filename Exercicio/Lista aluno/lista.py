lista = {"Danilo":25,
         "Diva":63,
         "Andin":48}
listagrande = {}

for var in lista:
    print(var)
    print(lista[var])
    score = lista[var]
    if score >= 91:
        listagrande[var] = "Você e o cara"
        print("\nVocê e o cara")
    elif score > 81:
        listagrande[var] = "Parabens"
        print("\nParabens")
    elif score > 71:
        listagrande[var] = "Tome cuidado"
        print("\nTome cuidado")

    else:
        listagrande[var] = "Reprovado"
        print("Reprovado")
print(listagrande)