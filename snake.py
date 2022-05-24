import pygame as p
from random import randrange
from board import *

class Snake:
    snakeSize = 2 # initial snake starts with head and tail
    
    globalScore = 0

    # F R U I T S
    apples = 0
    bananas = 0
    strawberries = 0

    # T R A P S
    mushrooms = 0
    ice = 0

    # D I S P E N S E R
    dispenser = 0
    shared_dispenser = 0

    def drawSnake(self, screen, board: Board, color: str):
        rand_X = randrange(board.boardSize)
        rand_Y = randrange(board.boardSize)
        board.busy_cells
