import turtle
t = turtle.Pen()
def ris(filled, r, g, b):
    t.color(r, g, b)
    if filled == True:
        t.begin_fill()
    for x in range(8):
        t.forward(50)
        t.right(45)
    if filled == True:
        t.end_fill()

ris(True, 0.9, 0.75, 0)
ris(False, 0, 0, 0)
