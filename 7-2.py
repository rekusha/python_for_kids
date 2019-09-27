def moon_weight(weight, koeff, years):
    for x in range(1, years+1):
        print('%s %s' % (x, (x+weight)*koeff))
moon_weight(30, 0.25, 5)
