from uuid import uuid4


def registar_fornecedor(fornecedores):
    """Pede os dados de um fornecedor e adiciona-o à lista."""
    print("\n=== REGISTAR FORNECEDOR ===")

    while True:
        nome = input("Nome: ").strip()

        if nome:
            break

        print("O nome não pode ficar vazio.")

    while True:
        contacto = input("Contacto (telefone ou email): ").strip()

        if contacto:
            break

        print("O contacto não pode ficar vazio.")

    while True:
        tipo_servico = input("Tipo de serviço: ").strip()

        if tipo_servico:
            break

        print("O tipo de serviço não pode ficar vazio.")

    # Este campo é opcional.
    informacoes = input("Informações relevantes (opcional): ").strip()

    fornecedor = {
        "id": uuid4().hex,
        "nome": nome,
        "contacto": contacto,
        "tipo_servico": tipo_servico,
        "informacoes": informacoes
    }

    fornecedores.append(fornecedor)

    print(f"Fornecedor '{nome}' registado com sucesso.")