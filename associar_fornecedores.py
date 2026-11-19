"""
Módulo de associação de fornecedores a eventos da aplicação Gestão de Festivais.

O id de cada fornecedor associado fica guardado no evento,
na lista evento["fornecedores"]. Os dados completos dos fornecedores
(nome, contacto, tipo_servico, informacoes) estão na lista de fornecedores.
"""
from participantes import escolher_evento

def escolher_fornecedor(fornecedores):
    """
    Mostra os fornecedores numerados e pede ao utilizador para escolher um.

    Parâmetros:
        fornecedores (list): lista de dicionários com os fornecedores.

    Devolve:
        dict: o fornecedor escolhido, ou None se cancelar ou a escolha for inválida.
    """
    for numero, fornecedor in enumerate(fornecedores, start=1):
        print(f"{numero} - {fornecedor['nome']} ({fornecedor['tipo_servico']})")

    print("0 - Cancelar")

    try:
        escolha = int(input("\nNúmero do fornecedor: ").strip())
    except ValueError:
        print("Número inválido. Tem de ser um número.")
        return None

    if escolha == 0:
        print("Operação cancelada.")
        return None

    if escolha < 1 or escolha > len(fornecedores):
        print("Não existe nenhum fornecedor com esse número.")
        return None

    return fornecedores[escolha - 1]

def associar_fornecedor(eventos, fornecedores):
    """
    Associa um fornecedor a um evento.

    Guarda o id do fornecedor em evento["fornecedores"].
    Não deixa associar o mesmo fornecedor duas vezes ao mesmo evento.

    Parâmetros:
        eventos (list): lista de dicionários com os eventos.
        fornecedores (list): lista de dicionários com os fornecedores.
    """
    print("\n=== ASSOCIAR FORNECEDOR A EVENTO ===")

    if not eventos:
        print("Ainda não existem eventos. Cria um primeiro.")
        return

    if not fornecedores:
        print("Ainda não existem fornecedores. Regista um primeiro.")
        return

    print("\nEscolhe o evento:")
    evento = escolher_evento(eventos)
    if evento is None:
        return

    print("\nEscolhe o fornecedor:")
    fornecedor = escolher_fornecedor(fornecedores)
    if fornecedor is None:
        return

    # Cria a lista se o evento ainda não tiver fornecedores associados
    ids_associados = evento.setdefault("fornecedores", [])

    # Evita associar o mesmo fornecedor duas vezes
    if fornecedor["id"] in ids_associados:
        print(f"O fornecedor '{fornecedor['nome']}' já está associado a este evento.")
        return

    ids_associados.append(fornecedor["id"])

    print(f"\nFornecedor '{fornecedor['nome']}' ({fornecedor['tipo_servico']}) "
          f"associado ao evento '{evento['nome']}'.")

def procurar_fornecedor_por_id(fornecedores, id_fornecedor):
    """
    Procura um fornecedor na lista pelo seu id.

    Parâmetros:
        fornecedores (list): lista de dicionários com os fornecedores.
        id_fornecedor (str): id do fornecedor a procurar.

    Devolve:
        dict: o fornecedor encontrado, ou None se não existir.
    """
    for fornecedor in fornecedores:
        if fornecedor["id"] == id_fornecedor:
            return fornecedor

    return None

def procurar_fornecedor_por_id(fornecedores, id_fornecedor):
    """
    Procura um fornecedor na lista pelo seu id.

    Parâmetros:
        fornecedores (list): lista de dicionários com os fornecedores.
        id_fornecedor (str): id do fornecedor a procurar.

    Devolve:
        dict: o fornecedor encontrado, ou None se não existir.
    """
    for fornecedor in fornecedores:
        if fornecedor["id"] == id_fornecedor:
            return fornecedor

    return None


def mostrar_fornecedores_eventos(eventos, fornecedores):
    """
    Mostra, para cada evento, os fornecedores associados e o serviço de cada um.

    Parâmetros:
        eventos (list): lista de dicionários com os eventos.
        fornecedores (list): lista de dicionários com os fornecedores.
    """
    print("\n=== FORNECEDORES POR EVENTO ===")

    if not eventos:
        print("Ainda não existem eventos registados.")
        return

    for evento in eventos:
        print(f"\n{evento['nome']} ({evento['data']})")

        ids_associados = evento.get("fornecedores", [])

        if not ids_associados:
            print("  Sem fornecedores associados.")
            continue  # passa ao evento seguinte

        for id_fornecedor in ids_associados:
            fornecedor = procurar_fornecedor_por_id(fornecedores, id_fornecedor)

            # O fornecedor pode já não existir na lista
            if fornecedor is None:
                print("  - Fornecedor não encontrado (pode ter sido removido).")
            else:
                print(f"  - {fornecedor['tipo_servico']}: {fornecedor['nome']} "
                      f"(contacto: {fornecedor['contacto']})")
                
# Este bloco só corre quando se executa este ficheiro diretamente
# (python associar_fornecedores.py). Serve apenas para testes.
if __name__ == "__main__":
    fornecedores_teste = [
        {"id": "f1", "nome": "SomPro", "contacto": "912345678",
         "tipo_servico": "Som", "informacoes": ""},
        {"id": "f2", "nome": "SeguraMais", "contacto": "seg@email.pt",
         "tipo_servico": "Segurança", "informacoes": ""},
    ]

    eventos_teste = [
        {"id": "e1", "nome": "Festival de Verão", "data": "15/07/2027"},
        {"id": "e2", "nome": "Noite de Jazz", "data": "10/08/2027"},
    ]

    # Associa 3 vezes: tenta repetir o mesmo fornecedor na 3.ª
    for tentativa in range(3):
        associar_fornecedor(eventos_teste, fornecedores_teste)

    print("\nFornecedores do evento 1:", eventos_teste[0].get("fornecedores", []))
    mostrar_fornecedores_eventos(eventos_teste, fornecedores_teste)