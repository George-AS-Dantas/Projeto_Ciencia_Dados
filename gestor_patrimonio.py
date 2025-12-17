import numpy as np

#Menu do programa
def exibir_menu():
    print("=== Bem vindo ao gestor financeiro! ===\n")
    print("1 - Adicionar gasto")
    print("2 - Relatório de gastos")
    print("3 - Adicionar renda variavel")
    print("4 - Alterar gastos fixos")
    print("5 - Sair")
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

#Função para soma de gastos e relatório
def ver_relatorio(salario, gastos_fixos, gastos_variaveis):
    total_fixo = 0
    total_variavel = 0

    valores_fixos = [item['valor'] for item in gastos_fixos]
    array_fixos = np.array(valores_fixos)
    total_fixo = np.sum(array_fixos)

    valores_variaveis = [item ['valor'] for item in gastos_variaveis]
    array_variaveis = np.array(valores_variaveis)
    total_variavel = np.sum(array_variaveis)

    total_gastos = (total_fixo + total_variavel)
    saldo_final = salario - total_gastos

#Objetivo reserva de emergencia
    reserva_emergencia_meta = 10000 / gastos_fixos[3]['valor']

#Alertas
    alertas = array_variaveis[array_variaveis>300]
    if len(alertas) > 0:
        print(f'!!!!!ATENÇÃO!!!!! \nVocê tem {len(alertas)} gasto(s) variável(is) acima de R$ 300.00!')

#Relatorio para o usuário
    print (f'O valor total das despesas é: {total_gastos}')
    print (f'O valor que sobra depois de pagar as contas é: {saldo_final}')
    print (f'Para atingir a meta da reserva de emergencia, levará {reserva_emergencia_meta} meses!\n')
    print(f"Relatório: R$ {total_fixo:.2f} Fixos + R$ {total_variavel:.2f} Variáveis")
    
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

#Gastos variaveis
gastos_variaveis = []

#Loop principal
while True:
    opcao = exibir_menu()

    #Chama a função de adicionar
    if opcao == '1':
        adicionar_gastos(gastos_variaveis)

    #Chama a função de relatório PASSANDO os dados   
    elif opcao == '2':
        ver_relatorio(salario, gastos_fixos, gastos_variaveis)
    
    #Encerrar o programa
    elif opcao == '5':
        print("Saindo... Até logo!")
        break
        
    else:
        print("Opção inválida ou em desenvolvimento...")



