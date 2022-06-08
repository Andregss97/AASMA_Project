import pygame as p
import numpy as np
from pygame import Vector2
from board import *
import traps
import fruits

VISION_RANGE = 5

apple = p.image.load('snake_imgs/apple.svg')
banana = p.image.load('snake_imgs/banana.svg')
strawberry = p.image.load('snake_imgs/strawberry.svg')

mushroom = p.image.load('snake_imgs/mushroom.svg')
ice = p.image.load('snake_imgs/ice.svg')

cooldown = p.image.load('snake_imgs/cooldown.svg')

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
        self.applesScanned = []
        self.bananas = 0
        self.bananasScanned = []
        self.strawberries = 0
        self.strawberriesScanned = []

        # T R A P S
        self.mushrooms = 0
        self.mushroomsScanned = []
        self.ices = 0
        self.icesScanned = []

        # D I S P E N S E R
        self.dispenser = 0
        self.dispensersScanned = []
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

    def scanArea(self, screen, fruits, traps, dispensers):
        self.circleBres(self.body[0].x, self.body[0].y)
        for i in range (DIMENSION):
            for j in range (DIMENSION):
                pos = p.Vector2(i,j)
                if np.round(self.manhattanDistance(self.body[0], pos), 0) <= VISION_RANGE and pos not in self.body and pos not in self.visibleArea:
                    self.visibleArea.append(pos)
        self.paintVision(screen, fruits, traps, dispensers)

    def paintVision(self, screen, fruits, traps, dispensers):
        for cell in self.visibleArea:
            if cell in fruits.apples and cell not in self.applesScanned:
                self.applesScanned.append(cell)
            if cell in fruits.bananas and cell not in self.bananasScanned:
                self.bananasScanned.append(cell)
            if cell in fruits.strawberries and cell not in self.strawberriesScanned:
                self.strawberriesScanned.append(cell)
            if cell in traps.mushrooms and cell not in self.mushroomsScanned:
                self.mushroomsScanned.append(cell)
            if cell in traps.ices and cell not in self.icesScanned:
                self.icesScanned.append(cell)
            if cell in dispensers.dispensers and cell not in self.dispensersScanned:
                self.dispensersScanned.append(cell)

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

    def circleBres(self, xc: int, yc: int):
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
    
    def drawFruits(self, screen):

        for apple_pos in self.applesScanned:
            screen.blit(apple, (apple_pos.x * SQUARE_SIZE, apple_pos.y * SQUARE_SIZE))

        for banana_pos in self.bananasScanned:
            screen.blit(banana, (banana_pos.x * SQUARE_SIZE, banana_pos.y * SQUARE_SIZE))

        for strawberry_pos in self.strawberriesScanned:
            screen.blit(strawberry, (strawberry_pos.x * SQUARE_SIZE, strawberry_pos.y * SQUARE_SIZE))

    def drawTraps(self, screen):

        for mushroom_pos in self.mushroomsScanned:
            screen.blit(mushroom, (mushroom_pos.x * SQUARE_SIZE, mushroom_pos.y * SQUARE_SIZE))

        for ice_pos in self.icesScanned:
            screen.blit(ice, (ice_pos.x * SQUARE_SIZE, ice_pos.y * SQUARE_SIZE))

    def drawDispensers(self, screen, dispensers):
        for dispenser in self.dispensersScanned:
            p.draw.rect(screen, dispensers.dispenser_color, p.Rect(dispenser.x * SQUARE_SIZE, dispenser.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    def updateDispenserState (self, screen, dispensers):
        for index in range(len(self.dispensersScanned)):
                if dispensers.STATE == 1:
                    dispensers.dispenser_color = p.Color("chartreuse3")
                if dispensers.STATE == 2:
                    dispensers.dispenser_color = p.Color("hotpink1")
                    screen.blit(cooldown, (self.dispensersScanned[index].x * SQUARE_SIZE, self.dispensersScanned[index].y * SQUARE_SIZE))
