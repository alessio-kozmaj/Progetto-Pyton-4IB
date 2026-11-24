"""
scheda.py  -  LA SCHEDA DI ALLENAMENTO (logica, niente grafica)

Contiene una lista di VoceScheda e sa salvarsi/caricarsi da data/scheda.json.
Funzioni che l'interfaccia puo' usare:
    scheda.aggiungi(voce)
    scheda.rimuovi(indice)
    scheda.voci            (la lista)
"""
import json
import os

from modelli import VoceScheda

_CARTELLA = os.path.dirname(os.path.abspath(__file__))
_PERCORSO_SCHEDA = os.path.join(_CARTELLA, "data", "scheda.json")


class Scheda:
    def __init__(self):
        self.voci = []  # List<VoceScheda>

    def aggiungi(self, voce):
        self.voci.append(voce)
        self.salva()

    def rimuovi(self, indice):
        if 0 <= indice < len(self.voci):
            del self.voci[indice]
            self.salva()

    def salva(self):
        with open(_PERCORSO_SCHEDA, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in self.voci], f, ensure_ascii=False, indent=2)

    def carica(self):
        if not os.path.exists(_PERCORSO_SCHEDA):
            return  # prima esecuzione: scheda vuota
        with open(_PERCORSO_SCHEDA, encoding="utf-8") as f:
            self.voci = [VoceScheda.from_dict(d) for d in json.load(f)]
