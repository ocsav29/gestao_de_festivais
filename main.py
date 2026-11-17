from criar_eventos import criar_evento
from dados import carregar_eventos, guardar_eventos
from consultar_eventos import consultar_eventos

eventos = carregar_eventos()

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
            criar_evento(eventos)
            guardar_eventos(eventos)
        elif opcao == "2":
            consultar_eventos(eventos)
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