import numpy as np

#Menu do programa
def exibir_menu():
    print("\n=== Bem vindo ao gestor financeiro! ===\n")
    print("1 - Adicionar gasto")
    print("2 - Relatório de gastos")
    print("3 - Adicionar renda variavel")
    print("4 - Consultar gastos fixos")
    print("5 - Gerenciar gastos fixos")
    print("6 - Sair")
    return input('Escolha uma opção: ')

#Função para adicionar gastos
def adicionar_gastos (gastos_variaveis):
    print("\n=== NOVO GASTO ===\n")
    item = input('Qual gasto a ser adicionado? (ex. Cartão, delivery): ')
    valor = float(input(f"Quanto você gastou com {item}?: "))

    if valor > 0:
        novo_gasto = {
            'nome': item, 
            'valor': valor
        }
        gastos_variaveis.append(novo_gasto)
        print(f"{item} adicionado com sucesso!")
    else:
        print('Valor incorreto! O gasto não foi salvo.')

#Função para adicionar renda extra
def adicionar_renda_extra(renda_extra):
    print("\n=== RENDA EXTRA ===\n")
    item = input('Qual a origem da renda?(Ex. Delivery, vendas, freela): ')
    valor = float(input(f"Qual valor arrecadado com {item}?: "))
    
    if valor > 0:
        nova_renda = {
            'nome': item, 
            'valor': valor
        }
        renda_extra.append(nova_renda)
        print(f"{item} adicionado com sucesso!")
    else:
        print('Valor incorreto! A entrada não foi salva.')

#Função para visualizar indice e gastos fixos
def listar_gastos_fixos(gastos_fixos):
    print("\n--- LISTA ATUAL DE GASTOS FIXOS ---")

    for i, gasto in enumerate(gastos_fixos):
        print(f"{i} - {gasto['nome']}: R$ {gasto['valor']:.2f}")

#Função para alterar os gastos fixos
def gerenciar_gastos_fixos(gastos_fixos):
    print("\n=== GESTÃO DE GASTOS FIXOS ===")

    gerenciamento_gastos = input('Deseja alterar, remover, adicionar gastos fixos?'
                            '\nPara adicionar digite: 1\n'
                            'Para remover digite: 2\n'
                            'Para alterar digite: 3\n'
                            'Para voltar ao menu: 4\n')

#Adicionar
    if gerenciamento_gastos == '1':
        listar_gastos_fixos(gastos_fixos)

        item = input('Qual gasto a ser adicionado?\n')
        valor = float(input('Qual o valor deste gasto?\n'))

        if valor > 0:
            novo_gasto = {
            'nome': item, 
            'valor': valor
        }
            gastos_fixos.append(novo_gasto)
            print(f"{item} adicionado com sucesso!")
        else:
            print('Valor incorreto! O gasto não foi salvo.')

#Remover
    elif gerenciamento_gastos == '2':
        listar_gastos_fixos(gastos_fixos)

        try:
            indice = int(input('Qual numero do gasto fixo que gostaria de remover?\n'))
            gasto_removido = gastos_fixos.pop(indice)
            print(f"'{gasto_removido['nome']}' removido com sucesso!")
        
        except ValueError:
            #Se digitar letra:
            print("Erro: Digite apenas números inteiros!")
        except IndexError:
            #Se digitar número que não existe:
            print("Erro: Esse número não existe na lista!")

#Alterar
    elif gerenciamento_gastos == '3':    
        listar_gastos_fixos(gastos_fixos)

        try:
            indice_escolhido = int(input('Qual numero do gasto fixo que deseja alterar?\n'))
            
            nome_gasto = gastos_fixos[indice_escolhido]['nome']
            print(f"Selecionado: {nome_gasto}")

            novo_valor = float(input(f'Digite o novo valor para {nome_gasto}: '))

            if novo_valor > 0:
                gastos_fixos[indice_escolhido]['valor'] = novo_valor
                print(f"Sucesso! Valor de '{nome_gasto}' atualizado para R$ {novo_valor:.2f}")
            else:
                print("Erro: O valor deve ser maior que zero.")
        
        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except IndexError:
            print("Erro: Esse número não existe na lista!")

    #Menu (Voltar)
    elif gerenciamento_gastos == '4':
        print("Voltando ao menu principal...")
    
    else:
        print("Opção inválida dentro da gestão.")

