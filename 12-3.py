import tkinter, time
tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width = 800, height=800)
canvas.pack()
my_image = tkinter.PhotoImage(file = '.\\RR.gif')
s = canvas.create_image(0, 0, anchor='nw', image=my_image)
for x in range(400):
    canvas.move(s, 1, 1)
    tk.update()
    time.sleep(0.01)
