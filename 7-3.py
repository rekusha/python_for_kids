import sys
def moon_weight():
    print('ves')
    weight = int(sys.stdin.readline()) 
    print('koef')
    koeff = int(sys.stdin.readline())
    print('years')
    years = int(sys.stdin.readline())
    for x in range(1, years+1):
        print('%s %s' % (x, (x+weight)*koeff))
moon_weight()