#Função para soma de gastos e relatório
def ver_relatorio(salario, gastos_fixos, gastos_variaveis, renda_extra):
#Variaveis temporarias
    total_fixo = 0
    total_gasto_variavel = 0
    total_renda_extra = 0
    valor_da_reserva = 0

#Cálculo da Renda Extra
    valores_renda_extra = [item['valor'] for item in renda_extra]
    array_renda_extra = np.array(valores_renda_extra)
    total_renda_extra = np.sum(array_renda_extra)

#Cálculo dos Gastos Fixos
    valores_fixos = [item['valor'] for item in gastos_fixos]
    array_fixos = np.array(valores_fixos)
    total_fixo = np.sum(array_fixos)

#Cálculo dos Gastos Variáveis
    valores_variaveis = [item ['valor'] for item in gastos_variaveis]
    array_variaveis = np.array(valores_variaveis)
    total_gasto_variavel = np.sum(array_variaveis)

    total_gastos = (total_fixo + total_gasto_variavel)
    saldo_final = salario + total_renda_extra - total_gastos

#Reserva de emergencia
    reserva_emergencia_meta = 0
#Cálculo reserva de emergencia
    for item in gastos_fixos:
     if item['nome'] == 'Reserva':
        valor_da_reserva = item['valor']
        break
     
#Objetivo reserva de emergencia
    if valor_da_reserva > 0:
        reserva_emergencia_meta = 10000 / valor_da_reserva
    else:
        print('Reserva de emergencia inalterada!')
    

#Alertas
    alertas = array_variaveis[array_variaveis>300]
    if len(alertas) > 0:
        print(f'!!!!!ATENÇÃO!!!!! \nVocê tem {len(alertas)} gasto(s) variável(is) acima de R$ 300.00!')

#Relatorio para o usuário
    print (f'O valor total das despesas é: {total_gastos}')
    print (f'O valor que sobra depois de pagar as contas é: {saldo_final}')
    print (f'Para atingir a meta da reserva de emergencia, levará {reserva_emergencia_meta} meses!\n')
    print(f"Relatório: R$ {total_fixo:.2f} Fixos + R$ {total_gasto_variavel:.2f} Variáveis")
    
#logica de decisão

    if saldo_final < 0:
        print ("!!!Atenção!!! \nSALDO NEGATIVO, CORTE GASTOS E AUMENTE A RENDA")
    elif saldo_final < salario*0.10:
        print ("!Cuidado! \nAumente a renda para que tenha sobra do salario")
    else:
        print ("Parabéns!!\nA saúde financeira está indo bem!")

#adiciona renda fixa
salario = float(input("Digite seu salário: "))

#Gastos fixos
gastos_fixos = [
                 {'nome': 'Casa', 'valor': 170},
                 {'nome': 'Moto', 'valor': 985},
                 {'nome': 'Suhai', 'valor': 385},
                 {'nome': 'Reserva', 'valor': 250}
                ]

#variaveis
renda_extra = []
gastos_variaveis = []

#Loop principal
while True:
    opcao = exibir_menu()

    #Chama a função de adicionar
    if opcao == '1':
        adicionar_gastos(gastos_variaveis)

    #Chama a função de relatório PASSANDO os dados   
    elif opcao == '2':
        ver_relatorio(salario, gastos_fixos, gastos_variaveis, renda_extra)
    
    elif opcao == '3':
        adicionar_renda_extra(renda_extra)
    elif opcao == '4':
        listar_gastos_fixos(gastos_fixos)

    elif opcao == '5':
        gerenciar_gastos_fixos(gastos_fixos)
    
    #Encerrar o programa
    elif opcao == '6':
        print("Saindo... Até logo!")
        break
        
    else:
        print("Opção inválida ou em desenvolvimento...")



