import pygame as p
from random import randrange
from board import *

directions = [(1,0),(-1,0),(0,1),(0,-1)]

class Snake:
    snakeSize = 2 # initial snake starts with head and tail
    color = ""
    
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

    def drawSnake(self, screen, board: Board):
        snake = False
        while not snake:
            rand_X = randrange(board.boardSize-1)
            rand_Y = randrange(board.boardSize-1)
            direction_i = randrange(3)
            direction = directions[direction_i]
            head = (rand_X, rand_Y)
            tail = (rand_X+direction[0], rand_Y+direction[1])
            # DIRECTION depends on the increment:
                # MOVE RIGHT vector = ( 1, 0)
                # MOVE LEFT vector  = (-1, 0)
                # MOVE UP vector    = ( 0,-1)
                # MOVE DOWN vector  = ( 0, 1)
            if head in board.busy_cells or tail in board.busy_cells or rand_X == 0 or rand_Y == 0:
                continue

            # create snake
            p.draw.rect(screen, self.color, p.Rect(head[0] * SQUARE_SIZE, head[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            p.draw.rect(screen, self.color, p.Rect(tail[0] * SQUARE_SIZE, tail[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            board.busy_cells.append(head)
            board.busy_cells.append(tail)
            snake = True

