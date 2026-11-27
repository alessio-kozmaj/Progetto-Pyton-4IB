import tkinter as tk
import webbrowser
import dati
from PIL import Image, ImageTk
import tkinter.font as tkfont

def avvia_app():
    finestra = tk.Tk()
    finestra.title("Atlante muscolare e scheda di allenamento")
    finestra.geometry("1100x800")
    finestra.configure(bg="#1e1e2e")

    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=13)

    pannello_sinistro = tk.Frame(finestra, bg="#1e1e2e", width=450)
    pannello_sinistro.pack(side="left", fill="y", padx=10, pady=10)
    pannello_sinistro.pack_propagate(False)

    tk.Label(pannello_sinistro, text="Atlante", bg="#1e1e2e", fg="white", font=tkfont.Font(size=20, weight="bold")).pack(pady=10)

    canvas = tk.Canvas(pannello_sinistro, bg="#1e1e2e", highlightthickness=0)
    canvas.pack(fill="both", expand=True, padx=(75, 0)) 

    pannello_destro = tk.Frame(finestra, bg="#282a36")
    pannello_destro.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    card_info = tk.Frame(pannello_destro, bg="#1e1e2e", padx=20, pady=20)
    card_info.pack(fill="x", pady=(0, 20))

    label_titolo = tk.Label(card_info, text="Seleziona un muscolo", bg="#1e1e2e", fg="white", font=tkfont.Font(size=28, weight="bold"))
    label_titolo.pack(pady=(0, 10))
    
    label_funzione = tk.Label(card_info, text="Passa il mouse sul corpo e clicca su un gruppo muscolare.", bg="#1e1e2e", fg="#a6accd", wraplength=600, justify="center", font=tkfont.Font(size=14))
    label_funzione.pack()

    frame_esercizi = tk.Frame(pannello_destro, bg="#282a36")
    frame_esercizi.pack(fill="both", expand=True)

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
            canvas.create_image(0, 0, anchor="nw", image=img_fronte_tk)
            
            crea_zona([129, 156, 157, 164, 158, 209, 136, 218, 109, 189], "pettorali") 
            crea_zona([193, 157, 217, 190, 198, 218, 169, 209, 169, 167], "pettorali") 
            crea_zona([85, 198, 102, 186, 122, 152, 104, 152, 90, 163, 85, 178, 85, 195], "spalle") 
            crea_zona([201, 154, 223, 186, 239, 198, 238, 179, 234, 166, 226, 155, 221, 152, 210, 150, 201, 153], "spalle") 
            crea_zona([87, 205, 79, 229, 84, 264, 99, 240, 106, 221, 104, 202, 102, 191, 88, 202], "bicipiti") 
            crea_zona([222, 192, 220, 214, 224, 232, 230, 249, 241, 264, 246, 250, 246, 235, 244, 220, 239, 208, 222, 192], "bicipiti") 
            crea_zona([75, 252, 63, 277, 63, 305, 55, 332, 68, 337, 83, 304, 89, 288, 92, 263, 82, 270, 77, 253], "avambracci") 
            crea_zona([229, 262, 237, 288, 246, 308, 256, 333, 270, 332, 261, 308, 262, 281, 249, 253, 245, 275, 230, 262], "avambracci") 
            crea_zona([108, 202, 120, 252, 118, 293, 144, 313, 162, 321, 181, 314, 206, 297, 203, 255, 213, 226, 214, 207, 199, 222, 188, 225, 165, 218, 136, 223, 109, 204], "addominali")
            crea_zona([114, 332, 107, 357, 105, 387, 108, 417, 116, 443, 129, 455, 139, 448, 149, 420, 155, 395, 156, 379, 155, 369, 122, 334], "quadricipiti") 
            crea_zona([172, 368, 195, 345, 210, 332, 220, 371, 218, 408, 210, 440, 198, 455, 187, 452, 180, 431, 169, 406, 169, 371], "quadricipiti") 
            crea_zona([110, 472, 106, 500, 111, 532, 117, 578, 131, 580, 130, 555, 140, 521, 139, 479, 112, 474], "polpacci") 
            crea_zona([210, 473, 218, 503, 213, 543, 210, 583, 191, 583, 190, 542, 181, 522, 187, 477, 205, 474], "polpacci") 

        else:
            canvas.create_image(0, 0, anchor="nw", image=img_retro_tk)

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
                    riga = tk.Frame(frame_esercizi, bg="#1e1e2e", padx=15, pady=15)
                    riga.pack(fill="x", pady=5)
                    
                    tk.Label(riga, text=es["nome"], bg="#1e1e2e", fg="#ffb86c", font=tkfont.Font(size=16, weight="bold"), anchor="w").pack(fill="x")
                    
                    tk.Label(riga, text=es["descrizione"], bg="#1e1e2e", fg="white", wraplength=600, justify="left", anchor="w", font=tkfont.Font(size=13)).pack(fill="x", pady=5)
                    
                    btn_video = tk.Button(riga, text="Guarda video", bg="#6272a4", fg="white", font=tkfont.Font(size=11, weight="bold"),
                                          padx=10, pady=5, relief="flat", cursor="hand2",
                                          command=lambda url=es["video_url"]: webbrowser.open(url))
                    btn_video.pack(anchor="w", pady=(5, 0))

    btn_gira = tk.Button(pannello_sinistro, text="Gira (fronte/retro)", command=gira_vista, bg="#44475a", fg="white", padx=10, pady=5, relief="flat", cursor="hand2", font=tkfont.Font(size=12))
    btn_gira.pack(pady=10)

    try:
        img_fronte_tk = carica_immagine("immagini/fronte.png", 300, 650)
        img_retro_tk = carica_immagine("immagini/retro.png", 300, 650)
        disegna_zone("fronte")
    except Exception as e:
        canvas.create_text(150, 200, text="Errore nel caricamento immagini!", fill="white")
        print("Errore dettagliato:", e)

    canvas.bind("<Button-1>", quando_clicchi)
    finestra.mainloop()

if __name__ == "__main__":
    avvia_app()