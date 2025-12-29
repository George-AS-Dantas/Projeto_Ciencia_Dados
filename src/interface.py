def exibir_menu_principal():
    print("\n=== Bem vindo ao gestor financeiro! ===\n")
    print("1 - Adicionar gasto variavel")
    print("2 - Relatório")
    print("3 - Adicionar renda extra")
    print("4 - Consultar gastos fixos")
    print("5 - Gerenciar gastos fixos")
    print("6 - Sair")
    return input('Escolha uma opção: ')

def ler_valor(mensagem):
#Tenta ler um float, se der erro pede de novo
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número válido (ex: 10.50)")

def ler_texto(mensagem):
    return input(mensagem)

def formulario_novo_gasto():
    print("\n=== NOVO GASTO ===")
    categoria = input('Qual a categoria? (ex.: Transporte, Alimentação): ').upper()
    item = input('O que você comprou?: ')
    valor = ler_valor(f"Quanto custou {item}?: ")
    return item, valor, categoria

def formulario_nova_renda():
    print("\n=== RENDA EXTRA ===")
    origem = input('Qual a origem da renda? (Ex. Vendas, Freela): ').upper()
    item = input('Descrição (Ex. Item vendido): ')
    valor = ler_valor(f"Qual valor arrecadado?: ")
    return item, valor, origem

def mostrar_relatorio_final(fixos, variaveis, entregas, renda_extra_manual, salario):
    # Lógica de visualização
    total_fixo = sum([f['valor'] for f in fixos])
    total_variavel = variaveis['Valor'].sum() if not variaveis.empty else 0
    
    total_gastos = total_fixo + total_variavel
    total_rendas = salario + entregas + renda_extra_manual
    saldo_final = total_rendas - total_gastos
    

    # Lógica da Reserva de Emergência (Recuperada)
    valor_da_reserva = 0
    for item in fixos:
        if item['nome'] == 'Reserva':
            valor_da_reserva = item['valor']
            break
            
    meses_meta = 0
    if valor_da_reserva > 0:
        meses_meta = 10000 / valor_da_reserva

    # --- EXIBIÇÃO ---
    print("\n--- RELATÓRIO FINANCEIRO ---")
    print(f"Ganhos Totais (Salário + Extras): R$ {total_rendas:.2f}")
    print(f" - Entregas (App): R$ {entregas:.2f}")
    print(f" - Renda Extra Manual: R$ {renda_extra_manual:.2f}")
    print("-" * 30)
    print(f"Despesas Totais: R$ {total_gastos:.2f}")
    print(f" - Fixos: R$ {total_fixo:.2f}")
    print(f" - Variáveis: R$ {total_variavel:.2f}")
    print("-" * 30)
    print(f"SALDO FINAL: R$ {saldo_final:.2f}")

    # Exibe a meta da reserva se ela existir
    if valor_da_reserva > 0:
        print(f"\n[META] Aportando R$ {valor_da_reserva:.2f}/mês, você terá R$ 10k em {meses_meta:.1f} meses!")
    else:
        print("\n[DICA] Adicione um gasto fixo chamado 'Reserva' para calcular sua meta.")

    # Lógica de aviso
    if saldo_final < 0:
        print("\n[!!!] ATENÇÃO: SALDO NEGATIVO! CORTE GASTOS!")
    elif saldo_final < (salario * 0.1):
        print("\n[!] Cuidado: Você está poupando menos de 10% do salário.")
    else:
        print("\n[OK] Parabéns! Saúde financeira estável.")

def listar_fixos(lista_fixos):
    print("\n--- GASTOS FIXOS ---")
    for i, gasto in enumerate(lista_fixos):
        print(f"{i} - {gasto['nome']}: R$ {gasto['valor']:.2f}")

def menu_gerenciar_fixos():
    print("\n=== GESTÃO DE GASTOS FIXOS ===")
    print("1 - Adicionar | 2 - Remover | 3 - Alterar | 4 - Voltar")
    return input("Opção: ")