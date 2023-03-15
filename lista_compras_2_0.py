import os
linha = ('-\n'
         '-')
"""
Faça uma lista de comprar com listas
- O usuário deve ter possibilidade de inserir, apagar e listar valores da sua lista
- Não permita que o programa quebre com erros de ídices inexistenste na lista
"""

# alimento = ['arroz', 'feijoa', 'macarrao', 'batata']
# bebida = ['coca', 'agua', 'suco', 'cafe']

alimento = []
bebida = []


while True:

    entrada = input('Escolha uma função desejada:\n'
                    '[I]nserir\n'
                    '[V]erificar ou Apagar\n'
                    '[S]air: ').upper()

    try:
        os.system('cls')
        if entrada == 'I':  # inserir item

            produto = input('Oque deseja inseir? ')
            categoria = int(input('Em qual lista?\n'
                            '[1]Alimento\n'
                                  '[2]Bebidas: '))

            if categoria == 1:
                alimento.append(produto)
                print(f'Você adicionou {produto} na categoria ALIMENTO')
            elif categoria == 2:
                bebida.append(produto)
                print(f'Você adicionou {produto} na categoria BEBIDA')
            else:
                print('Escreva um númeor válido')
                continue

        elif entrada == 'V':
            print('Esses são os itens da lista:')
            print(linha)
            lista = alimento + bebida
            if len(lista) == 0:
                print('A lista está vazia')
                continue
            print('ALIMENTO')
            for ver in range(len(alimento)):
                print(ver, alimento[ver])

            print('BEBIDA')
            for ver in range(len(bebida)):
                print(ver, bebida[ver])
            escolha = input('Deseja apagar? [S]im ou [N]ão: ').upper()
            if escolha == 'N':
                continue

            elif escolha == 'S':
                apg_cate = input('Escolha a categoria\n'
                                 '[A]limeto\n'
                                 '[B]ebida: ').upper()
                try:    
                    if apg_cate == 'A':
                        apg = input('Escolha o item para apagar: ')
                        try:
                            apg = int(apg)
                            if apg >= 0 and apg < len(alimento):
                                alimento.pop(apg)
                                print('Item apagado com sucesso')
                            else:
                                print('Número inválido')
                        except ValueError:
                            print('Digite um número válido')

                    if apg_cate == 'B':
                        apg = input('Escolha o item para apagar: ')
                        try:
                            apg = int(apg)
                            if apg >= 0 and apg < len(bebida):
                                bebida.pop(apg)
                                print('Item apagado com sucesso')
                            else:
                                print('Número inválido')
                        except ValueError:
                            print('Digite um número válido')
                except:
                    print('Digite somente A ou B')
                    continue
            else:
                print('Dado incorreto. Digite S ou N')
            print(linha)

        elif entrada == 'S':
            sair = input('Deseja sair?\n'
                         'Digite [S]air ou [C]ontinuar: ').upper()
            if 'S' in sair:
                break
        else:
            print('Função inexistente, tente novamente')
            continue

    except:
        print('Digite o valor da função ou categoria carrote!')

    # os.system('cls')