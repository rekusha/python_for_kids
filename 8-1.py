class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит детенышей молоком')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('ест листья')
    def left_foot_forward(self):
        print('левая нога впереди')
    def left_foot_back(self):
        print('левая нога зади')
    def right_foot_forward(self):
        print('правая нога впереди')
    def right_foot_back(self):
        print('правая нога зади')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        
reginald = Giraffes()
reginald.dance()
