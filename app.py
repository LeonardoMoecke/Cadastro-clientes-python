clientes = []

while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        clientes.append(nome)
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        print("\nClientes cadastrados:")
        for c in clientes:
            print("-", c)

    elif opcao == "3":
        break

    else:
        print("Opção inválida!")
