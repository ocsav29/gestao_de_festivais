def consultar_orcamento(eventos):
    """Mostra o orçamento previsto e o total gasto num evento."""
    if not eventos:
        print("\nNão existem eventos para consultar.")
        return

    print("\n=== CONSULTAR ORÇAMENTO ===")

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
    orcamento = evento["orcamento"]

    # Eventos sem despesas registadas têm um total gasto de zero.
    total_gasto = sum(
        despesa["valor"]
        for despesa in evento.get("despesas", [])
    )

    saldo = round(orcamento - total_gasto, 2)

    print(f"\nEvento: {evento['nome']}")
    print(f"Orçamento previsto: {orcamento:.2f} €")
    print(f"Total gasto: {total_gasto:.2f} €")

    if saldo > 0:
        print(f"Dentro do orçamento. Disponível: {saldo:.2f} €")
    elif saldo == 0:
        print("O orçamento foi totalmente utilizado.")
    else:
        print(f"Orçamento ultrapassado em {abs(saldo):.2f} €")
    input("\nCarrega em Enter para voltar ao menu...")