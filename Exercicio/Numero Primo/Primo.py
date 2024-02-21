def primo(numero):
    print(f"o numero {numero},....")
    enq = True
    for i in range(2 , numero):

        if numero % i == 0:
            enq = False
            
        if enq:
            print("E um numero primo")
        else:
            print("Não e primo")


numero = int(input("Digite um numero:"))

primo(numero)