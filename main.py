import tkinter as tk

WIDTH = 400
HEIGHT = 400
SIZE = 20

root = tk.Tk()
root.title("Had")

canvas = tk.Canvas(root, width=WIDTH,
                   height=HEIGHT, bg="lightblue")
canvas.pack()

had = [
    (100,100),
    (80,100),
    (60,100)
    ]

smer = "Dole"

def draw():
    canvas.delete("had")
    for x,y in had:
        canvas.create_rectangle(x,y, x+SIZE, y+SIZE,
                            fill="red", tag="had")

def move():
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
    had.pop()

def zmen_smer(event):
    global smer

    if event.keysym == "Up":
        smer = "Hore"
    elif event.keysym == "Down":
        smer = "Dole"
    elif event.keysym == "Right":
        smer = "Vpravo"
    elif event.keysym == "Left":
        smer = "Vlavo"
        
def game_loop():
    move()
    draw()

    canvas.after(200, game_loop)

root.bind("<Key>", zmen_smer)

game_loop()

root.mainloop()
