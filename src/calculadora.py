def gerar_resumo_financeiro (fixos, variaveis, entregas, renda_extra_manual, salario):
    total_gasto_fixo = sum([f['valor'] for f in fixos])
    total_gasto_variavel = variaveis['Valor'].sum() if not variaveis.empty else 0
    
    total_gastos = total_gasto_fixo + total_gasto_variavel
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

    # logica da meta
    if valor_da_reserva > 0:
        mensagem_meta = (f"\n[META] Aportando R$ {valor_da_reserva:.2f}/mês, você terá R$ 10k em {meses_meta:.1f} meses!")
    else:
        mensagem_meta = ("\n[DICA] Adicione um gasto fixo chamado 'Reserva' para calcular sua meta.")

    # Lógica de aviso
    if saldo_final < 0:
        aviso_saldo = ("\n[!!!] ATENÇÃO: SALDO NEGATIVO! CORTE GASTOS!")

    elif saldo_final < (salario * 0.1):
        aviso_saldo = ("\n[!] Cuidado: Você está poupando menos de 10% do salário.")
    
    else:
        aviso_saldo = ("\n[OK] Parabéns! Saúde financeira estável.")

    return {
        "salario": salario,
        "renda_extra_manual": renda_extra_manual,
        "entregas": entregas,
        "total_gastos": total_gastos,
        "total_rendas": total_rendas,
        "total_gasto_fixo": total_gasto_fixo,
        "total_gasto_variavel": total_gasto_variavel,
        "saldo_final": saldo_final,
        "valor_da_reserva": valor_da_reserva,
        "meses_meta": meses_meta,
        "mensagem_meta": mensagem_meta,
        "aviso_saldo": aviso_saldo
        }