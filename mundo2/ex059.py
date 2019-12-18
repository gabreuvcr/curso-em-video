## EX059 ##

opcao = 4
while opcao != 5:
    if opcao == 4:
        print('')
        n1 = int(input('Digite o 1º numero: '))
        n2 = int(input('Digite o 2º numero: '))
    print('''\n[1] Soma
[2] Multiplicar
[3] Maior
[4] Novos digitos
[5] Sair do programa''')
    opcao = int(input('>>> Digite uma opção: '))
    if opcao == 1:
        print('\nA soma é: {}'.format(n1 + n2))
    elif opcao == 2:
        print('\nA multiplicação é: {}'.format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('\nO maior é o {}. ({} > {}) '.format(n1, n1, n2))
        elif n1 < n2:
            print('\nO maior é o {}. ({} > {})'.format(n2, n2, n1))
        else:
            print('\nAmbos são iguais. ({} = {})'.format(n1, n2))
    elif 0 < opcao > 5:
        print('\nValor invalido. Digite novamente.')
    if opcao < 4:
        ok = input('Digite qualquer tecla para continuar...')
