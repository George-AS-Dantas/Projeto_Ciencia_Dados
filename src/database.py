import pandas as pd
import json
import os
from datetime import date
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


# Pega o diretório onde este arquivo (database.py) está
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Sobe um nível (para a raiz do projeto)
RAIZ_PROJETO = os.path.dirname(DIRETORIO_ATUAL)

# Aponta para a pasta de dados
PASTA_DADOS = os.path.join(RAIZ_PROJETO, "dados")

# Define os caminhos finais
TABELA_GASTOS = os.path.join(PASTA_DADOS, "gastos_variaveis.csv")
TABELA_ENTRADAS = os.path.join(PASTA_DADOS, "entradas.csv")
ARQUIVO_FIXOS = os.path.join(PASTA_DADOS, "gastos_fixos.json")

# --- FUNÇÕES DE GASTOS FIXOS (JSON) ---

def carregar_gastos_fixos():
    gastos_fixos_padrao = [
        {"nome": 'Casa', 'valor': 170},
        {'nome': 'Moto', 'valor': 985},
        {'nome': 'Suhai', 'valor': 385},
        {'nome': 'Reserva', 'valor': 250}
    ]
    
    if os.path.exists(ARQUIVO_FIXOS):
        try:
            with open(ARQUIVO_FIXOS, "r", encoding='utf8') as arquivo:
                gastos_fixos = json.load(arquivo)
            print("Gastos fixos carregados do arquivo com sucesso!")
            return gastos_fixos
        except:
            print("Arquivo corrompido. Recriando padrão...")
            return gastos_fixos_padrao
    else:
        # Cria o arquivo inicial se não existir
        salvar_gastos_fixos(gastos_fixos_padrao)
        print("Primeira execução: Arquivo criado com seus gastos padrão!")
        return gastos_fixos_padrao

def salvar_gastos_fixos(lista_atualizada):
    with open(ARQUIVO_FIXOS, "w", encoding='utf8') as arquivo:
        json.dump(lista_atualizada, arquivo, indent=4)
    print("Dados gravados no arquivo JSON!")

# --- FUNÇÕES DE TRANSAÇÕES (CSV) ---

def inicializar_banco_gastos():
    if os.path.exists(TABELA_GASTOS):
        print("Base de gastos carregada!")
    else:
        gastos_vazio = {
            'Data':[], 'Nome':[], 'Valor':[], 'Categoria':[] 
        }
        df_gastos = pd.DataFrame(gastos_vazio)
        df_gastos.to_csv(TABELA_GASTOS, index=False)
        print("Novo banco de gastos criado!")

def inicializar_banco_entradas():
    try: 
        pd.read_csv(TABELA_ENTRADAS)
        print("Base de entradas carregada!")
    except:
        entradas_vazio = {
            'Data':[], 'Nome':[], 'Valor':[], 'Origem':[] 
        }
        df_entradas = pd.DataFrame(entradas_vazio)
        df_entradas.to_csv(TABELA_ENTRADAS, index=False)
        print("Novo banco de entradas criado!")

def salvar_novo_gasto(item, valor, categoria):
    df_gastos = pd.read_csv(TABELA_GASTOS)
    data_hoje = date.today()
    
    novo_gasto = {
        'Data': [data_hoje],
        'Nome': [item], 
        'Valor': [valor],
        'Categoria': [categoria]
    }
    df_novo_gasto = pd.DataFrame(novo_gasto)
    gastos_atualizado = pd.concat([df_gastos, df_novo_gasto], ignore_index=True)
    gastos_atualizado.to_csv(TABELA_GASTOS, index=False)
    return gastos_atualizado

def salvar_nova_renda(item, valor, origem):
    # Carrega ou cria
    try:
        df_entradas = pd.read_csv(TABELA_ENTRADAS)
    except:
        inicializar_banco_entradas()
        df_entradas = pd.read_csv(TABELA_ENTRADAS)

    data_hoje = date.today()
    nova_renda = {
        'Data': [data_hoje],
        'Nome': [item],
        'Valor': [valor],
        'Origem': [origem]
    }
    df_nova_renda = pd.DataFrame(nova_renda)
    entradas_atualizado = pd.concat([df_entradas, df_nova_renda], ignore_index=True)
    entradas_atualizado.to_csv(TABELA_ENTRADAS, index=False)
    return entradas_atualizado

def ler_todos_gastos():
    return pd.read_csv(TABELA_GASTOS)

def ler_todas_entradas():
    try:
        return pd.read_csv(TABELA_ENTRADAS)
    except:
        return pd.DataFrame({'Valor': []}) # Retorna vazio se der erro
    
    # Adicione isso no final do database.py

def buscar_renda_entregas():
    url_planilha = 'https://docs.google.com/spreadsheets/d/16VXgnu18Hf3D5tX55EHcjguxa7_DCLga1EKXWDzvL5E/export?format=csv'
    try:
        #Lê a planilha direto da URL
        renda_entregas = pd.read_csv(url_planilha, header=2, decimal=',', thousands='.')
        return renda_entregas['Lucro liquido'].sum()
    except Exception as e:
        print(f"Erro de conexão com Google Sheets: {e}")
        return 0.0