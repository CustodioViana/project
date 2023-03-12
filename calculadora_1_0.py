print('Calculadora com while')


while True:
    valor_1 = int(input('Por favor, digite o primeiro número: '))
    valor_2 = int(input('Por favor, digite o segundo número: '))
    operador = input('Escolha a operação que deseja realizar: \
[1]Adição; \
[2]Subtração; \
[3]Divisão; \
[4]Multiplicação e \
[5]Potencialização: ')
    
    adicao = '{} + {} = '.format(valor_1, valor_2)
    subtracao = '{} - {} = '.format(valor_1, valor_2)
    divisao = '{} / {} = '.format(valor_1, valor_2)
    multiplicacao = '{} * {} = '.format(valor_1, valor_2)
    pontenciacao = '{} ** {} = '.format(valor_1, valor_2)

    if operador == '1':
        print(adicao, valor_1 + valor_2)
    elif operador == '2':
        print(subtracao, valor_1 - valor_2)
    elif operador == '3':
        print(divisao, valor_1 / valor_2)
    elif operador == '4':
        print(multiplicacao, valor_1 * valor_2)
    elif operador == '5':
        print(pontenciacao, valor_1 ** valor_2)
    else:
        print(f'Por favor, insita um {operador=} válido e tente novamente')
    
    sair = input("Deseja sair sa calculadora? Aperte [s]: ").lower().startswith('s')

    fazer = input("Deseja realizar uma nova operação? Aperte [f]: ").lower().startswith('f')
    if fazer is True:
        print('Calcule novamente')

    if sair is True:
        break