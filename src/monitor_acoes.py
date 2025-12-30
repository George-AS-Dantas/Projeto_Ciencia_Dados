import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import os

print("=== MONITOR DE AÇÕES v1.0 ===")

#Definir o que vamos buscar
carteira_acoes = ['PETR4.SA',  #Petrobras
                  'VALE3.SA', #Vale S.A.
                  'ITUB4.SA', #Itaú
                  'BBDC4.SA', #Bradesco
                  'BPAC11.SA', #BTG Pactual
                  'BBAS3.SA', #Banco do Brasil 
                  'ROXO34.SA' #Nubank
                  ]

dados_acoes = pd.DataFrame()

for item in carteira_acoes:
    try:
        #Baixa os dados
        dados_yahoo = yf.download(item, start="2024-01-01", end="2024-12-31", progress=False)

        #TRATAMENTO (ETL)
        #Seleciona só o fechamento para simplificar e renomeia a coluna close para preco
        df_limpo = dados_yahoo[['Close']].copy()
        df_limpo.columns = ['Preco']

        #Cria a coluna Ticker
        df_limpo['Ticker'] = item.replace('.SA', '') #Tira o .SA para ficar limpo
        
        #Transforma a Data (que é Índice) em Coluna
        df_limpo.reset_index(inplace=True)

        #Transforma a tabela vazia com a tabela tratada
        dados_acoes = pd.concat([dados_acoes, df_limpo], ignore_index=True)
        
    except Exception as e:
        print(f"Erro ao processar {item}: {e}")

#FIM DO LOOP
print("\nSalvando arquivo final...")
caminho_arquivo = os.path.join("dados", "historico_acoes.xlsx")
dados_acoes.to_excel(caminho_arquivo, index=False)
print(f"Arquivo gerado com sucesso: {caminho_arquivo}")