from BoardItem import *

class Apple(BoardItem):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = p.image.load('snake_imgs/apple.svg')

    def eat(self, snake, otherSnakes):
        snake.apples += 1
        snake.globalScore += 2
        snake.increaseSize()