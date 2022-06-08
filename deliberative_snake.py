import pygame as p
import numpy as np
from pygame import Vector2
from board import *

VISION_RANGE = 5

class Deliberative_Snake:

    def __init__(self):
        self.color = "olivedrab"
        self.scanColor = "lemonchiffon3"
        self.visibleArea = []
        
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = p.Vector2(1, 0)
        self.size = len(self.body)
        # TODO: rearrange which snake goes where in the start
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

    def drawSnake (self, screen):
        for cell in self.body:
            x_pos = int(cell.x * SQUARE_SIZE)
            y_pos = int(cell.y * SQUARE_SIZE)
            cell_rect = p.Rect(x_pos, y_pos, SQUARE_SIZE, SQUARE_SIZE)

            p.draw.rect(screen, self.color, cell_rect)
    
    def moveSnake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def increaseSize(self):
        body_copy = self.body[:]
        body_copy.append(body_copy[-1])
        self.body = body_copy[:]

    def manhattanDistance (self, start: Vector2, end: Vector2):
        return np.abs(end.x - start.x) + np.abs(end.y - start.y) 

    def scanArea(self, screen):
        self.circleBres(self.body[0].x, self.body[0].y, screen)
        for i in range (DIMENSION):
            for j in range (DIMENSION):
                pos = p.Vector2(i,j)
                if np.round(self.manhattanDistance(self.body[0], pos), 0) <= VISION_RANGE and pos not in self.body and pos not in self.visibleArea:
                    self.visibleArea.append(pos)
        self.paintVision(screen)

    def paintVision(self, screen):
        for cell in self.visibleArea:
            p.draw.rect(screen, self.scanColor, p.Rect(cell.x * SQUARE_SIZE, cell.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drawCircle(self, xc: int, yc: int, x: int, y: int):
        self.visibleArea.append(p.Vector2(xc+x, yc+y))
        self.visibleArea.append(p.Vector2(xc-x, yc+y))
        self.visibleArea.append(p.Vector2(xc+x, yc-y))
        self.visibleArea.append(p.Vector2(xc-x, yc-y))
        self.visibleArea.append(p.Vector2(xc+y, yc+x))
        self.visibleArea.append(p.Vector2(xc-y, yc+x))
        self.visibleArea.append(p.Vector2(xc+y, yc-x))
        self.visibleArea.append(p.Vector2(xc-y, yc-x))

    def circleBres(self, xc: int, yc: int, screen):
        self.visibleArea = []
        x = 0
        y = VISION_RANGE
        d = 3 - 2 * VISION_RANGE
        self.drawCircle(xc, yc, x, y)
        while y >= x:
            x += 1
            if (d > 0):
                y -= 1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6;
            self.drawCircle(xc, yc, x, y)
