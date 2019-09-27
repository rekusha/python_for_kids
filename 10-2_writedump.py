import pickle

mylist = ['40', 'тысяч', 'обезьян', 'что-то', 'делали', 'банан']
file1 = open('d:\\10-2.dat', 'wb')
pickle.dump(mylist, file1)
file1.close()
