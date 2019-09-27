import tkinter, random
tk = tkinter.Tk()
tk_width = 400
tk_height = 400
canvas = tkinter.Canvas(tk, width = tk_width, height = tk_height)
canvas.pack()
x = 0
y = 0
triangle_size = 50
color = ['red', 'green', 'blue', 'yellow', 'brown', 'white', 'orange', 'pink']
while y <= (tk_height - triangle_size):
    while x <= (tk_width - (triangle_size / 2)):
        s = canvas.create_polygon(x, y, x+triangle_size, y, x+triangle_size/2, y+triangle_size)
        canvas.itemconfig(s, fill = random.choice(color))
        x += triangle_size
    x = 0
    y += triangle_size
