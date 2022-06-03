import pygame as p
from pygame import Vector2
from random import randrange

WIDTH = HEIGHT = 900 # 600
DIMENSION = 30 # 20
SQUARE_SIZE = HEIGHT // DIMENSION

class Board:

    def __init__(self):
        self.boardSize = DIMENSION
        self.tileSize = DIMENSION*SQUARE_SIZE
        self.busy_cells = [Vector2(6,6), Vector2(6,23), Vector2(23,6), Vector2(23,23)] # Initialized with DISPENSERS' positions
    
    def drawLines (self, screen):
        lines_color = p.Color("black")
        for l in range(self.boardSize):
            p.draw.lines(screen, lines_color, True, [(0, l * SQUARE_SIZE), (self.tileSize, l * SQUARE_SIZE)])
            p.draw.lines(screen, lines_color, True, [(l * SQUARE_SIZE, 0), (l * SQUARE_SIZE, self.tileSize)])

    def generateBoardPositions(self, numbr: int):
        i = 1
        positions = []
        while i <= numbr:
            rand_X = randrange(self.boardSize)
            rand_Y = randrange(self.boardSize)
            new_pos = Vector2(rand_X, rand_Y)
            if new_pos not in self.busy_cells:
                positions.append(new_pos)
                self.busy_cells.append(new_pos)
                i += 1
        return positions

