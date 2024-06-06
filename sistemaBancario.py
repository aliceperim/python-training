menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
ext = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            ext += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            ext += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
