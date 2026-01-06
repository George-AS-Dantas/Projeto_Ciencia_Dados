import sqlite3
import os
import pandas as pd

# Pega o diretório onde este arquivo (database.py) está
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Sobe um nível (para a raiz do projeto)
RAIZ_PROJETO = os.path.dirname(DIRETORIO_ATUAL)

# Aponta para a pasta de dados
PASTA_DADOS = os.path.join(RAIZ_PROJETO, "dados")

# Aponta para o ARQUIVO FINAL completo
CAMINHO_BANCO = os.path.join(PASTA_DADOS, "banco_teste.db")

#Inicio
con = sqlite3.connect(CAMINHO_BANCO)
cur = con.cursor()

#Cria a tabela
cur.execute("""
CREATE TABLE IF NOT EXISTS Extrato(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    descricao TEXT,
    valor REAL,
    tipo TEXT)""")

#Adiciona dados
dados_compra = ('2026-01-05', 'Cinema', 50.0, 'Lazer')
cur.execute("INSERT INTO Extrato (data,descricao,valor,tipo) VALUES (?, ?, ?, ?)", dados_compra)
con.commit()

#seleciona tudo da tabela utilizando pandas
df = pd.read_sql("SELECT * FROM Extrato", con)

print(df)
con.close()