import sys
x1 = "У какого слона нет хобота? У шахматного!"
x2 = sys.stdout.write(x1)
print(x2, '\n', x1)
print(x2 + 5)

#если используем sys.stdout.write("У какого") - получаем вывод строки
#если используем print(sys.stdout.write("У какого")) - получаем вывод строки + количество выведенных символов
