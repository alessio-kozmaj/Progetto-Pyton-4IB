import json # per leggere i file
import os # per avere i percorsi
from dataclasses import dataclass # per avere le classi

BASE = os.path.dirname(os.path.abspath(__file__)) 
FILE_ESERCIZI = os.path.join(BASE, "esercizi.json") # per le directory del progetto

@dataclass
class Esercizio: # classe per gli esercizzi
    nome: str
    muscolo: str
    descrizione: str
    esecuzione: str

def leggi_json(percorso, default):             # serve a leggere il file json contenente gli esercizzi
    if not os.path.exists(percorso): # controllo che esiste il file json degli esercizzi 
        return default
    with open(percorso, "r", encoding="utf-8") as f:
        return json.load(f)

    