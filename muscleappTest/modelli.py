"""
modelli.py  -  LE CLASSI DEI DATI

Qui descriviamo "che cosa esiste" nel programma:
un esercizio, un gruppo muscolare, una riga della scheda di allenamento.
Questo file NON sa nulla di grafica e NON legge file: contiene solo classi.

"""


class Esercizio:
    def __init__(self, nome, descrizione, tipo, video_url):
        self.nome = nome                  # es. "Push-up"
        self.descrizione = descrizione    # breve spiegazione
        self.tipo = tipo                  # "palestra" oppure "calisthenics"
        self.video_url = video_url        # link che si apre nel browser


class GruppoMuscolare:
    def __init__(self, id, nome, funzione, esercizi):
        self.id = id                # identificatore tecnico, es. "pettorali"
        self.nome = nome            # nome da mostrare, es. "Pettorali"
        self.funzione = funzione    # a cosa serve il muscolo
        self.esercizi = esercizi    # List<Esercizio> (in Python: una lista [])


class VoceScheda:
    """Una riga della scheda: 'Push-up, 3 serie da 10'."""

    def __init__(self, nome_esercizio, nome_gruppo, serie, ripetizioni):
        self.nome_esercizio = nome_esercizio
        self.nome_gruppo = nome_gruppo
        self.serie = serie
        self.ripetizioni = ripetizioni

    # Per salvare su file JSON dobbiamo trasformare l'oggetto in un dizionario
    # (e viceversa). In C# useresti la serializzazione.
    def to_dict(self):
        return {
            "nome_esercizio": self.nome_esercizio,
            "nome_gruppo": self.nome_gruppo,
            "serie": self.serie,
            "ripetizioni": self.ripetizioni,
        }

    @staticmethod
    def from_dict(d):
        return VoceScheda(d["nome_esercizio"], d["nome_gruppo"], d["serie"], d["ripetizioni"])
