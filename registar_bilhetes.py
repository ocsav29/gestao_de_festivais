def registar_bilhetes(eventos):
    """Inicia o registo de bilhetes vendidos para um evento."""

    print("\n=== REGISTAR BILHETES ===")

    if not eventos:
        print("Ainda não existem eventos registados.")
        return

    print("Eventos disponíveis:")

    for evento in eventos:
        print(f"ID: {evento['id']} - {evento['nome']}")