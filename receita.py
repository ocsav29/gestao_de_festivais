"""
Módulo de cálculo da receita dos bilhetes da aplicação Gestão de Festivais.

Usa as vendas de bilhetes registadas (lista de dicionários com as chaves
id_evento, quantidade, preco_unitario e total) para calcular a receita
de cada evento e a receita total.
"""


def calcular_receita_evento(bilhetes, id_evento):
    """
    Soma o valor de todas as vendas de bilhetes de um evento.

    Parâmetros:
        bilhetes (list): lista de vendas de bilhetes.
        id_evento (str): id do evento.

    Devolve:
        float: receita total desse evento (0.0 se não houver vendas).
    """
    receita = 0.0

    # Percorre as vendas e soma só as que pertencem a este evento
    for venda in bilhetes:
        if venda["id_evento"] == id_evento:
            receita += venda["total"]

    return receita

def contar_bilhetes_evento(bilhetes, id_evento):
    """
    Soma a quantidade de bilhetes vendidos de um evento.

    Parâmetros:
        bilhetes (list): lista de vendas de bilhetes.
        id_evento (str): id do evento.

    Devolve:
        int: número de bilhetes vendidos (0 se não houver vendas).
    """
    quantidade = 0

    for venda in bilhetes:
        if venda["id_evento"] == id_evento:
            quantidade += venda["quantidade"]

    return quantidade


def calcular_receita_total(bilhetes):
    """
    Soma o valor de todas as vendas de bilhetes, de todos os eventos.

    Parâmetros:
        bilhetes (list): lista de vendas de bilhetes.

    Devolve:
        float: receita total (0.0 se não houver vendas).
    """
    receita = 0.0

    for venda in bilhetes:
        receita += venda["total"]

    return receita

# Este bloco só corre quando se executa este ficheiro diretamente
# (python receita.py). Serve apenas para testes.
if __name__ == "__main__":
    bilhetes_teste = [
        {"id_evento": "teste1", "quantidade": 10, "preco_unitario": 15.0, "total": 150.0},
        {"id_evento": "teste1", "quantidade": 5, "preco_unitario": 20.0, "total": 100.0},
        {"id_evento": "teste2", "quantidade": 3, "preco_unitario": 12.5, "total": 37.5},
    ]

    print("Receita teste1:", calcular_receita_evento(bilhetes_teste, "teste1"))
    print("Receita teste2:", calcular_receita_evento(bilhetes_teste, "teste2"))
    print("Receita evento sem vendas:", calcular_receita_evento(bilhetes_teste, "outro"))

    print("Bilhetes teste1:", contar_bilhetes_evento(bilhetes_teste, "teste1"))
    print("Receita total:", calcular_receita_total(bilhetes_teste))
    print("Receita total sem vendas:", calcular_receita_total([]))