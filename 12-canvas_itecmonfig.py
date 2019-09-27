from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35) # получаем id объекта

canvas.move(1, 50, 0)
canvas.move(mytriangle, 0, 50) # используем id для движения

canvas.itemconfig(mytriangle, fill='red') # меняем свойства объекта по id
