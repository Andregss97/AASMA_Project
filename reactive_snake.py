import pygame as p
from pygame import Vector2
from board import *

class Reactive_Snake:

    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = p.Vector2(1, 0)
        self.globalScore = 0

        # F R U I T S
        self.apples = 0
        self.bananas = 0
        self.strawberries = 0

        # T R A P S
        self.mushrooms = 0
        self.ices = 0

        # D I S P E N S E R
        self.dispenser = 0
        # shared_dispenser = 0
        # TODO: Criar várias cobras e identificar estes eventos

    def getBody(self):
        return self.body

    def drawSnake (self, screen):
        for cell in self.body:
            x_pos = int(cell.x * SQUARE_SIZE)
            y_pos = int(cell.y * SQUARE_SIZE)
            cell_rect = p.Rect(x_pos, y_pos, SQUARE_SIZE, SQUARE_SIZE)

            p.draw.rect(screen, "orange2", cell_rect)
    
    def moveSnake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def increaseSize(self):
        body_copy = self.body[:]
        body_copy.append(body_copy[-1])
        self.body = body_copy[:]

