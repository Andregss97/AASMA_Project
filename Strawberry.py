from BoardItem import *

class Strawberry(BoardItem):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = p.image.load('snake_imgs/strawberry.svg')

    def eat(self, snake, otherSnakes):
        snake.strawberries += 1
        snake.globalScore += 5
        snake.increaseSize()