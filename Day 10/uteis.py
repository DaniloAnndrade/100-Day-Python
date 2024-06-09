import front

print('Calculadora')
num = 0
while True:

    if num == 0:
        num = int(input("Digite o primero numero:"))
    else:
        print(f'o Valor resultado{num}')

    while True:
        si = input("Digite um Sinal [ + / - * ]:")
        if si in '+-/*':
            break
        else:
            print('ERRO!Digite um dos sinais!')

    seg_num = int(input("Digite um numero:"))
    num = front.cal(num,si,seg_num)
    print(num)
    while True:
        cont = input('Deseja continuar? [S/N]').upper()
        if cont in 'SN':
                break
        else:
            print('Erro! Digite [S/N]')

    if cont == 'N':
        break