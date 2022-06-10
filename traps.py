import pygame as p
from pygame import Vector2
from random import randrange
from board import *

mushroom = p.image.load('snake_imgs/mushroom.svg')
ice = p.image.load('snake_imgs/ice.svg')

NMBR_START_MUSHROOMS = 3
NMBR_START_ICES = 2

class Traps:

    def __init__(self):
        self.mushrooms = []
        self.ices = []
        self.mushroomNMB = NMBR_START_MUSHROOMS
        self.iceNMB = NMBR_START_ICES

    def definePositions(self, board: Board):
        self.mushrooms = board.generateBoardPositions(NMBR_START_MUSHROOMS)
        self.ices = board.generateBoardPositions(NMBR_START_ICES)

    def drawTraps(self, screen):

        for mushroom_pos in self.mushrooms:
            screen.blit(mushroom.convert_alpha(), (mushroom_pos.x * SQUARE_SIZE, mushroom_pos.y * SQUARE_SIZE))

        for ice_pos in self.ices:
            screen.blit(ice.convert_alpha(), (ice_pos.x * SQUARE_SIZE, ice_pos.y * SQUARE_SIZE))
