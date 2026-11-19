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