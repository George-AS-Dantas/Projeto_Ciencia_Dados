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

cur.execute("DELETE FROM Extrato")

transacoes = [
    ('2024-01-05', 'Salário', 5000.0, 'Receita'),
    ('2024-01-10', 'Cinema', 50.0, 'Lazer'),
    ('2024-01-11', 'Barzinho', 80.0, 'Lazer'),
    ('2024-01-12', 'Uber Ida', 25.0, 'Transporte'),
    ('2024-01-12', 'Uber Volta', 25.0, 'Transporte'),
    ('2024-01-13', 'Mercado', 450.0, 'Alimentação'),
    ('2024-01-15', 'Padaria', 20.0, 'Alimentação'),
    ('2024-01-15', 'Uber Trabalho', 20.0, 'Transporte')
]

cur.executemany("INSERT INTO Extrato (data,descricao,valor,tipo) VALUES (?, ?, ?, ?)", transacoes)
con.commit()

sql = ("SELECT tipo, SUM(valor) FROM Extrato GROUP BY tipo ORDER BY SUM(valor) DESC")

df = pd.read_sql(sql, con)
print(df)
con.close()