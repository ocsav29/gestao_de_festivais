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

def registar_participante(eventos):
    """
    Inscreve um participante num evento, respeitando a capacidade máxima.

    O participante é guardado dentro do evento, na lista
    evento["participantes"]. Se o evento estiver lotado, não inscreve.

    Parâmetros:
        eventos (list): lista de dicionários com os eventos.
            A lista é alterada diretamente (não é feita uma cópia).
    """
    print("\n=== REGISTAR PARTICIPANTE ===")

    # Sem eventos, não há onde inscrever participantes
    if not eventos:
        print("Ainda não existem eventos. Cria um primeiro.")
        return

    evento = escolher_evento(eventos)

    # None = o utilizador cancelou ou escolheu um número inválido
    if evento is None:
        return

    print(f"\nLugares ocupados: {contar_participantes(evento)}/{evento['capacidade']}")

    # Controlo da capacidade: não deixa inscrever se não houver vagas
    if lugares_disponiveis(evento) <= 0:
        print("Este evento está lotado. Não é possível inscrever mais participantes.")
        return

    participante = pedir_dados_participante()

    # Cria a lista de participantes se o evento ainda não tiver uma
    evento.setdefault("participantes", []).append(participante)

    print(f"\nParticipante '{participante['nome']}' inscrito no evento '{evento['nome']}'.")
    print(f"Lugares ocupados: {contar_participantes(evento)}/{evento['capacidade']}")

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

            # Tenta inscrever 4 pessoas no evento 1, que só tem 3 lugares
    for tentativa in range(4):
        registar_participante(eventos_teste)

    print("\nParticipantes do evento 1:")
    for participante in eventos_teste[0].get("participantes", []):
        print(participante)