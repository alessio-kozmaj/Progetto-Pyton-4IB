"""
main.py  -  PUNTO DI PARTENZA. Si avvia con:   python main.py
(come il Main() di C#)
"""
import dati
from app import App

if __name__ == "__main__":
    dati.carica_dati()   # 1. legge muscoli ed esercizi dal JSON
    App().mainloop()     # 2. crea la finestra e resta in attesa degli eventi
