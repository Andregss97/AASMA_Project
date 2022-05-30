from BoardItem import *

class Mushroom(BoardItem):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = p.image.load('snake_imgs/mushroom.svg')

    def eat(self, snake, otherSnakes):
        # print("MUSHROOM >__<")
        snake.mushrooms += 1
        snake.globalScore -= 1
        for s in otherSnakes:
            s.globalScore -= 4

