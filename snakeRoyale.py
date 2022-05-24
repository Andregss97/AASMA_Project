import pygame as p
from random import randrange
from board import *
from snake import *

'''
Main function. Handles initializing application and updating graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    running = True
    food_spawned = False

    board = Board()
    
    board.drawBoard(screen)   # draw squares of the board

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        event = p.event.wait()
        if event.type == p.KEYDOWN:
            if event.key == p.K_s:
                food_spawned = False
        if not food_spawned:
            drawGame(board, screen)
            food_spawned = True
        clock.tick(MAX_FPS)
        p.display.flip()
        board.updateDispenserState(screen)    # verifies if the the dispenser is ACTIVE or ON COOLDOWN

'''
Responsible for initializing the board
'''
def drawGame(board, screen):
    board.drawBoard(screen)   # draw squares of the board
    board.spawnFood(screen)    # spawn food on the board

# def spawnTraps(screen):

if __name__ == "__main__":
    main()
