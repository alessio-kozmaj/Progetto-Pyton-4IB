"""
ui_pannello.py  -  PANNELLO INFORMAZIONI (interfaccia, parte B)

Mostra nome, funzione e i migliori esercizi del muscolo cliccato.
Per ogni esercizio: bottone Video, scelta serie/ripetizioni, bottone "+ Scheda".
Quando si preme "+ Scheda" crea una VoceScheda e la passa alla funzione
on_aggiungi (che decide l'App cosa farne).
"""
import tkinter as tk
import webbrowser

from modelli import VoceScheda

SFONDO = "#25253a"
TESTO = "#eaeaf2"
TESTO_SECONDARIO = "#a0a0b8"
ACCENTO = "#ff6b5b"


def _leggi_intero(variabile, predefinito):
    try:
        valore = int(variabile.get())
        return valore if valore > 0 else predefinito
    except ValueError:
        return predefinito


class PannelloInfo(tk.Frame):
    def __init__(self, parent, on_aggiungi):
        super().__init__(parent, bg=SFONDO)
        self.on_aggiungi = on_aggiungi

        self.lbl_nome = tk.Label(self, font=("Segoe UI", 22, "bold"), bg=SFONDO, fg=TESTO, anchor="w")
        self.lbl_nome.pack(fill="x", padx=16, pady=(16, 0))
        self.lbl_funzione = tk.Label(self, font=("Segoe UI", 11), bg=SFONDO, fg=TESTO_SECONDARIO,
                                     wraplength=400, justify="left", anchor="w")
        self.lbl_funzione.pack(fill="x", padx=16, pady=(4, 12))

        self.contenitore = tk.Frame(self, bg=SFONDO)
        self.contenitore.pack(fill="both", expand=True, padx=16)

        self.mostra_vuoto()

    def mostra_vuoto(self):
        self.lbl_nome.config(text="Seleziona un muscolo")
        self.lbl_funzione.config(text="Passa il mouse sul corpo e clicca su un gruppo muscolare.")
        self._svuota()

    def mostra_gruppo(self, gruppo):
        self.lbl_nome.config(text=gruppo.nome)
        self.lbl_funzione.config(text=gruppo.funzione)
        self._svuota()
        for esercizio in gruppo.esercizi:
            self._crea_riga(gruppo, esercizio)

    def _svuota(self):
        for widget in self.contenitore.winfo_children():
            widget.destroy()

    def _crea_riga(self, gruppo, esercizio):
        riga = tk.Frame(self.contenitore, bg=SFONDO)
        riga.pack(fill="x", pady=8)

        titolo = f"{esercizio.nome}  ({esercizio.tipo})"
        tk.Label(riga, text=titolo, font=("Segoe UI", 12, "bold"), bg=SFONDO, fg=TESTO,
                 anchor="w").pack(fill="x")
        tk.Label(riga, text=esercizio.descrizione, font=("Segoe UI", 10), bg=SFONDO,
                 fg=TESTO_SECONDARIO, wraplength=400, justify="left", anchor="w").pack(fill="x")

        controlli = tk.Frame(riga, bg=SFONDO)
        controlli.pack(fill="x", pady=(4, 0))

        serie = tk.StringVar(value="3")
        ripetizioni = tk.StringVar(value="10")
        tk.Spinbox(controlli, from_=1, to=20, width=3, textvariable=serie).pack(side="left")
        tk.Label(controlli, text="serie x", bg=SFONDO, fg=TESTO).pack(side="left", padx=4)
        tk.Spinbox(controlli, from_=1, to=50, width=3, textvariable=ripetizioni).pack(side="left")
        tk.Label(controlli, text="rip.", bg=SFONDO, fg=TESTO).pack(side="left", padx=4)

        tk.Button(controlli, text="▶ Video",
                  command=lambda: webbrowser.open(esercizio.video_url)).pack(side="right")

        def aggiungi():
            voce = VoceScheda(esercizio.nome, gruppo.nome,
                              _leggi_intero(serie, 3), _leggi_intero(ripetizioni, 10))
            self.on_aggiungi(voce)

        tk.Button(controlli, text="+ Scheda", command=aggiungi).pack(side="right", padx=6)
