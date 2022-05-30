from pygame import Vector2
from Board import *

WIDTH = HEIGHT = 600 # 900
DIMENSION = 20 # 30
SQUARE_SIZE = HEIGHT // DIMENSION

class BoardItem: # Abstract class

    def __init__(self, pos):
        self.pos = pos
        self.image = None

    def draw(self, screen):
        screen.blit(self.image, (self.pos.x * SQUARE_SIZE, self.pos.y * SQUARE_SIZE))

    def eat(self, snake, otherSnakes):
        pass