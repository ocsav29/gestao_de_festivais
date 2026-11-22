
from orcamento import consultar_orcamento
from fornecedores import registar_fornecedor
from dados import carregar_fornecedores, guardar_fornecedores
from despesas import registar_despesa
from eliminar_eventos import eliminar_evento
from criar_eventos import criar_evento
from dados import carregar_eventos, guardar_eventos
from consultar_eventos import consultar_eventos
from editar_eventos import editar_evento
from participantes import registar_participante
from registar_bilhetes import registar_bilhetes
from receita import mostrar_receitas
from dados_bilhetes import carregar_bilhetes
from resumo_financeiro import mostrar_resumo_financeiro
from associar_fornecedores import associar_fornecedor, mostrar_fornecedores_eventos
from resumo_eventos import mostrar_resumo_evento

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
        print("9 - Registar bilhetes vendidos")
        print("10 - Consultar receita dos bilhetes")
        print("11 - Resumo financeiro (despesas, receitas e lucro)")
        print("12 - Associar fornecedor a evento")
        print("13 - Consultar fornecedores por evento")
        print("14 - Consultar resumo geral de um evento")
        print("0 - Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            criar_evento(eventos)
            guardar_eventos(eventos)

        elif opcao == "2":
            consultar_eventos(eventos)
        elif opcao == "3":
            editar_evento(eventos)
            guardar_eventos(eventos)

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

        elif opcao == "9":
            registar_bilhetes(eventos)

        elif opcao == "10":
            mostrar_receitas(eventos, carregar_bilhetes())
        
        elif opcao == "11":
            mostrar_resumo_financeiro(eventos, carregar_bilhetes())
            
        elif opcao == "12":
            associar_fornecedor(eventos, fornecedores)
            guardar_eventos(eventos)

        elif opcao == "13":
            mostrar_fornecedores_eventos(eventos, fornecedores)
        
        elif opcao == "14":
            mostrar_resumo_evento(eventos)
        
        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida. Tenta novamente.")


if __name__ == "__main__":
    menu()
