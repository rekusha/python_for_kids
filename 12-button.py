from tkinter import * #Конструкция from <имя модуля> import * позволяет обращаться к содержимому модуля, не указывая каждый раз его имя

def hello():
    print('Privet')
tk =Tk()
btn = Button(tk, text='click me', command=hello)
btn.pack()
