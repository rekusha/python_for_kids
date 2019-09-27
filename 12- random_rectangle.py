from tkinter import *
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

for x in range(100):
    random_rectangle(400, 400, random.choice(['#00FF00', '#FF0000', '#0000FF', '#808080', '#FFFF00', '#FF00FF', '#800080', '#008080', '#000080', '#00FFFF']))
