import pickle
load_file = open('d:\\save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)
