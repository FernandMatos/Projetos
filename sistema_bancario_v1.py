from datetime import datetime

saldo_conta_bancaria = 0
limite_saque_diario = 3
limite_transacoes_diario = 10
entrada_extrato = []

def depositar():
    global saldo_conta_bancaria
    while True:
        try:
            deposito = float(input("Qual valor você quer depositar?\n"))
            if deposito > 0:
                data_hora = datetime.now()
                entrada_extrato.append(f'{data_hora} | Depósito: + R$ {deposito:.2f}')
                saldo_conta_bancaria += deposito
                print("Depósito realizado.")
                break
            else:
                print("Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def sacar():
    global saldo_conta_bancaria, limite_saque_diario
    limite_valor_por_saque = 500
    if limite_saque_diario == 0:
        print("Limite diário de saques atingido.")
        return

    try:
        saque = float(input("Qual valor você quer sacar?\n"))
        if 0 < saque <= limite_valor_por_saque and saque <= saldo_conta_bancaria:
            data_hora = datetime.now()
            entrada_extrato.append(f'{data_hora} | Saque: - R$ {saque:.2f}')
            saldo_conta_bancaria -= saque
            limite_saque_diario -= 1
            print("Saque realizado.")
        else:
            print("Valor inválido ou saldo insuficiente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def ver_extrato():
    print("\n--- Extrato ---")
    for linha in entrada_extrato:
        print(linha)
    print(f"Saldo atual: R$ {saldo_conta_bancaria:.2f}")
    print("--------------")

def menu_inicial():
    while True:
        print("\n[1] Depositar\n[2] Sacar\n[3] Ver Extrato\n[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            depositar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            ver_extrato()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

menu_inicial()
