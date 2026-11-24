import json
import os
# legge il file json rendendolo leggibile per tutto il resto del programma
from modelli import Esercizio, GruppoMuscolare

_CARTELLA = os.path.dirname(os.path.abspath(__file__))
_PERCORSO_JSON = os.path.join(_CARTELLA, "data", "esercizi.json")

_gruppi = {}   # id -> GruppoMuscolare (come Dictionary<string, GruppoMuscolare>)


def carica_dati():
    global _gruppi
    with open(_PERCORSO_JSON, encoding="utf-8") as f:
        grezzi = json.load(f)          # lista di dizionari

    _gruppi = {}
    for g in grezzi:
        esercizi = [
            Esercizio(e["nome"], e["descrizione"], e["tipo"], e["video_url"])
            for e in g["esercizi"]
        ]
        _gruppi[g["id"]] = GruppoMuscolare(g["id"], g["nome"], g["funzione"], esercizi)


def get_gruppo(id_gruppo):
    return _gruppi.get(id_gruppo)      # None se non esiste


def get_tutti_i_gruppi():
    return list(_gruppi.values())