import tkinter as tk
import random as rd


#constantes
LONGUEUR = 600
LARGEUR = 400

#fonctions

def creer_balle():
    cercle_bleu = canvas.create_oval(290, 190, 310, 210, fill="blue")
    v = rd.randint(0,7)
    w = rd.randint(0,7)
    balle = []
    balle.append(290, 190, 310, 210, v, w)
    return cercle_bleu, balle

racine=tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=LARGEUR, width=LONGUEUR)
bouton = tk.Button(racine, text="Démarrer", font=("helvetica"))

canvas.grid(column=0, row=0, columnspan=2)
bouton.grid(column=0, row=1, columnspan=2)

racine.mainloop()