print('-='*15)
print('     Bem vindo, aos pizzas')
print('-='*15)

print('\nTabela de Preço\nP - Pequena R$ 15\nM - Media   R$ 20\nG - Grande  R$ 25\n')

tam = str(input("Tamanho escolhido é:"))

con = 0
pp = ""
pp_extra = ""
che = ""

if tam == "p" or tam == "P":
    con = 15
    print()
elif tam == "m" or tam == "M":
    con = 20
    print()
elif tam == "g" or tam == "G:":
    con = 25
    print()
else:
    print("Escolha incorreta")

print('\nTabela Adicionais\nPeperone       R$ 2\nPeperoni Extra R$ 3\nQueijo cheese  R$ 1\n')

pepero = str(input('Deseja Peperoni (S ou N):'))
if pepero == "s" or pepero == "S":
    pp = "+ Peperone"
    con += 2

pepero_extra =str(input("Deseja peperoni Extra (S ou N):"))
if pepero_extra == "s" or pepero_extra == "S":
    pp_extra = " + Peperone Extra"
    con += 3
cheese = str(input("Deseja queijo cheese (S ou N):"))
if cheese == "s" or cheese == "S":
    che = "+ Quejo cheese"
    con +=1

print(f"\nPedido Realizado com Sucesso\no seu pedido ficou no total de\nR% {con} {pp} {pp_extra} {che}")
