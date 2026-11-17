from datetime import datetime

def criar_evento(eventos):
    """Valida os dados introduzidos e adiciona um evento à lista."""
    print("\n=== CRIAR EVENTO ===")

    while True:
        nome = input("Nome: ").strip()

        if nome:
            break

        print("O nome não pode ficar vazio.")

    while True:
        descricao = input("Descrição: ").strip()

        if descricao:
            break

        print("A descrição não pode ficar vazia.")

    while True:
        local = input("Local: ").strip()

        if local:
            break

        print("O local não pode ficar vazio.")
    while True:
        data = input("Data (DD/MM/AAAA): ").strip()

        try:
            data_validada = datetime.strptime(data, "%d/%m/%Y")
            data = data_validada.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Usa DD/MM/AAAA com uma data real.")
    while True:
        try:
            capacidade = int(input("Capacidade máxima: "))

            if capacidade > 0:
                break

            print("A capacidade tem de ser maior que zero.")

        except ValueError:
            print("Escreve um número inteiro. Exemplo: 500.")
    while True:
        try:
            orcamento = float(
                input("Orçamento (€): ").replace(",", ".")
            )

            if 0 <= orcamento < float("inf"):
                break

            print("Introduz um orçamento válido igual ou superior a zero.")

        except ValueError:
            print("Escreve um número. Exemplo: 1500 ou 1500,50.")

    evento = {
        "id": len(eventos) + 1,
        "nome": nome,
        "descricao": descricao,
        "local": local,
        "data": data,
        "capacidade": capacidade,
        "orcamento": orcamento
    }

    eventos.append(evento)

    print(f"\nEvento '{nome}' criado com sucesso!")