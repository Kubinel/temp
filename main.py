import tkinter as tk
import random  # Potrebujeme na náhodné umiestnenie jablka

WIDTH = 400
HEIGHT = 400
SIZE = 20

root = tk.Tk()
root.title("Had")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

had = [
    (100, 100),
    (80, 100),
    (60, 100)
]

smer = "Dole"

# Globálne premenné pre pozíciu jablka
jablko_x = 0
jablko_y = 0

def generuj_jablko():
    global jablko_x, jablko_y
    # Vygeneruje náhodné súradnice, ktoré sú násobkami veľkosti SIZE
    jablko_x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
    jablko_y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE

def draw():
    canvas.delete("had")
    canvas.delete("jablko")  # Najprv vymažeme staré jablko
    
    # Vykreslenie jablka (zelený kruh)
    canvas.create_oval(jablko_x, jablko_y, jablko_x + SIZE, jablko_y + SIZE, fill="green", tag="jablko")
    
    # Vykreslenie hada (červené štvorce)
    for x, y in had:
        canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill="red", tag="had")

def move():
    global jablko_x, jablko_y, my_run
    
    hlava_x, hlava_y = had[0]
    if smer == "Vpravo":
        nova_hlava = (hlava_x + SIZE, hlava_y)
    elif smer == "Vlavo":
        nova_hlava = (hlava_x - SIZE, hlava_y)
    elif smer == "Hore":
        nova_hlava = (hlava_x, hlava_y - SIZE)
    elif smer == "Dole":
        nova_hlava = (hlava_x, hlava_y + SIZE)
        
    had.insert(0, nova_hlava)

    while nova_hlava in had[1:]:
        had.pop()

    if nova_hlava[0] > WIDTH:
        root.after_cancel(my_run)
    
    # KONTROLA: Zjedol had jablko?
    if nova_hlava == (jablko_x, jablko_y):
        generuj_jablko()  # Ak áno, vytvor nové jablko a NEmaž chvost (had narastie)
    else:
        had.pop()         # Ak nie, had sa len posunie (zmaže sa posledný článok)

def zmen_smer(event):
    global smer

    if event.keysym == "Up" and smer != "Dole":
        smer = "Hore"
    elif event.keysym == "Down" and smer != "Hore":
        smer = "Dole"
    elif event.keysym == "Right" and smer != "Vlavo":
        smer = "Vpravo"
    elif event.keysym == "Left" and smer != "Vpravo":
        smer = "Vlavo"

my_run = None

def game_over():
    hlava = had[0]
    
    
   
def game_loop():
    global my_run
    move()
    draw()
    my_run = canvas.after(200, game_loop)

root.bind("<Key>", zmen_smer)

# Vygenerujeme prvé jablko ešte pred spustením hlavnej slučky
generuj_jablko()

game_loop()

root.mainloop()
