from tkinter import *
import tkinter.colorchooser
import random
tk=Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, x2, y1, y2, fill = fill_color)
c = tkinter.colorchooser.askcolor()
random_rectangle(400, 400, c[1])
