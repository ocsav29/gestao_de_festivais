def eliminar_evento(eventos):
    """Mostra os eventos e permite eliminar um após confirmação."""
    if not eventos:
        print("\nNão existem eventos para eliminar.")
        return

    print("\n=== ELIMINAR EVENTO ===")

    # Os números apresentados servem apenas para escolher na lista.
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

    # As posições da lista começam em zero.
    evento = eventos[escolha - 1]

    confirmacao = input(
        f"Eliminar '{evento['nome']}'? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        eventos.pop(escolha - 1)
        print("Evento eliminado com sucesso.")
    else:
        print("Operação cancelada.")