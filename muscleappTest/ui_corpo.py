"""
ui_corpo.py  -  IL CORPO CLICCABILE (interfaccia, parte A)

VistaCorpo e' un Canvas che disegna i poligoni di regioni.py.
Non conosce i dati (nomi, esercizi): quando succede qualcosa AVVISA chi l'ha
creato tramite due "callback" (funzioni passate dal di fuori, come i delegate in C#):
    on_hover(id_gruppo)   - il mouse entra (id) o esce (None) da un muscolo
    on_click(id_gruppo)   - click su un muscolo
"""
import tkinter as tk

from regioni import LARGHEZZA, ALTEZZA, SILHOUETTE, REGIONI

COLORE_SFONDO = "#1b1b2b"
COLORE_SILHOUETTE = "#33334a"
COLORE_MUSCOLO = "#8e3b46"
COLORE_HOVER = "#ff6b5b"
COLORE_SELEZIONATO = "#f1c40f"


def appiattisci(punti):
    """[(x1,y1),(x2,y2)] -> [x1,y1,x2,y2]  (formato richiesto da create_polygon)"""
    return [coordinata for punto in punti for coordinata in punto]


class VistaCorpo(tk.Canvas):
    def __init__(self, parent, on_hover=None, on_click=None):
        super().__init__(parent, width=LARGHEZZA, height=ALTEZZA,
                         bg=COLORE_SFONDO, highlightthickness=0)
        self.on_hover = on_hover
        self.on_click = on_click
        self.vista = "fronte"      # oppure "retro"
        self.selezionato = None    # id del muscolo cliccato
        self.disegna()

    def disegna(self):
        self.delete("all")  # cancella tutto (e anche i vecchi bind)

        for tipo, dati in SILHOUETTE:
            if tipo == "ovale":
                self.create_oval(*dati, fill=COLORE_SILHOUETTE, outline="")
            else:
                self.create_polygon(appiattisci(dati), fill=COLORE_SILHOUETTE, outline="")

        for id_gruppo, poligoni in REGIONI[self.vista].items():
            for punti in poligoni:
                # tags=(id_gruppo,): "etichetta" che permette di trattare insieme
                # il muscolo sinistro e il destro
                self.create_polygon(appiattisci(punti), fill=self._colore_base(id_gruppo),
                                    outline=COLORE_SFONDO, width=2, tags=(id_gruppo,))
            # g=id_gruppo serve per "congelare" il valore dentro la lambda
            self.tag_bind(id_gruppo, "<Enter>", lambda e, g=id_gruppo: self._entra(g))
            self.tag_bind(id_gruppo, "<Leave>", lambda e, g=id_gruppo: self._esci(g))
            self.tag_bind(id_gruppo, "<Button-1>", lambda e, g=id_gruppo: self._clicca(g))

    def cambia_vista(self):
        self.vista = "retro" if self.vista == "fronte" else "fronte"
        self.disegna()

    # ---- metodi interni (il "_" davanti significa "uso interno") ----
    def _colore_base(self, id_gruppo):
        return COLORE_SELEZIONATO if id_gruppo == self.selezionato else COLORE_MUSCOLO

    def _entra(self, id_gruppo):
        self.itemconfig(id_gruppo, fill=COLORE_HOVER)
        self.config(cursor="hand2")
        if self.on_hover:
            self.on_hover(id_gruppo)

    def _esci(self, id_gruppo):
        self.itemconfig(id_gruppo, fill=self._colore_base(id_gruppo))
        self.config(cursor="")
        if self.on_hover:
            self.on_hover(None)

    def _clicca(self, id_gruppo):
        self.selezionato = id_gruppo
        for g in REGIONI[self.vista]:
            self.itemconfig(g, fill=self._colore_base(g))
        if self.on_click:
            self.on_click(id_gruppo)
