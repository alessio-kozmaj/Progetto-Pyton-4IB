"""
ui_scheda.py  -  TABELLA DELLA SCHEDA (interfaccia, parte B)

Mostra le voci della Scheda in una tabella (Treeview) e permette di rimuoverle.
Riceve l'oggetto Scheda nel costruttore: l'interfaccia MOSTRA, la Scheda DECIDE.
"""
import tkinter as tk
from tkinter import ttk


class PannelloScheda(tk.Frame):
    def __init__(self, parent, scheda):
        super().__init__(parent, bg="#25253a")
        self.scheda = scheda

        colonne = ("esercizio", "gruppo", "serie", "rip")
        self.tabella = ttk.Treeview(self, columns=colonne, show="headings", height=16)
        for colonna, titolo, larghezza in [("esercizio", "Esercizio", 180), ("gruppo", "Muscolo", 120),
                                           ("serie", "Serie", 60), ("rip", "Rip.", 60)]:
            self.tabella.heading(colonna, text=titolo)
            self.tabella.column(colonna, width=larghezza, anchor="w")
        self.tabella.pack(fill="both", expand=True, padx=16, pady=16)

        tk.Button(self, text="Rimuovi selezionato", command=self._rimuovi).pack(pady=(0, 16))
        self.aggiorna()

    def aggiorna(self):
        """Ridisegna la tabella a partire da scheda.voci."""
        for riga in self.tabella.get_children():
            self.tabella.delete(riga)
        for indice, voce in enumerate(self.scheda.voci):
            self.tabella.insert("", "end", iid=str(indice),
                                values=(voce.nome_esercizio, voce.nome_gruppo, voce.serie, voce.ripetizioni))

    def _rimuovi(self):
        selezione = self.tabella.selection()
        if selezione:
            self.scheda.rimuovi(int(selezione[0]))
            self.aggiorna()
