import os
import re
import sys

sair = False
while True:
    print('-')
    try:
        escolha = int(input('Você deseja gerar ou Validar um CPF?\n'
                            '[1] Gerar CPF\n'
                            '[2] Validar CPF\n'
                            '[3] Sair\n'
                            ': '))

        print('-')
        if escolha > 3:
            print('Escolha entre as opções 1, 2 ou 3')

        elif escolha == 1:
            cpf_gerar = input('Digite 9 números: ')
            print('-')
            if len(cpf_gerar) < 9:
                print('Quantidade insuficiente de núemros. Digite 9 números.')

            cpf_gerar = re.sub(
                r'[^0-9]',
                '',
                cpf_gerar
            )

            entrada_repetida = cpf_gerar == cpf_gerar[0] * len(cpf_gerar)
            if entrada_repetida:
                print('Você enviou dados sequenciais.')
                sys.exit()

            dig_9 = cpf_gerar[:9]
            cr_1 = 10
            resultado_1 = 0
            for digito in dig_9:
                resultado_1 += int(digito) * cr_1
                cr_1 -= 1
            dig_1 = (resultado_1 * 10) % 11

            dig_10 = dig_9 + str(dig_1)
            cr_2 = 11
            resutado_2 = 0
            for digito in dig_10:
                resutado_2 += int(digito) * cr_2
                cr_2 -= 1
            dig_2 = (resutado_2 * 10) % 11

            cpf_gerado = f'{dig_9}{dig_1}{dig_2}'

            print(f'Esse é o seu CPF gerado {cpf_gerado}')

        elif escolha == 2:
            cpf = input('Digite o CPF para Validação: ')
            print('-')
            cpf = re.sub(
                r'[^0-9]',
                '',
                cpf
            )

            entrada_repetida = cpf == cpf[0] * len(cpf)
            if entrada_repetida:
                print('Você enviou dados sequenciais.')
                sys.exit()

            dig_9 = cpf[:9]
            cr_1 = 10
            resultado_1 = 0
            for digito in dig_9:
                resultado_1 += int(digito) * cr_1
                cr_1 -= 1
            dig_1 = (resultado_1 * 10) % 11

            dig_10 = dig_9 + str(dig_1)
            cr_2 = 11
            resutado_2 = 0
            for digito in dig_10:
                resutado_2 += int(digito) * cr_2
                cr_2 -= 1
            dig_2 = (resutado_2 * 10) % 11

            cpf_gerado = f'{dig_9}{dig_1}{dig_2}'

            if cpf == cpf_gerado:
                print(f'Este CPF {cpf} é Válido')
            else:
                print('CPF inválido')
        elif escolha == 3:
            os.system('cls')        
            print('Obrigado por usar meu sistema de CPF')            
            break
    except TypeError:
        print('Letras não são permitidas. Tente novamente')
    except ValueError:
        print('Letras não são permitidas. Tente novamente')

