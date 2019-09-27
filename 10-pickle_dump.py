import pickle
game_data = {
    'позиция-игрока' : 'C23 B45',
    'карманы' : ['ключи', 'карманный нож', 'гладкий камень'],
    'рюкзак' : ['веревка', 'молоток', 'яблоко'],
    'деньги' : 158.50
    }
save_file = open('d:\\save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()
