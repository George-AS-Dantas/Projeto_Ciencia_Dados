import pandas as pd
import yfinance as yf

print("=== MONITOR DE AÇÕES v1.0 ===")

#Definir o que vamos buscar
acao = "PETR4.SA"  # Petrobras

#"Leitura" dos dados (Baixando do Yahoo Finance)
print(f"Baixando dados de {acao}...")
dados = yf.download(acao, start="2024-01-01", end="2024-12-31")

#Visualizando o DataFrame
print("\n--- AS PRIMEIRAS 5 LINHAS (HEAD) ---")
print(dados.head()) 

#Verificando os Tipos
print("\n--- VERIFICAÇÃO DE TIPO ---")
print(f"A variável 'dados' é do tipo: {type(dados)}")

#Isolando uma Coluna (Series)
fechamento = dados['Close']
print(f"A variável 'fechamento' é do tipo: {type(fechamento)}")