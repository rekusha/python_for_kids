import turtle

t = turtle.Pen()
for x in range(18):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
