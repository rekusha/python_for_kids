import time, tkinter
tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.create_polygon(340, 110, 340, 160, 380, 135)
for x in range(0, 60):
    canvas.move(1, 5, 0)
    canvas.move(2, -5, 0)
    tk.update()
    time.sleep(0.05)
