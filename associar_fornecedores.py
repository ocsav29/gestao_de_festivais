"""
Módulo de associação de fornecedores a eventos da aplicação Gestão de Festivais.

O id de cada fornecedor associado fica guardado no evento,
na lista evento["fornecedores"]. Os dados completos dos fornecedores
(nome, contacto, tipo_servico, informacoes) estão na lista de fornecedores.
"""


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


# Este bloco só corre quando se executa este ficheiro diretamente
# (python associar_fornecedores.py). Serve apenas para testes.
if __name__ == "__main__":
    fornecedores_teste = [
        {"id": "f1", "nome": "SomPro", "contacto": "912345678",
         "tipo_servico": "Som", "informacoes": ""},
        {"id": "f2", "nome": "SeguraMais", "contacto": "seg@email.pt",
         "tipo_servico": "Segurança", "informacoes": ""},
    ]

    escolhido = escolher_fornecedor(fornecedores_teste)
    print("Escolhido:", escolhido)