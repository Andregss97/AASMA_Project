import pygame as p
from pygame import Vector2
from random import randrange
from Dispenser import *
from Apple import *
from Banana import *
from Strawberry import *
from Mushroom import *
from Ice import *

WIDTH = HEIGHT = 600 # 900
DIMENSION = 20 # 30
SQUARE_SIZE = HEIGHT // DIMENSION
NMBR_START_APPLES = 20
NMBR_START_BANANAS = 10
NMBR_START_STRAWBERRIES = 3
NMBR_START_MUSHROOMS = 4
NMBR_START_ICES = 2

class Board:

    def __init__(self):
        self.boardSize = DIMENSION
        self.tileSize = DIMENSION*SQUARE_SIZE
        self.busy_cells = {} # Initialized with DISPENSERS' positions
        self.busy_cells[tuple(Vector2(4,4))] = Dispenser(Vector2(4,4))
        self.busy_cells[tuple(Vector2(4,15))] = Dispenser(Vector2(4,15))
        self.busy_cells[tuple(Vector2(15,4))] = Dispenser(Vector2(15,4))
        self.busy_cells[tuple(Vector2(15,15))] = Dispenser(Vector2(15,15))
        apples = self.generateBoardPositions(NMBR_START_APPLES)
        for pos in apples:
            self.busy_cells[tuple(pos)] = Apple(pos)
        bananas = self.generateBoardPositions(NMBR_START_BANANAS)
        for pos in bananas:
            self.busy_cells[tuple(pos)] = Banana(pos)
        strawberries = self.generateBoardPositions(NMBR_START_STRAWBERRIES)
        for pos in strawberries:
            self.busy_cells[tuple(pos)] = Strawberry(pos)
        mushrooms = self.generateBoardPositions(NMBR_START_MUSHROOMS)
        for pos in mushrooms:
            self.busy_cells[tuple(pos)] = Mushroom(pos)
        ices = self.generateBoardPositions(NMBR_START_ICES)
        for pos in ices:
            self.busy_cells[tuple(pos)] = Ice(pos)

    def update(self, snakes):
        for snake in snakes:
            head = tuple(snake.body[0])
            if head in self.busy_cells:
                self.busy_cells[head].eat(snake, [s for s in snakes if s.body[0] != snake.body[0]])
                del self.busy_cells[head]

    def draw(self, screen, snakes):
        screen.fill("lemonchiffon1")
        for item in self.busy_cells.values():
            item.draw(screen)
        #dispensers.drawDispensers(screen)
        #dispensers.updateDispenserState(screen)
        #TODO: Implement the cooldown factor on the dispensers
        for s in snakes:
            s.drawSnake(screen)
        self.drawLines(screen)

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
            if tuple(new_pos) not in self.busy_cells:
                positions.append(new_pos)
                #self.busy_cells.append(new_pos)
                i += 1
        return positions

    def addItem(item):
        self.busy_cells[tuple(item.pos)] = item

