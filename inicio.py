"""Módulo responsável pela interação do usuário com o sistema.


"""

import validacao as valid
from controller import Controller

if __name__ == '__main__':
    controller = Controller()

    while True:
        print('--------------Menu--------------')
        print('[1] Cadastrar anúncio')
        print('[2] Gerar relatórios de anúncios')
        print('[0] Sair')

        escolha = input('O que deseja fazer? ')

        if escolha.isdigit():
            escolha = int(escolha)

            if escolha == 1: #Cadastra novo anúncio
                print('Preencha as informações para o cadastro do anúncio:')
                nome = input('Nome: ')
                cliente = input('Cliente: ')

                while True:
                    data_inicio = input('Data de início (dd/mm/aaaa): ')
                    if valid.data_valida(data_inicio):
                        break
                    else:
                        print('Data de início inválida')

                while True:
                    data_termino = input('Data de término (dd/mm/aaaa): ')
                    if valid.data_valida(data_termino):
                        break
                    else:
                        print('Data de término inválida')

                while True:
                    investimento = input('Investimento por dia (em reais): ')
                    if not valid.is_float(investimento):
                        print('Valor de investimento inválido')
                    else:
                        investimento = float(investimento)
                        break

                if controller.cadastrar_anuncio(nome, cliente, data_inicio, data_termino, investimento):
                    print('Anúncio cadastrado com sucesso')
                else:
                    print('Erro ao cadastrar o anúncio')

            elif escolha == 2: #Gera o relatório
                cliente = ''
                data_inicio = ''
                data_termino = ''
                tipo_calculo = 'truncado'
                while True:
                    print('--------Relatório de Anúncios--------')
                    print('[1] Filtrar por Cliente')
                    print('[2] Filtrar por Data de Início ')
                    print('[3] Filtrar por Data de Término')
                    print('[4] Limpar todos os filtros')
                    print('[5] Gerar Relatório')
                    print('[6] Alterar tipo de cálculo')
                    print('[0] Voltar ao Menu')

                    print('Filtros aplicados: ')
                    print('-Cliente: ', end='')
                    if cliente == '':
                        print('Todos')
                    else:
                        print(cliente)

                    print('-Data de Início: ', end='')
                    if data_inicio == '':
                        print('Todos')
                    else:
                        print(data_inicio)

                    print('-Data de Término: ', end='')
                    if data_termino == '':
                        print('Todos')
                    else:
                        print(data_termino)

                    print()
                    print(f'Tipo de cálculo: {tipo_calculo}')
                    print()
                    opcao = input('O que deseja fazer? ')
                    if opcao.isdigit():
                        opcao = int(opcao)

                        if opcao == 1: #Altera cliente do filtro
                            entrada = input('Qual o cliente? [0] para voltar:')
                            if entrada != '0':
                                cliente = entrada

                        elif opcao == 2: #Altera data de início do filtro
                            while True:
                                entrada = input('Data de Início (dd/mm/aaaa): [0] para voltar:')
                                if entrada == '0':
                                    break
                                elif valid.data_valida(entrada):
                                    data_inicio = entrada
                                    break
                                else:
                                    print('Data de início inválida')

                        elif opcao == 3: #Altera data de término do filtro
                            while True:
                                entrada = input('Data de Término (dd/mm/aaaa). [0] para voltar: ')
                                if entrada == '0':
                                    break
                                elif valid.data_valida(entrada):
                                    data_termino = entrada
                                    break
                                else:
                                    print('Data de término inválida')

                        elif opcao == 4: #Reseta filtro
                            cliente = ''
                            data_inicio = ''
                            data_termino = ''

                        elif opcao == 5: #Gera relatório
                            resultado = controller.gera_relatorio(cliente,data_inicio, data_termino, tipo_calculo)
                            if resultado:
                                print(f'---------RELATÓRIO DE ANÚNCIOS---------')
                                print(f'{len(resultado)} Resultados')

                                for anuncio in resultado:

                                    print('---------------------------------------')
                                    print(f'Nome: {anuncio[0].nome} | Cliente: {anuncio[0].cliente} | '
                                          f'Data de Início: {anuncio[0].data_inicio} | '
                                          f'Data de Término {anuncio[0].data_termino}')

                                    print(f'Investimento Total: {anuncio[1]} | Cliques: {anuncio[2][0]} | '
                                          f'Compartilhamentos: {anuncio[2][1]} | Visualizações {anuncio[2][2]}')
                                    print('---------------------------------------')

                            else:
                                print('Nenhum resultado encontrado. Altere o filtro ou cadastre um anúncio.')

                        elif opcao == 6: #Altera tipo de cálculo do relattório
                            while True:
                                entrada = input(
                                    'Qual tipo de cálculo? (p - proporcional | t - truncado | [0] para voltar)')
                                if entrada != '0':
                                    if entrada == 'p':
                                        tipo_calculo = 'proporcional'
                                        break

                                    elif entrada == 't':
                                        tipo_calculo = 'truncado'
                                        break

                                    else:
                                        print('Opção inválida')
                                else:
                                    break

                        elif opcao == 0: #Volta ao menu
                            break

                        else:
                            print('Opção inválida')

                    else:
                        print('Opção inválida')

            elif escolha == 0: #Termina execução do programa
                break

            else:
                print('Opção inválida')

        else:
            print('Opção inválida')
