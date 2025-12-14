salario = float(input("Digite seu salário: "))

###Gastos fixos
gastos_fixos = [
                 {'nome': 'Casa', 'valor': 170},
                 {'nome': 'Moto', 'valor': 985},
                 {'nome': 'Suhai', 'valor': 385},
                 {'nome': 'Reserva', 'valor': 250}
                ]
total_fixo = 0

###Gastos variaveis
gastos_variaveis = []
total_variavel = 0

#Adiciona itens as listas
continuar = input('Deseja adicionar gasto? [S/N]: ').upper()

while continuar == 'S':
    item = input('Qual gasto a ser adicionado? (ex. Cartão, delivery, uber, etc.): ')
    valor_variavel = float(input(f"Quanto você gastou com {item}?: "))

    if valor_variavel > 0:
      novo_gasto = {
          'nome': item, 
          'valor': valor_variavel
      }
      gastos_variaveis.append(novo_gasto)
    else:
        print('Valor incorreto!')

    continuar = input('Adicionar outro gasto? [S/N]: ').upper()

#Somos dos valores presentes nos dicionarios
for item in gastos_fixos:
    total_fixo = total_fixo + item['valor']

for item in gastos_variaveis:
    total_variavel = total_variavel + item['valor']

###Objetivo reserva de emergencia
reserva_emergencia_meta = 10000 / gastos_fixos[3]['valor']

###Total de gastos e valor que sobra do salario

total_gastos = (total_fixo + total_variavel)
saldo_final = salario - total_gastos

print (f'O valor total das despesas é: {total_gastos}')
print (f'O valor que sobra depois de pagar as contas é: {saldo_final}')

print(f"Relatório: R$ {total_fixo:.2f} Fixos + R$ {total_variavel:.2f} Variáveis")
print(f"Total Geral: R$ {total_gastos:.2f}\n")

print (f'Para atingir a meta da reserva de emergencia, levará {reserva_emergencia_meta} meses!\n')

#logica de decisão
if saldo_final < 0:
    print ("!!!Atenção!!! \nSALDO NEGATIVO, CORTE GASTOS E AUMENTE A RENDA")
elif saldo_final < salario*0.10:
    print ("!Cuidado! \nAumente a renda para que tenha sobra do salario")
else:
    print ("Parabéns!!\nA saúde financeira está indo bem!")

