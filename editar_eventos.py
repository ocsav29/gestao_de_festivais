"""
Módulo de edição de eventos da aplicação Gestão de Festivais.

Permite alterar os dados de um evento que já existe.
Cada evento é um dicionário com as chaves:
id, nome, descricao, local, data, capacidade e orcamento.
"""
from datetime import datetime

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

def pedir_data(valor_atual):
    """
    Pede uma nova data no formato DD/MM/AAAA.

    Se o utilizador carregar só em Enter, mantém a data atual.
    Se a data for inválida, volta a pedir até ser válida.

    Parâmetros:
        valor_atual (str): data que o evento tem agora (DD/MM/AAAA).

    Devolve:
        str: a nova data em DD/MM/AAAA, ou a data atual.
    """
    while True:
        nova = input(f"Data (DD/MM/AAAA) [{valor_atual}]: ").strip()

        # Enter sem escrever nada = manter a data antiga
        if nova == "":
            return valor_atual

        try:
            # Verifica se o texto é uma data real no formato DD/MM/AAAA
            data_validada = datetime.strptime(nova, "%d/%m/%Y")
            # Volta a escrever com 2 dígitos (ex.: 1/2/2027 -> 01/02/2027)
            return data_validada.strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida. Usa DD/MM/AAAA com uma data real.")

def pedir_capacidade(valor_atual):
    """
    Pede uma nova capacidade máxima (número inteiro maior que zero).

    Se o utilizador carregar só em Enter, mantém a capacidade atual.
    Se o valor for inválido, volta a pedir.

    Parâmetros:
        valor_atual (int): capacidade que o evento tem agora.

    Devolve:
        int: a nova capacidade, ou a capacidade atual.
    """
    while True:
        nova = input(f"Capacidade máxima [{valor_atual}]: ").strip()

        # Enter sem escrever nada = manter a capacidade antiga
        if nova == "":
            return valor_atual

        try:
            capacidade = int(nova)
        except ValueError:
            print("Escreve um número inteiro. Exemplo: 500.")
            continue  # volta ao início do while e pergunta outra vez

        if capacidade > 0:
            return capacidade

        print("A capacidade tem de ser maior que zero.")

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

    nova_capacidade = pedir_capacidade(500)
    print("Resultado:", nova_capacidade)
