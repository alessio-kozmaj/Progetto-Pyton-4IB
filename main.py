import tkinter as tk

def avvia_app():
    finestra = tk.Tk()
    finestra.title("Atlante muscolare e scheda di allenamento")
    finestra.geometry("950x750")
    finestra.configure(bg="#1e1e2e")

    # --- PANNELLO SINISTRO (per la figura) ---
    pannello_sinistro = tk.Frame(finestra, bg="#1e1e2e", width=350)
    pannello_sinistro.pack(side="left", fill="y", padx=10, pady=10)
    pannello_sinistro.pack_propagate(False) # impedisce al frame di rimpicciolirsi

    # Titolo del pannello sinistro
    tk.Label(pannello_sinistro, text="Atlante", bg="#1e1e2e", fg="white", font=("Arial", 16, "bold")).pack(pady=10)

    # --- PANNELLO DESTRO (per i dettagli e la scheda) ---
    pannello_destro = tk.Frame(finestra, bg="#282a36")
    pannello_destro.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Testo di benvenuto nel pannello destro
    tk.Label(pannello_destro, text="Seleziona un muscolo", bg="#282a36", fg="white", font=("Arial", 20, "bold")).pack(pady=50)
    tk.Label(pannello_destro, text="Passa il mouse sul corpo e clicca su un gruppo muscolare.", bg="#282a36", fg="#a6accd").pack()

    finestra.mainloop()

if __name__ == "__main__":
    avvia_app()