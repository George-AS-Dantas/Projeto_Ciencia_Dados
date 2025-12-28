import numpy as np
import pandas as pd
import json
import os
from datetime import date

#Inicio
tabela_gastos = "gastos.csv"
tabela_entradas = "entradas.csv"
arquivo_fixos = "gastos_fixos.json"

#Gastos fixos
gastos_fixos_padrão = [
                 {"nome": 'Casa', 'valor': 170},
                 {'nome': 'Moto', 'valor': 985},
                 {'nome': 'Suhai', 'valor': 385},
                 {'nome': 'Reserva', 'valor': 250}
                ]
#tenta acessar o json de gastos fixos, e usa o padrão acima caso não consiga
if os.path.exists(arquivo_fixos):
    try:
        with open(arquivo_fixos, "r", encoding='utf8') as arquivo:
            gastos_fixos = json.load(arquivo)
        print("Gastos fixos carregados do arquivo com sucesso!")
    except:
        # Se o arquivo existir mas estiver corrompido/vazio
        print("Arquivo corrompido. Recriando padrão...")
        gastos_fixos = gastos_fixos_padrão
else: #Caso arquivo não exista
    gastos_fixos = gastos_fixos_padrão

    with open(arquivo_fixos, "w", encoding='utf8') as arquivo:
        json.dump(gastos_fixos, arquivo, indent=4)
    
    print("Primeira execução: Arquivo criado com seus gastos padrão!")
#salvar os gastos fixos

#Acessa a base de dados gastos caso exista e cria uma se não existir
if os.path.exists(tabela_gastos):
	df_gastos = pd.read_csv(tabela_gastos)
	print("Base de gastos carregada!")
else:
	gastos_vazio = {
                     'Data':[], 
                     'Nome':[],
                     'Valor':[],
                     'Categoria':[] 
                    }
	df_gastos = pd.DataFrame(gastos_vazio)
	df_gastos.to_csv(tabela_gastos, index=False)
	print("Novo banco de gastos criado!")

#Menu do programa
def exibir_menu():
    print("\n=== Bem vindo ao gestor financeiro! ===\n")
    print("1 - Adicionar gasto variavel")
    print("2 - Relatório")
    print("3 - Adicionar renda extra")
    print("4 - Consultar gastos fixos")
    print("5 - Gerenciar gastos fixos")
    print("6 - Sair")
    return input('Escolha uma opção: ')

#salva o json de gastos
def salvar_alteracoes(lista_atualizada):
    with open(arquivo_fixos, "w", encoding='utf8') as arquivo:
        json.dump(lista_atualizada, arquivo, indent=4)
    print("Dados gravados no arquivo JSON!")

#Função para adicionar gastos
def adicionar_gastos ():
    print("\n=== NOVO GASTO ===\n")
    df_gastos = pd.read_csv(tabela_gastos)
    data_hoje = date.today()

#entradas do usuário
    categoria = input('Qual a categoria do gasto? (ex.: Transporte, Alimentação, lazer): ').upper()
    item = input('Qual gasto a ser adicionado? (ex. Pizza, uber, cinema): ')
    valor = float(input(f"Quanto você gastou com {item}?: "))
    
    if valor > 0:
        novo_gasto = {
            'Data': [data_hoje],
            'Nome': [item], 
            'Valor': [valor],
            'Categoria': [categoria]}
        
        df_novo_gasto = pd.DataFrame(novo_gasto)

        print(f"{item} adicionado com sucesso!")

        gastos_atualizado = pd.concat([df_gastos, df_novo_gasto], ignore_index=True)
        gastos_atualizado.to_csv(tabela_gastos, index=False)
        print("\n--- TABELA DE GASTOS ATUALIZADO ---")
        print(gastos_atualizado)

    else:
        print('Valor incorreto! O gasto não foi salvo.')

#Função para adicionar renda extra
def adicionar_renda_extra():
    data_hoje = date.today()
    print("\n=== RENDA EXTRA ===\n")

