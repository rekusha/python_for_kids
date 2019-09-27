import time
import sys
def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    return t2-t1

def lots_of_numbers2(max):
    t1 = time.time()
    for x in range(0, max):
        sys.stdout.write(str(x)+'\n')
    t2 = time.time()
    return t2-t1

print('Прошло %s секунд' % (lots_of_numbers(1000)))
print('Прошло %s секунд' % (lots_of_numbers2(1000)))


