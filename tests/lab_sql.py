import sqlite3
import os
import pandas as pd


# 1. Configura Caminhos
CAMINHO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Apontando para o BANCO OFICIAL
CAMINHO_BANCO = os.path.join(CAMINHO_BASE, 'dados', 'banco_principal.db') 

# 2. Conecta
con = sqlite3.connect(CAMINHO_BANCO)
cur = con.cursor()

# --- FAXINA (Executar uma vez para apagar a tabela de teste errada) ---
try:
    cur.execute("DROP TABLE IF EXISTS Extrato") # Apaga a tabela com dados falsos
    con.commit()
    print("Limpeza concluída: Tabela de teste 'Extrato' removida do banco oficial.")
except Exception as e:
    print(f"Erro na limpeza: {e}")

# --- VERIFICAÇÃO (Ler a tabela certa que veio do CSV) ---
# Note que o nome agora é 'gastos' (minúsculo), que foi o nome que demos na migração
sql = "SELECT * FROM entradas"

try:
    df = pd.read_sql(sql, con)
    print("\n--- DADOS REAIS DO CSV (Tabela 'gastos') ---")
    print(df.head()) # Mostra as 5 primeiras linhas
    print("-" * 30)
    print(f"Total de linhas encontradas: {len(df)}")
except Exception as e:
    print(f"\nErro ao ler a tabela 'gastos': {e}")
    print("Dica: Verifique se o script migracao.py rodou corretamente.")

con.close()