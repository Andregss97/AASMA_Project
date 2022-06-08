import pygame as p
from pygame import Vector2
from board import *

cooldown = p.image.load('snake_imgs/cooldown.svg')

class Dispensers:

    def __init__(self):
        self.dispensers = [Vector2(6,6), Vector2(6,23), Vector2(23,6), Vector2(23,23)]
        self.dispenser_color = p.Color("hotpink1")
        # Dispenser States : 0 - ACTIVE , 1 - WAITING , 2 - ON COOLDOWN
        self.STATE = 0  # dispensers state

    def drawDispensers(self, screen):
        for dispenser in self.dispensers:
            p.draw.rect(screen, self.dispenser_color, p.Rect(dispenser.x * SQUARE_SIZE, dispenser.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    def updateDispenserState (self, screen):
        for index in range(len(self.dispensers)):
                if self.STATE == 1:
                    self.dispenser_color = p.Color("chartreuse3")
                if self.STATE == 2:
                    self.dispenser_color = p.Color("hotpink1")
                    screen.blit(cooldown, (self.dispensers[index].x * SQUARE_SIZE, self.dispensers[index].y * SQUARE_SIZE))