import math
def mat(base, altura, covarde):
    b = (base * altura)/ covarde
    a = math.ceil(b)
    print(f"O tatal e de {a}, a base e  {base} a altura e {altura}.")



base = float(input("Qual a Largura da parde:"))
altura = float(input("Qual a Altura da parede:"))

covarde = 5

mat(base, altura, covarde)