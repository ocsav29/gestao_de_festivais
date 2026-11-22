
from participantes import escolher_evento


def mostrar_resumo_evento(eventos):
    """
    Permite selecionar um evento para consultar o seu resumo geral.

    Parâmetros:
        eventos (list): lista dos eventos registados.
    """
    print("\n=== RESUMO GERAL DE EVENTOS ===")

    if not eventos:
        print("Ainda não existem eventos registados.")
        return

    print("\nEscolhe o evento:")
    evento = escolher_evento(eventos)

    if evento is None:
        return

    print(f"\nEvento selecionado: {evento['nome']}")
    print("\n=== INFORMAÇÕES DO EVENTO ===")
    print(f"Nome: {evento['nome']}")
    print(f"Descrição: {evento['descricao']}")
    print(f"Local: {evento['local']}")
    print(f"Data: {evento['data']}")
    print(f"Capacidade: {evento['capacidade']} pessoas")
    print(f"Orçamento: {evento['orcamento']:.2f} €")