#criando ou acessando banco de entradas
    try: 
        df_entradas = pd.read_csv(tabela_entradas)
        print("Base de entradas carregada!")
    except:
        entradas_vazio = {
                     'Data':[], 
                     'Nome':[],
                     'Valor':[],
                     'Origem':[] 
                    }
        df_entradas = pd.DataFrame(entradas_vazio)
        df_entradas.to_csv(tabela_entradas, index=False)
        print("Novo banco de entradas criado!")

    origem = input('Qual a origem da renda?(Ex. Entregas, vendas, freela): ').upper()
    item = input('Oque foi feito para adquirir a renda?(Ex. Item vendido, freelance feito, presente recebido): ')
    valor = float(input(f"Qual valor arrecadado com {item}?: "))
    
    if origem == 'ENTREGAS':
        print('Para entradas vindas de entregas, utilize a planilha (Controle de entradas - Entregas)')
    elif valor > 0:
        nova_renda = {
            'Data': [data_hoje],
            'Nome': [item],
            'Valor': [valor],
            'Origem': [origem]
        }
        df_nova_renda = pd.DataFrame(nova_renda)
        print(f"{origem} adicionado com sucesso!")

        entradas_atualizado = pd.concat([df_entradas, df_nova_renda], ignore_index=True)
        entradas_atualizado.to_csv(tabela_entradas, index=False)
        print("\n--- TABELA DE ENTRADAS ATUALIZADO ---")
        print(entradas_atualizado)

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
            salvar_alteracoes(gastos_fixos)

            print(f"{item} adicionado com sucesso!")
        else:
            print('Valor incorreto! O gasto não foi salvo.')

#Remover
    elif gerenciamento_gastos == '2':
        listar_gastos_fixos(gastos_fixos)

        try:
            indice = int(input('Qual numero do gasto fixo que gostaria de remover?\n'))
            gasto_removido = gastos_fixos.pop(indice)
            salvar_alteracoes(gastos_fixos)

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
                salvar_alteracoes(gastos_fixos)

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
def ver_relatorio(salario, gastos_fixos):
#Variaveis temporarias
    total_fixo = 0
    total_gasto_variavel = 0
    renda_extra_manual = 0
    total_renda_extra = 0
    valor_da_reserva = 0

    #acessa as tabelas
    df_gastos = pd.read_csv(tabela_gastos)
    
    #entradas que não são entregas de app
    try:
        df_entradas = pd.read_csv(tabela_entradas)
        renda_extra_manual = df_entradas['Valor'].sum()
    except:
        print('Tabela de entradas manual não encontrada. Considerando R$ 0,00.')   
    #entregas de app
    try:
        url_planilha = 'https://docs.google.com/spreadsheets/d/16VXgnu18Hf3D5tX55EHcjguxa7_DCLga1EKXWDzvL5E/export?format=csv'
        renda_entregas = pd.read_csv(url_planilha, header=2, decimal=',', thousands='.')
        total_entregas = renda_entregas['Lucro liquido'].sum()
        print(f"Entregas salvas no sheets: R$ {total_entregas:.2f}")
    except:
        total_entregas = 0
        print('Erro ao acessar planilha, verifique!')

#Cálculo da Renda Extra
    total_renda_extra = renda_extra_manual + total_entregas

#Cálculo dos Gastos Fixos
    valores_fixos = [item['valor'] for item in gastos_fixos]
    array_fixos = np.array(valores_fixos)
    total_fixo = np.sum(array_fixos)

#Cálculo dos Gastos
    total_gasto_variavel = df_gastos['Valor'].sum()
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
    gastos_altos = df_gastos[df_gastos['Valor']>300]
    if len(gastos_altos) > 0:
        print(f'!!!!!ATENÇÃO!!!!! \nVocê tem {len(gastos_altos)} gasto(s) variável(is) acima de R$ 300.00!')

#Relatorio para o usuário
    print (f'O valor total das despesas é: {total_gastos}')
    print (f'O valor que sobra depois de pagar as contas é: {saldo_final:.2f}')
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

#Loop principal
while True:
    opcao = exibir_menu()

    #Chama a função de adicionar
    if opcao == '1':
        adicionar_gastos()

    #Chama a função de relatório PASSANDO os dados   
    elif opcao == '2':
        ver_relatorio(salario, gastos_fixos)
    
    elif opcao == '3':
        adicionar_renda_extra()
    elif opcao == '4':
        listar_gastos_fixos(gastos_fixos)

    elif opcao == '5':
        gerenciar_gastos_fixos(gastos_fixos)
    
    elif opcao == '6':
        print("Saindo... Até logo!")
        break
        
    else:
        print("Opção inválida ou em desenvolvimento...")



