menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limit = 500
extract = ""
number_serves = 0
LIMIT_SERVES = 3

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Informe o valor do depósito: "))

        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif option == "s":
        value = float(input("Informe o valor do saque: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_verves = number_serves >= LIMIT_SERVES

        if exceeded_balance:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif exceeded_limit:
            print("Operação falhou! O valor do saque excede o limite.")

        elif exceeded_verves:
            print("Operação falhou! Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            extract += f"Saque: R$ {value:.2f}\n"
            number_serves += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif option == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extract else extract)
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")