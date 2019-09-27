import turtle
def draw_star(size, points):
    t = turtle.Pen()
    angle = 180 - (180 / points)
    for i in range(points):
        t.forward(size)
        t.right(angle)

draw_star(200, 101)
