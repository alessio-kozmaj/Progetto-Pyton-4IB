import json
import os
from datetime import date
# legge il file json rendendolo leggibile per tutto il resto del programma
from modelli import Esercizio, GruppoMuscolare

_CARTELLA = os.path.dirname(os.path.abspath(__file__))
_PERCORSO_JSON = os.path.join(_CARTELLA, "data", "esercizi.json")
_PERCORSO_SCHEDE = os.path.join(_CARTELLA, "data", "schede.json")
_PERCORSO_ALLENAMENTI = os.path.join(_CARTELLA, "data", "allenamenti.json")

_gruppi = {}   # id -> GruppoMuscolare (come Dictionary<string, GruppoMuscolare>)


# ---------------------------------------------------------------
# Funzioni di supporto per leggere/scrivere JSON
# ---------------------------------------------------------------

def _leggi(percorso, default):
    """Legge un JSON. Se il file non esiste ancora, ritorna il valore di default."""
    if not os.path.exists(percorso):
        return default
    with open(percorso, encoding="utf-8") as f:
        return json.load(f)


def _scrivi(percorso, dati):
    """Scrive un JSON (crea la cartella data/ se manca)."""
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------
# Esercizi e gruppi muscolari (sola lettura)
# ---------------------------------------------------------------

def carica_dati():
    global _gruppi
    with open(_PERCORSO_JSON, encoding="utf-8") as f:
        grezzi = json.load(f)          # lista di dizionari

    _gruppi = {}
    for g in grezzi:
        esercizi = [
            Esercizio(e["nome"], e["descrizione"], e["tipo"], e["video_url"], g["id"])
            for e in g["esercizi"]
        ]
        _gruppi[g["id"]] = GruppoMuscolare(g["id"], g["nome"], g["funzione"], esercizi)


def get_gruppo(id_gruppo):
    if not _gruppi:                    # se non ho ancora caricato, lo faccio ora
        carica_dati()
    return _gruppi.get(id_gruppo)      # None se non esiste


def get_tutti_i_gruppi():
    if not _gruppi:
        carica_dati()
    return list(_gruppi.values())


def trova_esercizio(id_gruppo, nome_esercizio):
    """Ritorna l'Esercizio con quel nome dentro quel gruppo, oppure None."""
    gruppo = get_gruppo(id_gruppo)
    if gruppo is None:
        return None
    for e in gruppo.esercizi:
        if e.nome == nome_esercizio:
            return e
    return None


# ---------------------------------------------------------------
# Schede di allenamento (lettura e scrittura)
# Formato schede.json:  {"Scheda A": [ {gruppo_id, nome, serie, rip}, ... ]}
# ---------------------------------------------------------------

def carica_schede():
    return _leggi(_PERCORSO_SCHEDE, {})


def crea_scheda(nome_scheda):
    schede = carica_schede()
    if nome_scheda not in schede:
        schede[nome_scheda] = []
        _scrivi(_PERCORSO_SCHEDE, schede)


def aggiungi_a_scheda(nome_scheda, esercizio, serie=3, rip=10):
    schede = carica_schede()
    schede.setdefault(nome_scheda, []).append({
        "gruppo_id": esercizio.gruppo_id,
        "nome": esercizio.nome,
        "serie": serie,
        "rip": rip,
    })
    _scrivi(_PERCORSO_SCHEDE, schede)


def rimuovi_da_scheda(nome_scheda, indice):
    schede = carica_schede()
    if nome_scheda in schede and 0 <= indice < len(schede[nome_scheda]):
        schede[nome_scheda].pop(indice)
        _scrivi(_PERCORSO_SCHEDE, schede)


def elimina_scheda(nome_scheda):
    schede = carica_schede()
    schede.pop(nome_scheda, None)
    _scrivi(_PERCORSO_SCHEDE, schede)


# ---------------------------------------------------------------
# Allenamenti e storico (per il grafico pesi/ripetizioni)
# Formato allenamenti.json:
#   [ {"data": "2026-11-27", "esercizio": "Panca piana", "peso": 60, "rip": 8}, ... ]
# ---------------------------------------------------------------

def registra_allenamento(nome_esercizio, peso, rip):
    log = _leggi(_PERCORSO_ALLENAMENTI, [])
    log.append({
        "data": date.today().isoformat(),
        "esercizio": nome_esercizio,
        "peso": peso,
        "rip": rip,
    })
    _scrivi(_PERCORSO_ALLENAMENTI, log)


def storico(nome_esercizio):
    """Tutte le registrazioni di un esercizio, in ordine di data."""
    log = _leggi(_PERCORSO_ALLENAMENTI, [])
    voci = [r for r in log if r["esercizio"] == nome_esercizio]
    return sorted(voci, key=lambda r: r["data"])