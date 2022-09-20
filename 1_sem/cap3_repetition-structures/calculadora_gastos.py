#1 - Usuário deve informar quantas transações financeiras realizou ao longo de um dia
#2 - Inserir o valor de cada uma
#3 - Exibir valor total gasto e média de transações
caixa = 0.0
gastos = 0.0
ganhos = 0.0
i = 0

transacoes = int(input("Insira o número de transações realizadas no dia: "))
print(transacoes)

while i < transacoes:
    tipo_de_transacao = int(input("Informe o tipo de transação, 1 - Ganho ou 2 - Gasto: "))
    valor = float(input("Informe o valor da transação: "))
    if tipo_de_transacao == 1:
          caixa = caixa + valor
          ganhos = ganhos + valor
    elif tipo_de_transacao == 2:
          caixa = caixa - valor
          gastos = gastos + valor
    i = i + 1

media = (ganhos + gastos)/transacoes
print("O valor total gasto foi de -R${}".format(gastos))
print("O quanto se tem no caixa é R${}".format(caixa))
print("O quanto se ganhou foi +R${}".format(ganhos))
print("A média de transações foi de R${}".format(media))