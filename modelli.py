class Esercizio:
    def __init__(self, nome, descrizione, tipo, video_url):
        self.nome = nome
        self.descrizione = descrizione
        self.tipo = tipo              # "palestra" oppure "calisthenics"
        self.video_url = video_url


class GruppoMuscolare:
    def __init__(self, id, nome, funzione, esercizi):
        self.id = id                  # es. "pettorali"
        self.nome = nome              # es. "Pettorali"
        self.funzione = funzione
        self.esercizi = esercizi      # lista di Esercizio


class VoceScheda:
    """Una riga della scheda: 'Push-up, 3 serie da 10'."""

    def __init__(self, nome_esercizio, nome_gruppo, serie, ripetizioni): #costruttore
        self.nome_esercizio = nome_esercizio
        self.nome_gruppo = nome_gruppo
        self.serie = serie
        self.ripetizioni = ripetizioni

    def to_dict(self): # per rendere json dizionario
        return {
            "nome_esercizio": self.nome_esercizio,
            "nome_gruppo": self.nome_gruppo,
            "serie": self.serie,
            "ripetizioni": self.ripetizioni,
        }

    @staticmethod
    def from_dict(d):
        return VoceScheda(d["nome_esercizio"], d["nome_gruppo"],
                          d["serie"], d["ripetizioni"])