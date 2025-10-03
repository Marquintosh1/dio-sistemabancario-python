menu = """

[n] Novo Usuário
[lu] Lista Usuários
[lc] Lista Contas
[c] Nova Conta
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
usuarios = []
contas = []
AGENCIA = "0001"

def efetuar_saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return saldo, extrato

def efetuar_deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    # Verifica se já existe um usuário com esse CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\nOperação falhou! Já existe usuário com esse CPF.\n")
            return usuarios  # retorna sem alterações

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Cria o dicionário do usuário
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("\nUsuário criado com sucesso!\n")

    return usuarios

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    # Busca o usuário pelo CPF
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break

    if usuario:
        print("\nConta criada com sucesso!\n")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print("\nOperação falhou! Usuário não encontrado.\n")
    return None

def listar_usuarios(usuarios):
    if not usuarios:
        print("\nNão há usuários cadastrados.\n")
        return

    print("\n========== LISTA DE USUÁRIOS ==========")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereço: {usuario['endereco']}")
        print("----------------------------------------")

def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas.\n")
        return

    print("\n========== LISTA DE CONTAS ==========")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']} (CPF: {conta['usuario']['cpf']})")
        print("--------------------------------------")


while True:

    opcao = input(menu)

    if opcao == "n":
        usuarios = criar_usuario(usuarios)
        print (usuarios)
    elif opcao == "lu":
        listar_usuarios(usuarios)
    elif opcao == "lc":
        listar_contas(contas)
    elif opcao == "c":
        nova_conta = criar_conta(AGENCIA, len(contas)+1, usuarios)
        if nova_conta:
            contas.append(nova_conta)
    elif opcao == "d":
        saldo, extrato = efetuar_deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = efetuar_saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        saldo, extrato = exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")