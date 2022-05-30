from BoardItem import *

class Banana(BoardItem):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = p.image.load('snake_imgs/banana.svg')

    def eat(self, snake, otherSnakes):
        snake.bananas += 1
        snake.globalScore += 3
        snake.increaseSize()