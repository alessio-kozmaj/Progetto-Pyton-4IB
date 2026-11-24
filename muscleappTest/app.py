"""
app.py  -  LA FINESTRA PRINCIPALE: UNISCE TUTTI I PEZZI

Qui non c'e' logica "vera": si creano i componenti e si collegano tra loro.
    VistaCorpo --(click)--> App --(get_gruppo)--> dati
                             App --(mostra_gruppo)--> PannelloInfo
    PannelloInfo --(aggiungi)--> App --> Scheda + PannelloScheda
I componenti non si conoscono tra loro: parlano solo con l'App.
"""
import tkinter as tk
from tkinter import ttk

import dati
from scheda import Scheda
from ui_corpo import VistaCorpo
from ui_pannello import PannelloInfo
from ui_scheda import PannelloScheda

SFONDO = "#1b1b2b"
TESTO = "#eaeaf2"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Atlante muscolare e scheda di allenamento")
        self.configure(bg=SFONDO)
        self.resizable(False, False)

        self.scheda = Scheda()
        self.scheda.carica()

        # --- colonna sinistra: corpo ---
        sinistra = tk.Frame(self, bg=SFONDO)
        sinistra.pack(side="left", padx=16, pady=16)

        self.lbl_hover = tk.Label(sinistra, text=" ", font=("Segoe UI", 14, "bold"), bg=SFONDO, fg=TESTO)
        self.lbl_hover.pack(pady=(0, 8))
        self.corpo = VistaCorpo(sinistra, on_hover=self.su_hover, on_click=self.su_click)
        self.corpo.pack()
        tk.Button(sinistra, text="↻ Gira (fronte / retro)", command=self.corpo.cambia_vista).pack(pady=(10, 0))

        # --- colonna destra: due schede (tab) ---
        destra = tk.Frame(self, bg=SFONDO)
        destra.pack(side="left", fill="both", expand=True, padx=(0, 16), pady=16)

        self.tab = ttk.Notebook(destra)
        self.tab.pack(fill="both", expand=True)
        self.pannello_info = PannelloInfo(self.tab, on_aggiungi=self.su_aggiungi)
        self.pannello_scheda = PannelloScheda(self.tab, self.scheda)
        self.tab.add(self.pannello_info, text="Muscolo")
        self.tab.add(self.pannello_scheda, text="La mia scheda")

        self.lbl_stato = tk.Label(destra, text=" ", bg=SFONDO, fg="#a0a0b8")
        self.lbl_stato.pack(pady=(8, 0))

    # ---- reazioni agli eventi ----
    def su_hover(self, id_gruppo):
        if id_gruppo is None:
            self.lbl_hover.config(text=" ")
            return
        gruppo = dati.get_gruppo(id_gruppo)
        self.lbl_hover.config(text=gruppo.nome if gruppo else id_gruppo)

    def su_click(self, id_gruppo):
        gruppo = dati.get_gruppo(id_gruppo)
        if gruppo is None:
            self.lbl_stato.config(text=f"Manca '{id_gruppo}' in data/muscoli.json")
            return
        self.pannello_info.mostra_gruppo(gruppo)
        self.tab.select(self.pannello_info)

    def su_aggiungi(self, voce):
        self.scheda.aggiungi(voce)
        self.pannello_scheda.aggiorna()
        self.lbl_stato.config(text=f"Aggiunto alla scheda: {voce.nome_esercizio}")
