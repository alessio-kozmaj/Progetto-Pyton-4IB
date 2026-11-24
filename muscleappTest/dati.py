"""
dati.py  -  CARICA I MUSCOLI E GLI ESERCIZI DAL FILE JSON

Gli altri file NON aprono mai il JSON direttamente: chiedono a questo file.
Le due funzioni che l'interfaccia puo' usare sono:
    get_gruppo(id)          ->  restituisce un GruppoMuscolare (o None)
    get_tutti_i_gruppi()    ->  restituisce la lista di tutti i gruppi
"""
import json
import os

from modelli import Esercizio, GruppoMuscolare

_CARTELLA = os.path.dirname(os.path.abspath(__file__))
_PERCORSO_JSON = os.path.join(_CARTELLA, "data", "muscoli.json")

_gruppi = {}  # dizionario: id -> GruppoMuscolare (come Dictionary<string, GruppoMuscolare>)


def carica_dati():
    """Legge il JSON e crea gli oggetti. Va chiamata una volta all'avvio."""
    global _gruppi
    with open(_PERCORSO_JSON, encoding="utf-8") as f:
        grezzi = json.load(f)  # lista di dizionari

    _gruppi = {}
    for g in grezzi:
        # "list comprehension": il LINQ Select() di Python
        esercizi = [
            Esercizio(e["nome"], e["descrizione"], e["tipo"], e["video_url"])
            for e in g["esercizi"]
        ]
        _gruppi[g["id"]] = GruppoMuscolare(g["id"], g["nome"], g["funzione"], esercizi)


def get_gruppo(id_gruppo):
    return _gruppi.get(id_gruppo)  # .get() restituisce None se non esiste


def get_tutti_i_gruppi():
    return list(_gruppi.values())
