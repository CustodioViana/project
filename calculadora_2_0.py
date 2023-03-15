print('Calculadora com while')
linha = 80 * '-'

while True:
    try:
        valor_1 = float(input('Por favor, digite o primeiro número: '))
        valor_2 = float(input('Por favor, digite o segundo número: '))
        if valor_1 + valor_2 == 0.0:
            print('Ambos os números são 0(zero), favor digitar números válidos.')
            print(linha)
            continue
        operador = input(f'Escolha a operação que deseja realizar:\n'
                    f'[1]Adição\n'
                    f'[2]Subtração\n'
                    f'[3]Divisão\n'
                    f'[4]Multiplicação\n'
                    f'[5]Potencialização\n'
                    f'[6]Sair: ')
        print(linha)
        adicao = valor_1 + valor_2
        subtracao = valor_1 - valor_2
        divisao = valor_1 / valor_2
        multiplicacao = valor_1 * valor_2
        pontenciacao = valor_1 ** valor_2

        if operador == '6':
            print(f'Você saiu do programa!')
            break

        elif operador == '1':
            print(f'{valor_1} + {valor_2} = {adicao:.2f}')
            print(linha)
        elif operador == '2':
            print(f'{valor_1} - {valor_2} = {subtracao:.2f}')
            print(linha)
        elif operador == '3':
            print(f'{valor_1} / {valor_2} = {divisao:.2f}')
            print(linha)
        elif operador == '4':
            print(f'{valor_1} * {valor_2} = {multiplicacao:.2f}')
            print(linha)
        elif operador == '5':
            print(f'{valor_1} ** {valor_2} = {pontenciacao:.2f}')
            print(linha)
        else:
            print(f'Por favor, insita um operador válido, você digitou {operador}')
            print(linha)
            continue
    
        sair = input("Deseja sair sa calculadora? Aperte [s]: ").lower().startswith('s')
        print(linha)
        if sair is True:
            print('Obrigado por usar a minha calculadora!')
            print(linha)           
            break
        

    except:
        print('Por favor, digite apenas números.')
        print(linha)