"""
Módulo do resumo financeiro da aplicação Gestão de Festivais.

Para cada evento calcula o total de despesas, a receita dos bilhetes
e o lucro estimado (receita - despesas).

As despesas estão em evento["despesas"] (cada uma com a chave "valor").
As receitas vêm das vendas de bilhetes (chaves id_evento e total).
"""
from receita import calcular_receita_evento

def calcular_total_despesas(evento):
    """
    Soma o valor de todas as despesas de um evento.

    Parâmetros:
        evento (dict): o evento a analisar.

    Devolve:
        float: total das despesas (0.0 se o evento não tiver despesas).
    """
    total = 0.0

    # .get devolve uma lista vazia se o evento ainda não tiver despesas
    for despesa in evento.get("despesas", []):
        total += despesa["valor"]

    return total

def calcular_lucro(evento, bilhetes):
    """
    Calcula o lucro estimado de um evento: receita dos bilhetes - despesas.

    Parâmetros:
        evento (dict): o evento a analisar.
        bilhetes (list): lista de vendas de bilhetes.

    Devolve:
        float: lucro estimado (negativo se as despesas forem maiores).
    """
    receita = calcular_receita_evento(bilhetes, evento["id"])
    despesas = calcular_total_despesas(evento)

    return receita - despesas

# Este bloco só corre quando se executa este ficheiro diretamente
# (python resumo_financeiro.py). Serve apenas para testes.
if __name__ == "__main__":
    eventos_teste = [
        {
            "id": "teste1",
            "nome": "Festival de Verão",
            "data": "15/07/2027",
            "orcamento": 2000.0,
            "despesas": [
                {"categoria": "som", "descricao": "Aluguer de colunas", "valor": 300.0},
                {"categoria": "segurança", "descricao": "Seguranças", "valor": 150.5},
            ],
        },
        {
            "id": "teste2",
            "nome": "Noite de Jazz",
            "data": "10/08/2027",
            "orcamento": 800.0,
        },
    ]

    print("Despesas teste1:", calcular_total_despesas(eventos_teste[0]))
    print("Despesas teste2:", calcular_total_despesas(eventos_teste[1]))

    bilhetes_teste = [
        {"id_evento": "teste1", "quantidade": 40, "preco_unitario": 15.0, "total": 600.0},
        {"id_evento": "teste2", "quantidade": 2, "preco_unitario": 10.0, "total": 20.0},
    ]

    print("Lucro teste1:", calcular_lucro(eventos_teste[0], bilhetes_teste))
    print("Lucro teste2:", calcular_lucro(eventos_teste[1], bilhetes_teste))
    print("Lucro sem vendas:", calcular_lucro(eventos_teste[0], []))