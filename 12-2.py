import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
s = canvas.create_polygon(10, 10, 10, 60, 50, 35)
def animate_move(xx, yy):
    for x in range(60):
        canvas.move(s, xx, yy)
        tk.update()
        time.sleep(0.05)
animate_move(5, 0)
animate_move(0, 5)
animate_move(-5, 0)
animate_move(0, -5)

