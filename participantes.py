"""
Módulo de registo de participantes da aplicação Gestão de Festivais.

Os participantes ficam guardados dentro de cada evento,
na lista evento["participantes"]. Cada participante tem:
id, nome e contacto.
"""


def escolher_evento(eventos):
    """
    Mostra os eventos numerados e pede ao utilizador para escolher um.

    Parâmetros:
        eventos (list): lista de dicionários com os eventos.

    Devolve:
        dict: o evento escolhido, ou None se cancelar ou a escolha for inválida.
    """
    # Mostra os eventos numerados (1, 2, 3...)
    for numero, evento in enumerate(eventos, start=1):
        print(f"{numero} - {evento['nome']} ({evento['data']})")

    print("0 - Cancelar")

    try:
        escolha = int(input("\nNúmero do evento: ").strip())
    except ValueError:
        print("Número inválido. Tem de ser um número.")
        return None

    if escolha == 0:
        print("Operação cancelada.")
        return None

    # O número tem de corresponder a um evento da lista
    if escolha < 1 or escolha > len(eventos):
        print("Não existe nenhum evento com esse número.")
        return None

    # A lista começa na posição 0, por isso subtrai-se 1
    return eventos[escolha - 1]


# Este bloco só corre quando se executa este ficheiro diretamente
# (python participantes.py). Serve apenas para testes.
if __name__ == "__main__":
    eventos_teste = [
        {
            "id": "teste1",
            "nome": "Festival de Verão",
            "descricao": "Música ao ar livre",
            "local": "Faro",
            "data": "15/07/2027",
            "capacidade": 3,
            "orcamento": 2000.0,
        },
        {
            "id": "teste2",
            "nome": "Noite de Jazz",
            "descricao": "Concerto de jazz",
            "local": "Lagos",
            "data": "10/08/2027",
            "capacidade": 150,
            "orcamento": 800.0,
        },
    ]

    evento = escolher_evento(eventos_teste)
    print("Escolhido:", evento)
