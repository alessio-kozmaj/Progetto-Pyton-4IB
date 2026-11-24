"""
Strumento per quando avrete un'immagine vera del corpo (formato PNG).
Uso:   python tools/trova_coordinate.py percorso/immagine.png
Cliccate sui punti del contorno di un muscolo: le coordinate (x, y) vengono
stampate nel terminale, pronte da copiare dentro regioni.py.
"""
import sys
import tkinter as tk

if len(sys.argv) < 2:
    print("Uso: python tools/trova_coordinate.py immagine.png")
    sys.exit(1)

root = tk.Tk()
img = tk.PhotoImage(file=sys.argv[1])
canvas = tk.Canvas(root, width=img.width(), height=img.height())
canvas.pack()
canvas.create_image(0, 0, image=img, anchor="nw")


def click(evento):
    canvas.create_oval(evento.x - 3, evento.y - 3, evento.x + 3, evento.y + 3, fill="red")
    print(f"({evento.x}, {evento.y}),")


canvas.bind("<Button-1>", click)
root.mainloop()
