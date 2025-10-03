menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao= input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo +=valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso")
        else:
            print("OPERAÇÃO FALHOU! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques>= LIMITE_SAQUES
        if excedeu_saldo:
            print("OPERAÇÃO FALHOU! Você não tem saldo suficiente!")
        elif excedeu_limite:
            print("OPERAÇÃO FALHOU! O valor do saldo excede o limite!")
        elif excedeu_saques:
            print("OPERAÇÃO FALHOU! Número máximo de saques excedidos!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("OPERAÇÃO FALHOU! O valor informado é inválido!")
    

    elif opcao == "e":
        print("\n==========EXTRATO==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
    elif opcao == "q":
        break
    else:
        print("OPERAÇÃO INVÁLIDA. Selecione novamente a operação desejada.")