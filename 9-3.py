file1 = open('d:\\1.txt')
file2 = open('d:\\2.txt', 'w')
file2.write(str(file1.read()))
file2.close()
print('f2.close')
file1.close()

