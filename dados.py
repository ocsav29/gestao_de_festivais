import json
from pathlib import Path


# Guarda os dados na mesma pasta deste ficheiro.
FICHEIRO_EVENTOS = Path(__file__).with_name("eventos.json")


def carregar_eventos():
    """Lê os eventos guardados ou devolve uma lista vazia."""
    if not FICHEIRO_EVENTOS.exists():
        return []

    with FICHEIRO_EVENTOS.open("r", encoding="utf-8") as ficheiro:
        return json.load(ficheiro)


def guardar_eventos(eventos):
    """Grava a lista de eventos num ficheiro JSON."""
    with FICHEIRO_EVENTOS.open("w", encoding="utf-8") as ficheiro:
        json.dump(eventos, ficheiro, ensure_ascii=False, indent=4)