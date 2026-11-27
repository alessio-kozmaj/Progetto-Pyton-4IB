import tkinter as tk
import webbrowser
import dati
from PIL import Image, ImageTk

def avvia_app():
    finestra = tk.Tk()
    finestra.title("Atlante muscolare e scheda di allenamento")
    finestra.geometry("1050x750") # Ho allargato la finestra totale per non stringere troppo il pannello destro
    finestra.configure(bg="#1e1e2e")

    # --- PANNELLO SINISTRO (Larghezza 500) ---
    pannello_sinistro = tk.Frame(finestra, bg="#1e1e2e", width=500)
    pannello_sinistro.pack(side="left", fill="y", padx=10, pady=10)
    pannello_sinistro.pack_propagate(False)

    tk.Label(pannello_sinistro, text="Atlante", bg="#1e1e2e", fg="white", font=("Arial", 16, "bold")).pack(pady=5)

    canvas = tk.Canvas(pannello_sinistro, bg="#1e1e2e", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # --- PANNELLO DESTRO ---
    pannello_destro = tk.Frame(finestra, bg="#282a36")
    pannello_destro.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    label_titolo = tk.Label(pannello_destro, text="Seleziona un muscolo", bg="#282a36", fg="white", font=("Arial", 20, "bold"))
    label_titolo.pack(pady=20)
    
    label_funzione = tk.Label(pannello_destro, text="Passa il mouse sul corpo e clicca su un gruppo muscolare.", bg="#282a36", fg="#a6accd", wraplength=400, justify="left")
    label_funzione.pack(pady=10)

    frame_esercizi = tk.Frame(pannello_destro, bg="#282a36")
    frame_esercizi.pack(fill="both", expand=True, pady=10)

    img_fronte_tk = None
    img_retro_tk = None
    vista_attuale = "fronte"

    def carica_immagine(percorso, larghezza, altezza):
        img = Image.open(percorso)
        img = img.resize((larghezza, altezza), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    def crea_zona(coordinate, tag):
        poly_id = canvas.create_polygon(coordinate, fill="", outline="", tags=tag)
        return poly_id

    def disegna_zone(vista):
        canvas.delete("all") 
        
        if vista == "fronte":
            # Immagine centrata a X=100 (100 + 300 + 100 = 500)
            canvas.create_image(100, 0, anchor="nw", image=img_fronte_tk)
            
            # --- COORDINATE FRONTE (Spostate di +100 su X) ---
            crea_zona([229, 156, 257, 164, 258, 209, 236, 218, 209, 189], "pettorali") # Sx
            crea_zona([293, 157, 317, 190, 298, 218, 269, 209, 269, 167], "pettorali") # Dx
            
            crea_zona([185, 198, 202, 186, 222, 152, 204, 152, 190, 163, 185, 178, 185, 195], "spalle") # Sx
            crea_zona([301, 154, 323, 186, 339, 198, 338, 179, 334, 166, 326, 155, 321, 152, 310, 150, 301, 153], "spalle") # Dx
            
            crea_zona([187, 205, 179, 229, 184, 264, 199, 240, 206, 221, 204, 202, 202, 191, 188, 202], "bicipiti") # Sx
            crea_zona([322, 192, 320, 214, 324, 232, 330, 249, 341, 264, 346, 250, 346, 235, 344, 220, 339, 208, 322, 192], "bicipiti") # Dx
            
            crea_zona([175, 252, 163, 277, 163, 305, 155, 332, 168, 337, 183, 304, 189, 288, 192, 263, 182, 270, 177, 253], "avambracci") # Sx
            crea_zona([329, 262, 337, 288, 346, 308, 356, 333, 370, 332, 361, 308, 362, 281, 349, 253, 345, 275, 330, 262], "avambracci") # Dx
            
            crea_zona([208, 202, 220, 252, 218, 293, 244, 313, 262, 321, 281, 314, 306, 297, 303, 255, 313, 226, 314, 207, 299, 222, 288, 225, 265, 218, 236, 223, 209, 204], "addominali")
            
            crea_zona([214, 332, 207, 357, 205, 387, 208, 417, 216, 443, 229, 455, 239, 448, 249, 420, 255, 395, 256, 379, 255, 369, 222, 334], "quadricipiti") # Sx
            crea_zona([272, 368, 295, 345, 310, 332, 320, 371, 318, 408, 310, 440, 298, 455, 287, 452, 280, 431, 269, 406, 269, 371], "quadricipiti") # Dx
            
            crea_zona([210, 472, 206, 500, 211, 532, 217, 578, 231, 580, 230, 555, 240, 521, 239, 479, 212, 474], "polpacci") # Sx
            crea_zona([310, 473, 318, 503, 313, 543, 310, 583, 291, 583, 290, 542, 281, 522, 287, 477, 305, 474], "polpacci") # Dx

        else:
            canvas.create_image(100, 0, anchor="nw", image=img_retro_tk)
            # Retro da fare

    def gira_vista():
        nonlocal vista_attuale
        if vista_attuale == "fronte":
            vista_attuale = "retro"
            btn_gira.config(text="Gira (retro/fronte)")
        else:
            vista_attuale = "fronte"
            btn_gira.config(text="Gira (fronte/retro)")
        disegna_zone(vista_attuale)

    def quando_clicchi(event):
        item_id = canvas.find_withtag("current")
        if not item_id:
            return
        tags = canvas.gettags(item_id[0])
        
        if tags:
            id_muscolo = tags[0]
            tutti_i_muscoli = dati.carica_muscoli()
            muscolo_trovato = None
            for m in tutti_i_muscoli:
                if m["id"] == id_muscolo:
                    muscolo_trovato = m
                    break
            
            if muscolo_trovato:
                label_titolo.config(text=muscolo_trovato["nome"])
                label_funzione.config(text=muscolo_trovato["funzione"])
                
                for widget in frame_esercizi.winfo_children():
                    widget.destroy()
                
                for es in muscolo_trovato["esercizi"]:
                    riga = tk.Frame(frame_esercizi, bg="#1e1e2e", pady=10, padx=10)
                    riga.pack(fill="x", pady=5)
                    
                    tk.Label(riga, text=es["nome"], bg="#1e1e2e", fg="#ffb86c", font=("Arial", 12, "bold"), anchor="w").pack(fill="x")
                    tk.Label(riga, text=es["descrizione"], bg="#1e1e2e", fg="white", wraplength=400, justify="left", anchor="w").pack(fill="x")
                    
                    btn_video = tk.Button(riga, text="Guarda video", bg="#6272a4", fg="white", 
                                          command=lambda url=es["video_url"]: webbrowser.open(url))
                    btn_video.pack(anchor="w", pady=5)

    btn_gira = tk.Button(pannello_sinistro, text="Gira (fronte/retro)", command=gira_vista, bg="#44475a", fg="white", font=("Arial", 10))
    btn_gira.pack(pady=10)

    try:
        img_fronte_tk = carica_immagine("immagini/fronte.png", 300, 650)
        img_retro_tk = carica_immagine("immagini/retro.png", 300, 650)
        disegna_zone("fronte")
    except Exception as e:
        canvas.create_text(250, 200, text="Errore nel caricamento immagini!", fill="white", font=("Arial", 12)) # Testo spostato a X=250 per centrarlo
        print("Errore dettagliato:", e)

    canvas.bind("<Button-1>", quando_clicchi)
    finestra.mainloop()

if __name__ == "__main__":
    avvia_app()