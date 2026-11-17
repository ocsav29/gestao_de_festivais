"""
Módulo de registo de participantes da aplicação Gestão de Festivais.

Os participantes ficam guardados dentro de cada evento,
na lista evento["participantes"]. Cada participante tem:
id, nome e contacto.
"""
from uuid import uuid4

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

def contar_participantes(evento):
    """
    Conta quantos participantes estão inscritos num evento.

    Parâmetros:
        evento (dict): o evento a verificar.

    Devolve:
        int: número de participantes inscritos (0 se ainda não houver).
    """
    # .get devolve uma lista vazia se o evento ainda não tiver participantes
    return len(evento.get("participantes", []))


def lugares_disponiveis(evento):
    """
    Calcula quantos lugares ainda estão livres num evento.

    Parâmetros:
        evento (dict): o evento a verificar.

    Devolve:
        int: capacidade do evento menos os participantes já inscritos.
    """
    return evento["capacidade"] - contar_participantes(evento)

def pedir_texto_obrigatorio(pergunta):
    """
    Pede um texto ao utilizador e repete até não estar vazio.

    Parâmetros:
        pergunta (str): texto mostrado ao utilizador (ex.: "Nome: ").

    Devolve:
        str: o texto escrito, sem espaços no início e no fim.
    """
    while True:
        texto = input(pergunta).strip()

        if texto:
            return texto

        print("Este campo não pode ficar vazio.")


def pedir_dados_participante():
    """
    Pede o nome e o contacto de um participante e cria o seu dicionário.

    Devolve:
        dict: participante com as chaves id, nome e contacto.
    """
    nome = pedir_texto_obrigatorio("Nome do participante: ")
    contacto = pedir_texto_obrigatorio("Contacto (telefone ou email): ")

    participante = {
        "id": uuid4().hex,  # código único, como nos eventos
        "nome": nome,
        "contacto": contacto,
    }

    return participante

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

        # Evento sem participantes
    print("Inscritos:", contar_participantes(eventos_teste[0]))
    print("Vagas:", lugares_disponiveis(eventos_teste[0]))

    # Simula 2 participantes inscritos
    eventos_teste[0]["participantes"] = [
        {"id": "p1", "nome": "Ana", "contacto": "912345678"},
        {"id": "p2", "nome": "Rui", "contacto": "rui@email.pt"},
    ]
    print("Inscritos:", contar_participantes(eventos_teste[0]))
    print("Vagas:", lugares_disponiveis(eventos_teste[0]))

    novo = pedir_dados_participante()
    print("Participante criado:", novo)