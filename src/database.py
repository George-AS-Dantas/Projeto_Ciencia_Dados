import pandas as pd
import sqlite3
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
ARQUIVO_FIXOS = os.path.join(PASTA_DADOS, "gastos_fixos.json")
CAMINHO_BANCO = os.path.join(PASTA_DADOS, "banco_principal.db")


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

def salvar_novo_gasto(item, valor, categoria):
    data_hoje = date.today()

    con = sqlite3.connect(CAMINHO_BANCO)
    cur = con.cursor()

    sql_query = ("INSERT INTO gastos (Data, Nome, Valor, Categoria) VALUES (?, ?, ?, ?)")
    cur.execute(sql_query, (data_hoje, item, valor, categoria))

    con.commit()
    con.close()

    return ler_todos_gastos()

def salvar_nova_renda(item, valor, origem):
    data_hoje = date.today()

    con = sqlite3.connect(CAMINHO_BANCO)
    cur = con.cursor()

    sql_query = ("INSERT INTO entradas (Data, Nome, Valor, Categoria) VALUES (?,?,?,?)")
    cur.execute(sql_query, (data_hoje, item, valor, origem))

    con.commit()
    con.close()

    return ler_todas_entradas()

def ler_todos_gastos():
    con = sqlite3.connect(CAMINHO_BANCO)
    sql_query = ("SELECT * FROM gastos")
    df = pd.read_sql(sql_query, con)
    con.close()

    return df

def ler_todas_entradas():
    con = sqlite3.connect(CAMINHO_BANCO)
    sql_query = ("SELECT * FROM entradas")
    df = pd.read_sql(sql_query, con)
    con.close()

    return df

def buscar_renda_entregas():
    url_planilha = 'https://docs.google.com/spreadsheets/d/16VXgnu18Hf3D5tX55EHcjguxa7_DCLga1EKXWDzvL5E/export?format=csv'
    try:
        #Lê a planilha direto da URL
        renda_entregas = pd.read_csv(url_planilha, header=2, decimal=',', thousands='.')
        return renda_entregas['Lucro liquido'].sum()
    except Exception as e:
        print(f"Erro de conexão com Google Sheets: {e}")
        return 0.0