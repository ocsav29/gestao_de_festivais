from orcamento import consultar_orcamento
from fornecedores import registar_fornecedor
from dados import carregar_fornecedores, guardar_fornecedores
from despesas import registar_despesa
from eliminar_eventos import eliminar_evento
from criar_eventos import criar_evento
from dados import carregar_eventos, guardar_eventos
from participantes import registar_participante


eventos = carregar_eventos()
fornecedores = carregar_fornecedores()
def menu():
    while True:
        print("\n=== GESTÃO DE FESTIVAIS ===")
        print("1 - Criar evento")
        print("2 - Consultar eventos")
        print("3 - Editar evento")
        print("4 - Eliminar evento")
        print("5 - Registar despesa")
        print("6 - Registar fornecedor")
        print("7 - Consultar orçamento")
        print("8 - Registar participante")
        print("0 - Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            criar_evento(eventos)
            guardar_eventos(eventos)
        elif opcao == "2":
            print("Vamos implementar a consulta de eventos.")

        elif opcao == "3":
            print("Vamos implementar a edição de eventos.")

        elif opcao == "4":
            eliminar_evento(eventos)
            guardar_eventos(eventos)

        elif opcao == "5":
            registar_despesa(eventos)
            guardar_eventos(eventos)
        
        elif opcao == "6":
            registar_fornecedor(fornecedores)
            guardar_fornecedores(fornecedores)

        elif opcao == "7":
            consultar_orcamento(eventos)

        elif opcao == "8":
            registar_participante(eventos)
            guardar_eventos(eventos)

        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida. Tenta novamente.")


if __name__ == "__main__":
    menu()