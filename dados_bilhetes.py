import json
from pathlib import Path


# Localização do ficheiro onde ficam guardadas as vendas.
FICHEIRO_BILHETES = Path(__file__).with_name("bilhetes.json")


def carregar_bilhetes():
    """Carrega as vendas guardadas ou devolve uma lista vazia."""

    if not FICHEIRO_BILHETES.exists():
        return []

    with FICHEIRO_BILHETES.open("r", encoding="utf-8") as ficheiro:
        return json.load(ficheiro)


def guardar_bilhetes(bilhetes):
    """Guarda a lista de vendas de bilhetes num ficheiro JSON."""

    with FICHEIRO_BILHETES.open("w", encoding="utf-8") as ficheiro:
        json.dump(bilhetes, ficheiro, ensure_ascii=False, indent=4)