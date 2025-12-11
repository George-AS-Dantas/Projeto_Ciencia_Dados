salario = float(input("Digite seu salário: "))

###Gastos fixos
gastos = [170, 985, 385, 250]
gastos_soma = sum(gastos)
lista_gastos = ['Casa', 'Moto', 'Suhai', 'Reserva']

###Gastos variaveis
perguntas = ['Cartão', 'Lazer', 'Mercado', 'Gasolina', 'Roupa']  

#Adiciona itens as listas
for item in perguntas:
    valor = float(input(f"Quanto você gastou com {item}? "))
    
    gastos.append(valor)
    lista_gastos.append(item)
###Objetivo reserva de emergencia
reserva_emergenciaMeta = 10000 / gastos[3]

###Total de gastos e valor que sobra do salario
total_gastos = sum(gastos)
saldo_final = salario - total_gastos

print (f'O valor total das despesas é: {total_gastos}, sendo que {gastos_soma} foram gastos fixos.')
print (f'O valor que sobra depois de pagar as contas é: {saldo_final}')

print (f'Para atingir a meta da reserva de emergencia, levará {reserva_emergenciaMeta} meses')

#logica de decisão
if saldo_final < 0:
    print ("!!!Atenção!!! \nSALDO NEGATIVO, CORTE GASTOS E AUMENTE A RENDA")
elif saldo_final < salario*0.10:
    print ("!Cuidado! \nAumente a renda para que tenha sobra do salario")
else:
    print ("Parabéns!!\n A saúde financeira está indo bem!")

