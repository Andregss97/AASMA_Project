from BoardItem import *
import pygame as p

WIDTH = HEIGHT = 600 # 900
DIMENSION = 20 # 30
SQUARE_SIZE = HEIGHT // DIMENSION

class Dispenser(BoardItem): #useless?

    def __init__(self, pos):
        super().__init__(pos)
        self.image = p.image.load('snake_imgs/cooldown.svg')

    def draw(self, screen):
        p.draw.rect(screen, p.Color("hotpink1"), p.Rect(self.pos.x * SQUARE_SIZE, self.pos.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    def eat(self, snake, snakes): #TODO: do dispenser things
        pass