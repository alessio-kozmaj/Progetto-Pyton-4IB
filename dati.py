import json

def carica_muscoli():
    """Legge il file JSON e restituisce la lista dei muscoli."""
    try:
        # Apriamo il file in modalità lettura ("r") con codifica utf-8 per le lettere accentate
        with open("data/muscoli.json", "r", encoding="utf-8") as file:
            # json.load trasforma il testo in liste e dizionari Python
            muscoli = json.load(file)
            return muscoli
            
    except FileNotFoundError:
        print("ERRORE: Impossibile trovare il file 'data/muscoli.json'")
        return []
        
    except json.JSONDecodeError:
        print("ERRORE: Il file JSON contiene un errore di sintassi.")
        return []