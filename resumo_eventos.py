
from participantes import escolher_evento, contar_participantes, lugares_disponiveis
from receita import contar_bilhetes_evento, calcular_receita_evento
from dados_bilhetes import carregar_bilhetes
from resumo_financeiro import calcular_total_despesas, calcular_lucro


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
        
    bilhetes = carregar_bilhetes()

    quantidade_vendida = contar_bilhetes_evento(bilhetes, evento["id"])
    receita = calcular_receita_evento(bilhetes, evento["id"])

    print("\n=== BILHETES E RECEITAS ===")
    print(f"Bilhetes vendidos: {quantidade_vendida}")
    print(f"Receita dos bilhetes: {receita:.2f} €")
        
    despesas = calcular_total_despesas(evento)
    lucro = calcular_lucro(evento, bilhetes)

    print("\n=== INDICADORES FINANCEIROS ===")
    print(f"Orçamento: {evento['orcamento']:.2f} €")
    print(f"Despesas: {despesas:.2f} €")
    print(f"Lucro estimado: {lucro:.2f} €")
        
    participantes = contar_participantes(evento)
    lugares = lugares_disponiveis(evento)

    print("\n=== PARTICIPAÇÃO ===")
    print(f"Participantes inscritos: {participantes}")
    print(f"Capacidade máxima: {evento['capacidade']}")
    print(f"Lugares disponíveis: {lugares}")
        
    fornecedores = evento.get("fornecedores", [])

    print("\n=== FORNECEDORES ===")
    print(f"Fornecedores associados: {len(fornecedores)}")