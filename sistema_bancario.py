from datetime import datetime

usuarios_cadastrados = {}  # cpf: {dados do usuário}
contas_cadastradas = {}    # cpf: {"Ag": agencia, "Conta": numero}
saldos = {}                # cpf: saldo individual
extratos = {}              # cpf: lista de transações
AGENCIA_PADRAO = "0001"


def criar_usuario():
    nome_usuario = input("Nome completo: ").upper()
    data_nascimento = input("Data de nascimento: ")
    cpf = int(input("Digite CPF (somente números): "))
    logradouro = input("Logradouro (ex: Rua 123, Av. Brasil): ")
    numero_residencial = int(input("N° da residência: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade (ex: São Paulo): ")
    estado = input("Estado (ex: SP): ")
    endereco_completo = f'{logradouro}, n° {numero_residencial} – {bairro} – {cidade}/{estado}'.upper()
    usuario = {cpf: {'nome': nome_usuario, 'nascimento': data_nascimento, 'endereco': endereco_completo}}

    return usuario

def criar_conta(cpf_usuario):
    if cpf_usuario in usuarios_cadastrados:
        numero_conta = len(contas_cadastradas) + 1 if len(contas_cadastradas) > 0 else 1
        contas_cadastradas[cpf_usuario] = {"Ag": AGENCIA_PADRAO, "Conta": numero_conta}
        saldos[cpf_usuario] = 0
        extratos[cpf_usuario] = []
        print("Conta cadastrada com sucesso.")

    else:
        print("Esse usuário não foi cadastrado ou o CPF foi digitado incorretamente.")


def depositar(cpf_usuario):
    if cpf_usuario in contas_cadastradas:
        while True:
            try:
                valor = float(input("Qual valor você quer depositar?\n"))            
                if valor > 0:
                    data_hora = datetime.now()
                    saldos[cpf_usuario] += valor
                    extratos[cpf_usuario].append(f"{data_hora} | Depósito: + R$ {valor:.2f}")
                    print("Depósito realizado.")
                    return
                else:
                    print("Por favor, digite um valor superior a 0.")

            except ValueError:
                print("Entrada inválida.")
    else:
        print("CPF inválido ou conta não encontrada.")
        
def sacar(cpf_usuario):

    limite_valor_por_saque = 500

    if cpf_usuario in contas_cadastradas:
        try:
            valor = float(input("Qual valor você quer sacar?\n"))
        except ValueError:
            print("Valor inválido.")
            return
        
        if valor > saldos[cpf_usuario]:
            print("Saldo insuficiente.")
        
        elif valor > limite_valor_por_saque:
            print("Valor acima do limite permitido por saque.")
        else:
            data_hora = datetime.now()
            saldos[cpf_usuario] -= valor
            extratos[cpf_usuario].append(f'{data_hora} | Saque: - R$ {valor:.2f}')
            print("Saque realizado.")
    else:
        print("CPF inválido ou conta não encontrada.")

def extrato(cpf_usuario):

    print(" EXTRATO ".center(50, "="))
    if cpf_usuario not in extratos or not extratos[cpf_usuario]:
        print("Nenhuma movimentação realizada.")

    else:   
        for transacao in extratos[cpf_usuario]:
                print(transacao)

    print(f"\nTotal disponível na conta: R$ {saldos.get(cpf_usuario, 0):.2f}")

    print("="*50)

def verifica_transacoes_diarias(cpf_usuario, eh_saque):
    hoje = datetime.now().date()
    if cpf_usuario not in extratos:
        return True

    ultimas_transacoes = extratos[cpf_usuario][-10:]
    contador_saques = 0
    contador_geral = 0

    for transacao in ultimas_transacoes:
        data_str = transacao.split(" | ")[0]
        data = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S.%f").date()

        if data == hoje:
            contador_geral += 1
            if eh_saque and "saque" in transacao.lower():
                contador_saques += 1

    if contador_saques >= 3:
        print("Você atingiu o limite de 3 saques diários.")
        return False

    if contador_geral >= 10:
        print("Você atingiu o limite de 10 transações diárias.")
        return False

    return True

def listar_contas():

    print(" CONTAS CADASTRADAS ".center(50, "="))
    if not contas_cadastradas:
        print("Nenhuma conta cadastrada.")

    else:   
        for cpf, dados in contas_cadastradas.items():
            print(f"CPF: {cpf}, Dados: {dados}")

    print("="*50)

def menu_inicial():
    cpf_usuario = int(input("Digite seu CPF: "))

    while True:
        try:
            operacao_solicitada = float(input(f'''
            {"#"*54}

            Para iniciar digite o número da operação desejada:

            1 - Depósito
            2 - Saque
            3 - Extrato
            4 - Criar Usuário
            5 - Criar Conta
            6 - Listar Contas
            0 - Sair

            {"#"*54} 

            '''))
            
            if operacao_solicitada == 1:
                if verifica_transacoes_diarias(cpf_usuario,False):
                    depositar(cpf_usuario)    
            
            elif operacao_solicitada == 2:
                if verifica_transacoes_diarias(cpf_usuario, True):
                    sacar(cpf_usuario) 
            
            elif operacao_solicitada == 3:
                extrato(cpf_usuario)

            elif operacao_solicitada == 4:
                usuarios_cadastrados.update(criar_usuario())

            elif operacao_solicitada == 5:
                criar_conta(cpf_usuario)

            elif operacao_solicitada == 6:
                listar_contas()
            
            elif operacao_solicitada == 0:
                print("Agradecemos por utilizar os nossos serviços. Atendimento encerrado.")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite uma opção válida (1, 2, 3, 4, 5, 6 ou 0).")

menu_inicial()