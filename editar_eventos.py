"""
Módulo de edição de eventos da aplicação Gestão de Festivais.

Permite alterar os dados de um evento que já existe.
Cada evento é um dicionário com as chaves:
id, nome, descricao, local, data, capacidade e orcamento.
"""


def procurar_evento_por_id(eventos, id_evento):
    """
    Procura um evento na lista pelo seu id.

    Parâmetros:
        eventos (list): lista de dicionários com os eventos.
        id_evento (int): id do evento a procurar.

    Devolve:
        dict: o evento encontrado, ou None se não existir.
    """
    # Percorre os eventos um a um até encontrar o id pedido
    for evento in eventos:
        if evento["id"] == id_evento:
            return evento

    # Se chegou aqui, nenhum evento tem esse id
    return None


def pedir_texto(campo, valor_atual):
    """
    Pede um novo valor para um campo de texto (nome, descrição ou local).

    Se o utilizador carregar só em Enter, mantém o valor atual.
    Assim o campo nunca fica vazio.

    Parâmetros:
        campo (str): nome do campo mostrado ao utilizador (ex.: "Nome").
        valor_atual (str): valor que o evento tem agora.

    Devolve:
        str: o novo texto, ou o valor atual se o utilizador não escrever nada.
    """
    # Mostra o valor atual entre [ ] para o utilizador saber o que lá está
    novo = input(f"{campo} [{valor_atual}]: ").strip()

    # Enter sem escrever nada (ou só espaços) = manter o valor antigo
    if novo == "":
        return valor_atual

    return novo


# Este bloco só corre quando se executa este ficheiro diretamente
# (python editar_eventos.py). Serve apenas para testes.
if __name__ == "__main__":
    eventos_teste = [
        {
            "id": 1,
            "nome": "Festival de Verão",
            "descricao": "Música ao ar livre",
            "local": "Faro",
            "data": "15/07/2027",
            "capacidade": 500,
            "orcamento": 2000.0,
        },
        {
            "id": 2,
            "nome": "Noite de Jazz",
            "descricao": "Concerto de jazz",
            "local": "Lagos",
            "data": "10/08/2027",
            "capacidade": 150,
            "orcamento": 800.0,
        },
    ]

    print(procurar_evento_por_id(eventos_teste, 1))
    print(procurar_evento_por_id(eventos_teste, 99))

    novo_nome = pedir_texto("Nome", "Festival de Verão")
    print("Resultado:", novo_nome)
