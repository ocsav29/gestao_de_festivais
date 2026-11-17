def registar_bilhetes(eventos):
    from dados_bilhetes import carregar_bilhetes, guardar_bilhetes
    """Inicia o registo de bilhetes vendidos para um evento."""

    print("\n=== REGISTAR BILHETES ===")

    if not eventos:
        print("Ainda não existem eventos registados.")
        return

    print("Eventos disponíveis:")

    for evento in eventos:
        print(f"ID: {evento['id']} - {evento['nome']}")
    id_evento = input("\nIntroduz o ID do evento: ").strip()

    evento_escolhido = None

    for evento in eventos:
        if str(evento["id"]) == id_evento:
            evento_escolhido = evento
            break

    if evento_escolhido is None:
        print("Evento não encontrado.")
        return

    print(f"Evento selecionado: {evento_escolhido['nome']}")
    while True:
        try:
            quantidade = int(input("Quantidade de bilhetes vendidos: "))

            if quantidade > 0:
                break

            print("A quantidade deve ser superior a zero.")

        except ValueError:
            print("Introduz um número inteiro válido.")
    while True:
        try:
            preco = float(input("Preço de cada bilhete (€): ").replace(",", "."))

            if preco >= 0:
                break

            print("O preço não pode ser negativo.")

        except ValueError:
            print("Introduz um preço válido.")
                # Calcula o valor total dos bilhetes vendidos.
    total = quantidade * preco

    print("\n=== RESUMO DA VENDA ===")
    print(f"Evento: {evento_escolhido['nome']}")
    print(f"Quantidade vendida: {quantidade}")
    print(f"Preço por bilhete: {preco:.2f} €")
    print(f"Total da venda: {total:.2f} €")
    venda = {
        "id_evento": evento_escolhido["id"],
        "quantidade": quantidade,
        "preco_unitario": preco,
        "total": total
    }

    bilhetes = carregar_bilhetes()
    bilhetes.append(venda)
    guardar_bilhetes(bilhetes)

    print("Venda de bilhetes registada com sucesso!")