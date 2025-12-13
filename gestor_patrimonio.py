salario = float(input("Digite seu salário: "))

###Gastos fixos
gastos_fixos = [170, 985, 385, 250]
valor_fixo = sum(gastos_fixos)
nomes_fixos = ['Casa', 'Moto', 'Suhai', 'Reserva']

###Gastos variaveis
gastos_variaveis = []
nomes_variaveis = []

#Adiciona itens as listas
continuar = input('Deseja adicionar gasto? [S/N]: ').upper()

while continuar == 'S':
    item = input('Qual gasto a ser adicionado? (ex. Cartão, delivery, uber, etc.): ')
    valor = float(input(f"Quanto você gastou com {item}?: "))

    if valor > 0:
      gastos_variaveis.append(valor)
      nomes_variaveis.append(item)
    else:
        print('Valor incorreto!')

    continuar = input('Adicionar outro gasto? [S/N]: ').upper()
valor_variavel = sum(gastos_variaveis)
###Objetivo reserva de emergencia
reserva_emergenciaMeta = 10000 / gastos_fixos[3]

###Total de gastos e valor que sobra do salario
total_gastos = sum(gastos_fixos + gastos_variaveis)
saldo_final = salario - total_gastos

print (f'O valor total das despesas é: {total_gastos}')
print (f'O valor que sobra depois de pagar as contas é: {saldo_final}')

print(f"Relatório: R$ {valor_fixo:.2f} Fixos + R$ {valor_variavel:.2f} Variáveis")
print(f"Total Geral: R$ {total_gastos:.2f}\n")

print (f'Para atingir a meta da reserva de emergencia, levará {reserva_emergenciaMeta} meses!\n')

#logica de decisão
if saldo_final < 0:
    print ("!!!Atenção!!! \nSALDO NEGATIVO, CORTE GASTOS E AUMENTE A RENDA")
elif saldo_final < salario*0.10:
    print ("!Cuidado! \nAumente a renda para que tenha sobra do salario")
else:
    print ("Parabéns!!\nA saúde financeira está indo bem!")

