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

con = sqlite3.connect(CAMINHO_BANCO)

sql_query = ("SELECT rowid, * FROM gastos")
df = pd.read_sql(sql_query, con)
con.close()

print(df)
