eventos = []


def criar_evento():
    print("\n=== CRIAR EVENTO ===")

    nome = input("Nome: ")
    descricao = input("Descrição: ")
    local = input("Local: ")
    data = input("Data (DD/MM/AAAA): ")
    capacidade = int(input("Capacidade máxima: "))
    orcamento = float(input("Orçamento (€): ").replace(",", "."))

    evento = {
        "id": len(eventos) + 1,
        "nome": nome,
        "descricao": descricao,
        "local": local,
        "data": data,
        "capacidade": capacidade,
        "orcamento": orcamento
    }

    eventos.append(evento)

    print(f"\nEvento '{nome}' criado com sucesso!")




def menu():
    while True:
        print("\n=== GESTÃO DE FESTIVAIS ===")
        print("1 - Criar evento")
        print("2 - Consultar eventos")
        print("3 - Editar evento")
        print("4 - Eliminar evento")
        print("0 - Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            criar_evento()

        elif opcao == "2":
            print("Vamos implementar a consulta de eventos.")

        elif opcao == "3":
            print("Vamos implementar a edição de eventos.")

        elif opcao == "4":
            print("Vamos implementar a eliminação de eventos.")

        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida. Tenta novamente.")


if __name__ == "__main__":
    menu()