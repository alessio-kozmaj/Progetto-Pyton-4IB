import tkinter as tk
from PIL import Image, ImageTk

def avvia_picker():
    finestra = tk.Tk()
    finestra.title("Coordinate Picker - Clicca i vertici, tasto destro per finire")
    
    canvas = tk.Canvas(finestra, width=300, height=650, bg="black")
    canvas.pack()

    img = Image.open("immagini/retro.png") #Seleziona l'immagine da esaminare
    img = img.resize((300, 650), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor="nw", image=img_tk)

    punti = []

    def click_sinistro(event):
        x, y = event.x, event.y
        punti.append((x, y))
        # Disegna un pallino rosso
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="red")
        # Disegna la linea
        if len(punti) > 1:
            p1 = punti[-2]
            p2 = punti[-1]
            canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red", width=2)

    def click_destro(event):
        coordinate = []
        for p in punti:
            coordinate.extend(p)
        print("\nMettere nel main")
        print(f"crea_zona({coordinate}, \"nome_muscolo\")")
        finestra.destroy()

    canvas.bind("<Button-1>", click_sinistro) # Tasto sinistro aggiunge punto
    canvas.bind("<Button-3>", click_destro)   # Tasto destro stampa e chiude

    tk.Label(finestra, text="Sinistro: aggiungi punto. Destro: stampa e chiudi.").pack()
    finestra.mainloop()

if __name__ == "__main__":
    avvia_picker()