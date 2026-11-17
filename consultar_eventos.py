def consultar_eventos(eventos):
    """Apresenta os eventos registados na aplicação."""

    print("\n=== CONSULTAR EVENTOS ===")

    if not eventos:
        print("Ainda não existem eventos registados.")
        return
    for evento in eventos:
        print("\n-------------------------")
        print(f"ID: {evento['id']}")
        print(f"Nome: {evento['nome']}")
        print(f"Descrição: {evento['descricao']}")
        print(f"Local: {evento['local']}")
        print(f"Data: {evento['data']}")
        print(f"Capacidade: {evento['capacidade']}")
        print(f"Orçamento: {evento['orcamento']:.2f} €")

    print("\n-------------------------")