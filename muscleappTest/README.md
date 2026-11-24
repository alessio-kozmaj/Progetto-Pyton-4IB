# Atlante muscolare - progetto tkinter

Avvio:  `python main.py`   (serve Python 3 con tkinter; su Windows/Mac c'e' gia')

## Struttura

```
muscle_app/
  main.py            avvio
  app.py             finestra principale, collega i pezzi
  modelli.py         classi: Esercizio, GruppoMuscolare, VoceScheda
  dati.py            legge data/muscoli.json
  scheda.py          logica della scheda, salva data/scheda.json
  regioni.py         coordinate dei poligoni del corpo
  ui_corpo.py        Canvas cliccabile (hover, click, gira)
  ui_pannello.py     pannello info muscolo + esercizi
  ui_scheda.py       tabella della scheda
  data/muscoli.json  muscoli ed esercizi
  tools/trova_coordinate.py   aiuto per tracciare i poligoni su un'immagine
```

## Chi fa cosa

| Persona A (grafica del corpo) | Persona B (dati e scheda) |
|---|---|
| regioni.py, ui_corpo.py | dati.py, scheda.py, data/muscoli.json |
| estetica di app.py (colori, layout) | ui_pannello.py, ui_scheda.py |

## Il "contratto" (non cambiare senza dirlo all'altro)

1. `modelli.py`: nomi delle classi e dei loro attributi.
2. L'`id` di un muscolo (es. "pettorali") e' uguale in `regioni.py` e in `muscoli.json`.
3. `ui_corpo.VistaCorpo(parent, on_hover, on_click)`: le callback ricevono l'id (o None).
4. `dati.get_gruppo(id)` e `dati.get_tutti_i_gruppi()`.
5. `Scheda.aggiungi(voce)`, `Scheda.rimuovi(indice)`, `Scheda.voci`.
6. `PannelloInfo.mostra_gruppo(gruppo)` e `PannelloScheda.aggiorna()`.

## Regole per non fare casino

- Ognuno modifica SOLO i propri file. `modelli.py` e `app.py` (la logica di collegamento) si toccano solo dopo averne parlato.
- Usate Git/GitHub: commit piccoli e frequenti, `git pull` prima di iniziare a lavorare.
- Se serve un nuovo dato (es. "difficolta'" dell'esercizio): si aggiunge in `modelli.py` -> `muscoli.json` -> `dati.py` -> interfaccia, in quest'ordine.
