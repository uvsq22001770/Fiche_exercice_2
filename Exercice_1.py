"""import tkinter as tk
import random as rd

demarrer = 1

def start():
    global demarrer
    if demarrer:
        mouvement(balle)
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    demarrer = 1 - demarrer


def creer_balle():
    x, y = 300, 200
    r = 20
    cercle = canvas.create_oval((x-r, y-r), (x+r, y+r), fill="blue")
    dx = rd.randint(1, 7)
    dy = rd.randint(1, 7)
    return [cercle, dx, dy]


def mouvement(b):
    global id_after
    canvas.move(b[0], b[1], b[2])
    id_after = canvas.after(20, lambda: mouvement(b))
    rebond1(b)


def rebond1(b):
    x0, y0, x1, y1 = canvas.coords(b[0])
    if x0 <= 0 or x1 >= 600:
        b[1] = -b[1]
    if y0 <= 0 or y1 >= 400:
        b[2] = -b[2]


# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
bouton = tk.Button(racine, text="Démarrer", command=start)
bouton.grid(row=1)
balle = creer_balle()


racine.mainloop()"""

import tkinter as tk
import random as rd

WIDTH = 600
HEIGHT = 400
demarrer = 1

def start():
    global demarrer
    if demarrer:
        mouvement(balle)
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    demarrer = 1 - demarrer


def creer_balle():
    """création de la balle"""
    global cercle
    x, y = 300, 200
    r = 2
    cercle = canvas.create_oval((x-r, y-r), (x+r, y+r), fill="blue")
    dx = rd.randint(1, 7)
    dy = rd.randint(1, 7)
    return [cercle, dx, dy]


def mouvement(b):
    global id_after
    canvas.move(b[0], b[1], b[2])
    id_after = canvas.after(20, lambda: mouvement(b))
    rebond1(b)


def rebond1(b):
    """rebond"""
    x0, y0, x1, y1 = canvas.coords(b[0])
    if x0 <= 0 or x1 >= 600:
        b[1] = -b[1]
    if y0 <= 0 or y1 >= 400:
        b[2] = -b[2]

def creer_rectangle(x0, y0, x1, y1):
    """création du rectangle"""
    global ballon
    canvas.create_rectangle((x0, y0), (x1, y1), outline = "white")
    ballon = creer_balle()
    return [ballon, x0, y0, x1, y1]

def quadrillage(n, m):
    """création du quadrillage"""
    creer_rectangle

# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=WIDTH, height=HEIGHT)
canvas.grid()
bouton = tk.Button(racine, text="Démarrer", command=start)
bouton.grid(row=1)
balle = creer_balle()
rectangle = creer_rectangle(200, 200, 350, 300)
print(rectangle)


racine.mainloop()