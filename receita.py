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

def mostrar_receitas(eventos, bilhetes):
    """
    Mostra os bilhetes vendidos e a receita de cada evento, e a receita total.

    Parâmetros:
        eventos (list): lista de dicionários com os eventos.
        bilhetes (list): lista de vendas de bilhetes.
    """
    print("\n=== RECEITA DOS BILHETES ===")

    if not eventos:
        print("Ainda não existem eventos registados.")
        return

    for evento in eventos:
        quantidade = contar_bilhetes_evento(bilhetes, evento["id"])
        receita = calcular_receita_evento(bilhetes, evento["id"])

        # :.2f mostra sempre 2 casas decimais (ex.: 37.50)
        print(f"{evento['nome']} ({evento['data']}): "
              f"{quantidade} bilhetes | {receita:.2f} €")

    print(f"\nReceita total: {calcular_receita_total(bilhetes):.2f} €")

# Este bloco só corre quando se executa este ficheiro diretamente
# (python receita.py). Serve apenas para testes.
if __name__ == "__main__":
    bilhetes_teste = [
        {"id_evento": "teste1", "quantidade": 10, "preco_unitario": 15.0, "total": 150.0},
        {"id_evento": "teste1", "quantidade": 5, "preco_unitario": 20.0, "total": 100.0},
        {"id_evento": "teste2", "quantidade": 3, "preco_unitario": 12.5, "total": 37.5},
    ]

    eventos_teste = [
        {"id": "teste1", "nome": "Festival de Verão", "data": "15/07/2027"},
        {"id": "teste2", "nome": "Noite de Jazz", "data": "10/08/2027"},
        {"id": "teste3", "nome": "Feira Medieval", "data": "05/09/2027"},
    ]

    mostrar_receitas(eventos_teste, bilhetes_teste)
    mostrar_receitas([], bilhetes_teste)