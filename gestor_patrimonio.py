salario = float(input("Digite seu salário: "))

###Gastos fixos
gasto_casa = 170
gasto_moto = 985
gasto_seguroMoto = 385
reserva_emergencia = 250
gastos_fixos = gasto_casa + gasto_moto + gasto_seguroMoto + reserva_emergencia
###Gastos variaveis
gasto_cartaoCredito = float(input("Digite gasto de cartão: "))
gasto_lazer = float(input("Digite gasto lazer: "))   
gastos_variaveis =  gasto_cartaoCredito + gasto_lazer

###Objetivo reserva de emergencia
reserva_emergenciaMeta = 10000 / 250

###Total de gastos e valor que sobra do salario
total_gastos = gastos_fixos + gastos_variaveis
saldo_final = salario - total_gastos

print (f'O valor total das despesas é: {total_gastos}')
print (f'O valor que sobra depois de pagar as contas é: {saldo_final}')

print (f'PAra atingir a meta da reserva de emergencia, levará {reserva_emergenciaMeta} meses')


