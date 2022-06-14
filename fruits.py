import pygame as p
from board import *

apple = p.image.load('snake_imgs/apple.svg')
banana = p.image.load('snake_imgs/banana.svg')
strawberry = p.image.load('snake_imgs/strawberry.svg')

NMBR_START_APPLES = 20
NMBR_START_BANANAS = 10
NMBR_START_STRAWBERRIES = 5

NMBR_DISPENSER_APPLES = 20
NMBR_DISPENSER_BANANAS = 10
NMBR_DISPENSER_STRAWBERRIES = 5

class Fruits:

    def __init__(self):
        self.apples = []
        self.bananas = []
        self.strawberries = []
        self.appleNMB = NMBR_START_APPLES
        self.bananaNMB = NMBR_START_BANANAS
        self.strawberryNMB = NMBR_START_STRAWBERRIES
        self.applePoints = 2
        self.bananaPoints = 3
        self.strawberryPoints = 5

    def definePositions(self, board: Board):
        self.apples = board.generateBoardPositions(NMBR_START_APPLES)
        self.bananas = board.generateBoardPositions(NMBR_START_BANANAS)
        self.strawberries = board.generateBoardPositions(NMBR_START_STRAWBERRIES)

    def definePositionsDispenser(self, board: Board):
        self.apples += board.generateBoardPositions(NMBR_DISPENSER_APPLES)
        self.bananas += board.generateBoardPositions(NMBR_DISPENSER_BANANAS)
        self.strawberries += board.generateBoardPositions(NMBR_DISPENSER_STRAWBERRIES)

    def drawFruits(self, screen):

        for apple_pos in self.apples:
            screen.blit(apple.convert_alpha(), (apple_pos.x * SQUARE_SIZE, apple_pos.y * SQUARE_SIZE))

        for banana_pos in self.bananas:
            screen.blit(banana.convert_alpha(), (banana_pos.x * SQUARE_SIZE, banana_pos.y * SQUARE_SIZE))

        for strawberry_pos in self.strawberries:
            screen.blit(strawberry.convert_alpha(), (strawberry_pos.x * SQUARE_SIZE, strawberry_pos.y * SQUARE_SIZE))
        