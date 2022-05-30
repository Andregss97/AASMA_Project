from BoardItem import *

class Ice(BoardItem):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = p.image.load('snake_imgs/ice.svg')

    def eat(self, snake, otherSnakes):
        # print("ICE *__*")
        snake.ices += 1
        for s in otherSnakes:
            s.freeze()
