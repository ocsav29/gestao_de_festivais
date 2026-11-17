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
        id_evento (str): id do evento a procurar.

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

def pedir_orcamento(valor_atual):
    """
    Pede um novo orçamento (número igual ou superior a zero).

    Aceita vírgula ou ponto nas casas decimais (1500,50 ou 1500.50).
    Se o utilizador carregar só em Enter, mantém o orçamento atual.

    Parâmetros:
        valor_atual (float): orçamento que o evento tem agora.

    Devolve:
        float: o novo orçamento, ou o orçamento atual.
    """
    while True:
        novo = input(f"Orçamento (€) [{valor_atual}]: ").strip()

        # Enter sem escrever nada = manter o orçamento antigo
        if novo == "":
            return valor_atual

        try:
            # Troca a vírgula por ponto para o Python perceber o número
            orcamento = float(novo.replace(",", "."))
        except ValueError:
            print("Escreve um número. Exemplo: 1500 ou 1500,50.")
            continue

        # Igual à validação da criação: >= 0 e não infinito
        if 0 <= orcamento < float("inf"):
            return orcamento

        print("Introduz um orçamento válido igual ou superior a zero.")

def editar_evento(eventos):
    """
    Permite ao utilizador escolher um evento da lista e alterar os seus dados.

    Para cada campo, carregar só em Enter mantém o valor atual.
    O evento só é alterado no fim, depois de todos os valores serem válidos.

    Parâmetros:
        eventos (list): lista de dicionários com os eventos.
            A lista é alterada diretamente (não é feita uma cópia).
    """
    print("\n=== EDITAR EVENTO ===")

    # Sem eventos, não há nada para editar
    if not eventos:
        print("Ainda não existem eventos para editar.")
        return

    # Mostra os eventos numerados (1, 2, 3...) para o utilizador escolher.
    # O id é um código longo, por isso escolhe-se pelo número da lista.
    for numero, evento in enumerate(eventos, start=1):
        print(f"{numero} - {evento['nome']} ({evento['data']})")

    try:
        escolha = int(input("\nNúmero do evento a editar: ").strip())
    except ValueError:
        print("Número inválido. Tem de ser um número.")
        return

    # O número tem de corresponder a um evento da lista
    if escolha < 1 or escolha > len(eventos):
        print("Não existe nenhum evento com esse número.")
        return

    # A lista começa na posição 0, por isso subtrai-se 1
    evento = eventos[escolha - 1]

    print("\nCarrega em Enter para manter o valor que está entre [ ].")

    # Pede todos os valores primeiro
    novo_nome = pedir_texto("Nome", evento["nome"])
    nova_descricao = pedir_texto("Descrição", evento["descricao"])
    novo_local = pedir_texto("Local", evento["local"])
    nova_data = pedir_data(evento["data"])
    nova_capacidade = pedir_capacidade(evento["capacidade"])
    novo_orcamento = pedir_orcamento(evento["orcamento"])

    # Só depois altera o evento (o id nunca muda)
    evento["nome"] = novo_nome
    evento["descricao"] = nova_descricao
    evento["local"] = novo_local
    evento["data"] = nova_data
    evento["capacidade"] = nova_capacidade
    evento["orcamento"] = novo_orcamento

    print(f"\nEvento '{evento['nome']}' atualizado com sucesso!")


# Este bloco só corre quando se executa este ficheiro diretamente
# (python editar_eventos.py). Serve apenas para testes.
if __name__ == "__main__":
    eventos_teste = [
        {
            "id": "teste1",
            "nome": "Festival de Verão",
            "descricao": "Música ao ar livre",
            "local": "Faro",
            "data": "15/07/2027",
            "capacidade": 500,
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

    print(procurar_evento_por_id(eventos_teste, "teste1"))
    print(procurar_evento_por_id(eventos_teste, "nao-existe"))

    editar_evento(eventos_teste)

    # Mostra como ficaram os eventos depois da edição
    print("\nEventos depois da edição:")
    for evento in eventos_teste:
        print(evento)