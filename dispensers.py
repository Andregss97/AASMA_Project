import pygame as p
from pygame import Vector2
from board import *



cooldown = p.image.load('snake_imgs/cooldown.svg')

class Dispensers:

    def __init__(self):
        self.dispensers = [Vector2(4,4), Vector2(4,15), Vector2(15,4), Vector2(15,15)]
        self.dispenser_color = p.Color("hotpink1")
        # Dispenser States : 1 - ACTIVE , 0 - ON COOLDOWN
        self.TL_DISPENSER_STATE = 0  # top-left dispenser state
        self.TR_DISPENSER_STATE = 0  # top-right dispenser state
        self.BL_DISPENSER_STATE = 0  # bottom-left dispenser state
        self.BR_DISPENSER_STATE = 0  # bottom-right dispenser state

    def drawDispensers(self, screen):
        for dispenser in self.dispensers:
            p.draw.rect(screen, self.dispenser_color, p.Rect(dispenser.x * SQUARE_SIZE, dispenser.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    def updateDispenserState (self, screen):
        for index in range(len(self.dispensers)):
            if index == 0:
                if self.TL_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index].x * SQUARE_SIZE, self.dispensers[index].y * SQUARE_SIZE))
            if index == 1:
                if self.TR_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index].x * SQUARE_SIZE, self.dispensers[index].y * SQUARE_SIZE))
            if index == 2:
                if self.BL_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index].x * SQUARE_SIZE, self.dispensers[index].y * SQUARE_SIZE))
            if index == 3:
                if self.BR_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index].x * SQUARE_SIZE, self.dispensers[index].y * SQUARE_SIZE))
            