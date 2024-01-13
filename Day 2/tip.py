#Boas Vindas.
print("-=-"*10)
print('Seja, bem vindo')
print("-=-"*10)
#O valor da Conta.
total = float(input('Digite o valor total da conta:\nR$'))
#Quanto de Gorjeta
gorjeta = float(input("Digite a porcentagem gorjeta(10 , 12 ou 15):"))
#Dividir em quantas pessoas.
pessoa = int(input("Quantas pessoas: "))
#O que cada pessoas vai pagar.
gorjeta_tl = (total*gorjeta)/100
print("são R${} de gorjeta!".format(gorjeta_tl))
valor_soma = (gorjeta_tl + total)
print("A conta ficou no valor de R${:.2f} dividido em {} pessoas, fica R${:.2f} para cada cliente".format(valor_soma, pessoa, valor_soma / pessoa))