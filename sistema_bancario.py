saldo_conta_bancaria = 0
limite_saque_diario = 3
depositos_realizados = []
saque_realizados = []

def depositar():
    global saldo_conta_bancaria
    depositando = True

    while depositando == True:
        deposito = float(input("Qual valor você quer depositar?\n"))
        if deposito > 0:
            depositos_realizados.append(deposito)
            saldo_conta_bancaria += (deposito)
            print("Depósito realizado. Retornando ao menu inicial.")
            return menu_inicial()
        
        else:
            print("Por favor, digite um valor superior a 0.")

def sacar():
    global saldo_conta_bancaria
    global limite_saque_diario
    limite_valor_por_saque = 500

    saque = float(input("Qual valor você quer sacar?\n"))
    
    if saque <= saldo_conta_bancaria:

        if limite_saque_diario > 0:

            if saque <= limite_valor_por_saque:
                saque_realizados.append(saque)
                saldo_conta_bancaria -= (saque)
                limite_saque_diario -= 1
                print("Saque realizado. Retornando ao menu inicial.")
                return menu_inicial()
            else:
                print("Você digitou um valor superior ao valor limite por saque. Digite novamente.")
                sacar()

        else:
            print("Você atingiu o limite de saque diário. Retornando ao menu inicial.")
            menu_inicial()
    else:
        nova_tentativa = int(input("Você não possui saldo suficiente na conta. Deseja tentar novamente? 1 - SIM | 0 - NÃO \n"))
        if nova_tentativa == 1:
            sacar()
        else:
            menu_inicial()

def extrato():
    global saldo_conta_bancaria
    print(" EXTRATO ".center(50, "="))
    print("Depósitos: \n")
    for valor in depositos_realizados:
        print(f"+ R$ {valor:.2f}")

    print("\nSaques: \n")
    for valor in saque_realizados:
        print(f"+ R$ {valor:.2f}")

    print(f"\nTotal disponível na conta: R$ {saldo_conta_bancaria:.2f}")

    print("="*50)

    proxima_acao_usuario = int(input("Deseja realizar uma nova operação? 1 - SIM | 0 - NÃO \n"))
    if proxima_acao_usuario == 1:
            menu_inicial()
    else:
        print("Agradecemos por utilizar os nossos serviços. Atendimento encerrado.") 

def menu_inicial():
    operacao_solicitada = float(input(f'''
    {"#"*54}

    Para iniciar digite o número da operação desejada:

    1 - Depósito
    2 - Saque
    3 - Extrato
    0 - Sair

    {"#"*54} 

    '''))
    
    if operacao_solicitada == 1:
        return depositar()
    
    elif operacao_solicitada == 2:
        return sacar()
    
    elif operacao_solicitada == 3:
        return extrato()
    
    elif operacao_solicitada == 0:
        print("Agradecemos por utilizar os nossos serviços. Atendimento encerrado.")

menu_inicial()
