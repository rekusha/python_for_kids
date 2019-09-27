def moon_weight(weight, koeff):
    for x in range(1, 16):
        print('%s %s' % (x, (x+weight)*koeff))
moon_weight(30, 0.25)
