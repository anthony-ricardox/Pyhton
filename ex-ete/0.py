while True:
    print("\nEscolha uma opção:")
    print("1 - Dizer Olá")
    print("2 - Mostrar número")
    print("0 - Sair")

    opcao = int(input("Digite: "))

    match opcao:
        case 1:
            print("Olá!")
        case 2:
            print("Número: 42")
        case 0:
            print("Saindo...")
            break
        case _:
            print("Opção inválida")