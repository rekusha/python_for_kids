import pickle

file1 = open('d:\\10-2.dat', 'rb')
mylist = pickle.load(file1)
file1.close()

print(mylist)
