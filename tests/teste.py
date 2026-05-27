import pandas as pd
from src import calculadora as calc

print("=== INICIANDO TESTES DA CALCULADORA ===\n")

# --- CENÁRIO 1: Sem gastos variáveis, sem extras, sem reserva ---
# Simulando os dados vazios chegando do banco
fixos_cenario1 = [{'nome': 'Aluguel', 'valor': 1000.0}]
variaveis_cenario1 = pd.DataFrame(columns=['Valor']) # DataFrame vazio

resumo1 = calc.gerar_resumo_financeiro(
    fixos=fixos_cenario1, 
    variaveis=variaveis_cenario1, 
    entregas=0.0, 
    renda_extra_manual=0.0, 
    salario=2000.0
)
print("CENÁRIO 1 (Tudo básico):")
print(resumo1)
print("-" * 40)


# --- CENÁRIO 2: Com Reserva e Gastos Variáveis ---
fixos_cenario2 = [
    {'nome': 'Aluguel', 'valor': 1000.0},
    {'nome': 'Reserva', 'valor': 200.0} # Meta de 10.000 / 200 = 50 meses
]
variaveis_cenario2 = pd.DataFrame({'Valor': [150.0, 50.0]}) # Total de 200.0

resumo2 = calc.gerar_resumo_financeiro(
    fixos=fixos_cenario2, 
    variaveis=variaveis_cenario2, 
    entregas=300.0, 
    renda_extra_manual=100.0, 
    salario=2000.0
)
print("CENÁRIO 2 (Com Reserva e Variáveis):")
print(resumo2)
print("-" * 40)


# --- CENÁRIO 3: Saldo Negativo ---
fixos_cenario3 = [{'nome': 'Cartão', 'valor': 3000.0}]
variaveis_cenario3 = pd.DataFrame(columns=['Valor'])

resumo3 = calc.gerar_resumo_financeiro(
    fixos=fixos_cenario3, 
    variaveis=variaveis_cenario3, 
    entregas=0.0, 
    renda_extra_manual=0.0, 
    salario=2000.0
)
print("CENÁRIO 3 (Saldo Negativo):")
print(resumo3)
print("-" * 40)