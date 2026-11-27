import tkinter as tk
import webbrowser
import dati
from PIL import Image, ImageTk

def avvia_app():
    finestra = tk.Tk()
    finestra.title("Atlante muscolare e scheda di allenamento")
    finestra.geometry("950x750")
    finestra.configure(bg="#1e1e2e")

    pannello_sinistro = tk.Frame(finestra, bg="#1e1e2e", width=350)
    pannello_sinistro.pack(side="left", fill="y", padx=10, pady=10)
    pannello_sinistro.pack_propagate(False)

    tk.Label(pannello_sinistro, text="Atlante", bg="#1e1e2e", fg="white", font=("Arial", 16, "bold")).pack(pady=5)

    canvas = tk.Canvas(pannello_sinistro, bg="#1e1e2e", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    pannello_destro = tk.Frame(finestra, bg="#282a36")
    pannello_destro.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    label_titolo = tk.Label(pannello_destro, text="Seleziona un muscolo", bg="#282a36", fg="white", font=("Arial", 20, "bold"))
    label_titolo.pack(pady=20)
    
    label_funzione = tk.Label(pannello_destro, text="Passa il mouse sul corpo e clicca su un gruppo muscolare.", bg="#282a36", fg="#a6accd", wraplength=450, justify="left")
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

    def hover_entra(event):
        item_id = canvas.find_withtag("current")
        if item_id:
            canvas.itemconfig(item_id[0], outline="#ffb86c", width=3)

    def hover_esce(event):
        item_id = canvas.find_withtag("current")
        if item_id:
            canvas.itemconfig(item_id[0], outline="red", width=1)

    def crea_zona(coordinate, tag):
        poly_id = canvas.create_polygon(coordinate, fill="", outline="red", width=1, tags=tag)
        canvas.tag_bind(tag, "<Enter>", hover_entra)
        canvas.tag_bind(tag, "<Leave>", hover_esce)
        return poly_id

    def disegna_zone(vista):
        canvas.delete("all") 
        
        if vista == "fronte":
            canvas.create_image(0, 0, anchor="nw", image=img_fronte_tk)
            
            # PETTORALI (coordinate tue, precise!)
            crea_zona([129, 156, 157, 164, 158, 209, 136, 218, 109, 189], "pettorali") # Sinistro
            crea_zona([193, 157, 217, 190, 198, 218, 169, 209, 169, 167], "pettorali") # Destro
            
            # Le altre zone sono ancora stimate (da sistemare con il picker)
            crea_zona([120, 225, 180, 225, 170, 340, 130, 340], "addominali")
            crea_zona([70, 140, 110, 150, 110, 190, 70, 180], "spalle")
            crea_zona([190, 150, 230, 140, 230, 180, 190, 190], "spalle")
            crea_zona([60, 180, 100, 190, 100, 280, 60, 270], "bicipiti")
            crea_zona([200, 190, 240, 180, 240, 270, 200, 280], "bicipiti")
            crea_zona([110, 390, 145, 390, 145, 530, 110, 530], "quadricipiti")
            crea_zona([155, 390, 190, 390, 190, 530, 155, 530], "quadricipiti")
            crea_zona([110, 540, 145, 540, 145, 630, 110, 630], "polpacci")
            crea_zona([155, 540, 190, 540, 190, 630, 155, 630], "polpacci")

        else: # retro
            canvas.create_image(0, 0, anchor="nw", image=img_retro_tk)
            crea_zona([80, 130, 220, 130, 190, 300, 110, 300], "dorsali")
            crea_zona([110, 300, 190, 300, 180, 400, 120, 400], "glutei")
            crea_zona([60, 170, 100, 170, 100, 280, 60, 270], "tricipiti")
            crea_zona([200, 170, 240, 170, 240, 270, 200, 280], "tricipiti")
            crea_zona([110, 410, 145, 410, 145, 530, 110, 530], "femorali")
            crea_zona([155, 410, 190, 410, 190, 530, 155, 530], "femorali")
            crea_zona([110, 540, 145, 540, 145, 630, 110, 630], "polpacci")
            crea_zona([155, 540, 190, 540, 190, 630, 155, 630], "polpacci")

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
        canvas.create_text(150, 200, text="Errore nel caricamento immagini!", fill="white", font=("Arial", 12))
        print("Errore dettagliato:", e)

    canvas.bind("<Button-1>", quando_clicchi)
    finestra.mainloop()

if __name__ == "__main__":
    avvia_app()