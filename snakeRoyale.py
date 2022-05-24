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
    screen.fill(p.Color("black"))
    running = True
    food_spawned = False

    board = Board()
    snake = Snake()
    snake.color = "olivedrab"

    snake2 = Snake()
    snake2.color = "orange2"

    snake3 = Snake()
    snake3.color = "lightslategrey"

    snake4 = Snake()
    snake4.color = "indianred"
    
    board.drawBoard(screen)   # draw squares of the board

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        event = p.event.wait()
        if event.type == p.KEYDOWN:
            if event.key == p.K_s:
                board.busy_cells=[]
                food_spawned = False
        if not food_spawned:
            drawGame(board, screen)
            snake.drawSnake(screen, board)
            snake2.drawSnake(screen, board)
            snake3.drawSnake(screen, board)
            snake4.drawSnake(screen, board)
            board.drawLines(screen)
            food_spawned = True
        
        clock.tick(MAX_FPS)
        p.display.flip()
        # board.updateDispenserState(screen)    # verifies if the the dispenser is ACTIVE or ON COOLDOWN

'''
Responsible for initializing the board
'''
def drawGame(board, screen):
    board.drawBoard(screen)   # draw squares of the board
    board.spawnFood(screen)   # spawn food on the board
    board.spawnTraps(screen)
    

# def spawnTraps(screen):

if __name__ == "__main__":
    main()
