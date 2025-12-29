import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#Uso para estudo de pandas e matplotlib
print("=== MONITOR DE AÇÕES v1.0 ===")

#Definir o que vamos buscar
acao = "PETR4.SA"  # Petrobras

#"Leitura" dos dados (Baixando do Yahoo Finance)
print(f"Baixando dados de {acao}...")
dados_yahoo = yf.download(acao, start="2024-01-01", end="2024-12-31")

#Visualizando o DataFrame
print("\n--- AS PRIMEIRAS 5 LINHAS (HEAD) ---")
print(dados_yahoo.head()) 

#Verificando os Tipos
print("\n--- VERIFICAÇÃO DE TIPO ---")
print(f"A variável 'dados' é do tipo: {type(dados_yahoo)}")

#Isolando uma Coluna (Series)
series_fechamento = dados_yahoo['Close'].iloc[:, 0]
print(f"A variável 'fechamento' é do tipo: {type(series_fechamento)}")

#Explorando dados
print("\n=== ANÁLISE EXPLORATÓRIA ===")

#Saude
print("\n--- INFO ---")
dados_yahoo.info()

#Resumo Estatístico (Do Fechamento)
print("\n--- DESCRIBE ---")
dados_estatistica = dados_yahoo[['Close']]
print(dados_estatistica.describe())

#Extremos do Ano
dia_maximo = dados_yahoo[['High']].max().values[0]
dia_minimo = dados_yahoo[['Low']].min().values[0]
dia_atual = dados_yahoo['Close'].iloc[-1].item()

print(f"\n--- RELATÓRIO PETR4 ---")
print(f"Máxima do Ano: R$ {dia_maximo:.2f}")
print(f"Mínima do Ano: R$ {dia_minimo:.2f}")
print(f"Fechamento Atual: R$ {dia_atual:.2f}")

#Filtro de Alta
filtro_maior_38 = series_fechamento > 38
dias_filtrados = dados_yahoo[filtro_maior_38]
print(f"\nDias acima de R$ 38,00: {len(dias_filtrados)}")

#Grafico de evolução de preço
print("\nGerando gráfico...")

dados_yahoo['Close'].plot(title="Histórico de Preço - PETR4", figsize=(10, 5))
plt.show()

print("\nGerando Histograma...")
plt.figure()

dados_yahoo['Close'].hist(bins=30, color='orange')
plt.title("Distribuição de Preços - Onde a ação passou mais tempo?")

plt.show()