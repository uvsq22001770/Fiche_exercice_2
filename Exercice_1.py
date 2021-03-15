import tkinter as tk
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


racine.mainloop()

"""import tkinter as tk
import random as rd

WIDTH = 600
HEIGHT = 400
pause = False

def demarrer():
    global pause
    if pause == False:
        mouvement()
        bouton.config(text="Arrêter")
        pause = True
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
        pause = False


def creer_balle(x0, y0, x1, y1, largeur, hauteur):

    x, y = x0 + largeur // 2, y0 + hauteur // 2
    dx = rd.randint(1, 7)
    dy = rd.randint(1, 7)
    if hauteur > largeur :
        rayon = largeur // 10
    else:
        rayon = hauteurv // 10
    cercle = canvas.create_oval((x-rayon, y-rayon), (x+rayon, y+rayon), fill="blue")
    return [cercle, dx, dy]


def mouvement(b):
    global id_after
    canvas.move(b[0], b[1], b[2])
    id_after = canvas.after(20, lambda: mouvement(b))
    rebond1(b)


def rebond1():

    for i in range(0, len(liste)):
        x0, y0, x1, y1 = canvas.coords(liste[i][0])
        if x0 <= liste[i][3] or x1 >= liste[i][5]:
            liste[i][1] = -liste[i][1]
        if y0 <= liste[i][4] or y1 >= liste[i][6]:
            liste[i][2] = -liste[i][2]

def creer_rectangle(x0, y0, x1, y1):

    canvas.create_rectangle((x0, y0), (x1, y1), outline= "white")
    creer_balle(x0, y0, x1, y1)

def quadrillage(n, m):


# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=WIDTH, height=HEIGHT)
canvas.grid()
bouton = tk.Button(racine, text="Démarrer", command=start)
bouton.grid(row=1)
x0 = 250
y0 = 150
x1 = 375
y1 = 275
rectangle = creer_rectangle(x0, y0, x1, y1)
balle = creer_balle(x0, y0, x1, y1)

racine.mainloop()"""