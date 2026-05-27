def exibir_menu_principal():
    print("\n=== Bem vindo ao gestor financeiro! ===\n")
    print("1 - Relatório")
    print("2 - Adicionar renda extra")
    print("3 - Gerenciar gastos fixos")
    print("4 - Gerenciar Gastos Variáveis")
    print("5 - Sair")
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

def mostrar_relatorio_final(resumo):

    print("\n--- RELATÓRIO FINANCEIRO ---")
    print(f" - Entregas (App): R$ {resumo['entregas']:.2f}")
    print(f" - Renda Extra Manual: R$ {resumo['renda_extra_manual']:.2f}")
    print(f"Ganhos Totais (Salário + Extras): R$ {resumo['total_rendas']:.2f}")

    print("-" * 30)

    print(f" - Fixos: R$ {resumo['total_gasto_fixo']:.2f}")
    print(f" - Variáveis: R$ {resumo['total_gasto_variavel']:.2f}")
    print(f"Despesas Totais: R$ {resumo['total_gastos']:.2f}")

    print("-" * 30)

    print(f"SALDO FINAL: R$ {resumo['saldo_final']:.2f}")

    # mensagem de status de meta da reserva de emergencia
    print(resumo['mensagem_meta'])

    # mensagem de aviso de saldo
    print(resumo['aviso_saldo'])

def listar_fixos(lista_fixos):
    print("\n--- GASTOS FIXOS ---")
    for i, gasto in enumerate(lista_fixos):
        print(f"{i} - {gasto['nome']}: R$ {gasto['valor']:.2f}")

def menu_gerenciar_fixos():
    print("\n=== GESTÃO DE GASTOS FIXOS ===")
    print("1 - Adicionar | 2 - Remover | 3 - Alterar | 4 - Consultar | 5 - Voltar")
    return input("Opção: ")

def menu_gerenciar_variaveis():
    print("\n=== GESTÃO DE GASTOS VARIAVEIS ===")
    print("1 - Adicionar | 2 - Remover | 3 - Alterar | 4 - Consultar | 5 - Voltar")
    return input("Opção: ")