def registar_despesa(eventos):
    """Regista uma despesa com categoria descrição e valor num evento."""
    if not eventos:
        print("\nNão existem eventos. Cria um primeiro.")
        return

    print("\n=== REGISTAR DESPESA ===")

    for numero, evento in enumerate(eventos, start=1):
        print(f"{numero} - {evento['nome']} | {evento['data']}")

    print("0 - Cancelar")

    try:
        escolha = int(input("Escolhe o número do evento: "))
    except ValueError:
        print("Escreve um número inteiro.")
        return

    if escolha == 0:
        print("Operação cancelada.")
        return

    if escolha < 1 or escolha > len(eventos):
        print("Número de evento inválido.")
        return

    evento = eventos[escolha - 1]

    while True:
        categoria = input("Categoria (ex.: equipamento): ").strip()

        if categoria:
            break

        print("A categoria não pode ficar vazia.")

    while True:
        descricao = input("Descrição da despesa: ").strip()

        if descricao:
            break

        print("A descrição não pode ficar vazia.")

    while True:
        try:
            valor = float(input("Valor (€): ").replace(",", "."))

            if 0 < valor < float("inf"):
                break

            print("O valor tem de ser positivo e finito.")

        except ValueError:
            print("Escreve um número. Exemplo: 250,50.")

    despesa = {
        "categoria": categoria,
        "descricao": descricao,
        "valor": valor
    }

    # Cria a lista de despesas caso este evento ainda não tenha uma.
    evento.setdefault("despesas", []).append(despesa)

    print(f"Despesa registada no evento '{evento['nome']}'.")