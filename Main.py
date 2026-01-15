from src import database as db
from src import interface as ui

#Carregamento Inicial de Dados
gastos_fixos = db.carregar_gastos_fixos()

#Input Inicial
salario = ui.ler_valor("Digite seu salário mensal: ")

# 3. Loop Principal
while True:
    opcao = ui.exibir_menu_principal()

    if opcao == '1': # Adicionar Gasto Variável
        item, valor, categoria = ui.formulario_novo_gasto()
        if valor > 0:
            db.salvar_novo_gasto(item, valor, categoria)
            print("Gasto salvo com sucesso!")

    elif opcao == '2': # Relatório
        # pede os dados pro Banco..
        df_variaveis = db.ler_todos_gastos()
        df_extras = db.ler_todas_entradas()
        valor_entregas = db.buscar_renda_entregas() # Busca do Google Sheets
        
        # Calcula totais simples
        total_extras_manual = df_extras['Valor'].sum() if not df_extras.empty else 0

        # manda a Interface mostrar
        ui.mostrar_relatorio_final(
            gastos_fixos, 
            df_variaveis, 
            valor_entregas, 
            total_extras_manual, 
            salario
        )

    elif opcao == '3': # Renda Extra
        item, valor, origem = ui.formulario_nova_renda()
        if origem == 'ENTREGAS':
            print("Aviso: Entregas devem ser geridas na planilha do Google.")
        elif valor > 0:
            db.salvar_nova_renda(item, valor, origem)
            print("Renda extra salva!")

    elif opcao == '4': # Gerenciar Fixos
        sub_opcao = ui.menu_gerenciar_fixos()
        
        if sub_opcao == '1': # Adicionar
            item = ui.ler_texto("Nome do gasto fixo: ")
            valor = ui.ler_valor("Valor: ")
            gastos_fixos.append({'nome': item, 'valor': valor})
            db.salvar_gastos_fixos(gastos_fixos)
            
        elif sub_opcao == '2': # Remover
            ui.listar_fixos(gastos_fixos)
            indice = int(ui.ler_valor("Número para remover: "))
            try:
                gastos_fixos.pop(indice)
                db.salvar_gastos_fixos(gastos_fixos)
                print("Removido!")
            except:
                print("Erro: Índice inválido.")

        elif sub_opcao == '3':
            ui.listar_fixos(gastos_fixos)

            try:
                indice = int(ui.ler_valor("Número para alterar: "))

                #Validação de segurança: O índice existe na lista?
                if 0 <= indice < len(gastos_fixos):
                    #Pede os novos dados
                    print(f"Alterando: {gastos_fixos[indice]['nome']}") # Mostra o que está sendo mudado
                    novo_nome = ui.ler_texto("Novo nome: ")
                    novo_valor = ui.ler_valor("Novo valor: ")
                    
                    #Atualiza a lista na posição específica
                    gastos_fixos[indice] = {'nome': novo_nome, 'valor': novo_valor}
                    
                    #Salva no banco
                    db.salvar_gastos_fixos(gastos_fixos)
                    print("Gasto atualizado com sucesso!")
                    
                else:
                    print("Erro: Número não encontrado na lista.")
                
            except:
                print("Erro: Digite um número válido.")

        elif sub_opcao == '4': # Consultar Fixos
            ui.listar_fixos(gastos_fixos)

    elif opcao == '5':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")