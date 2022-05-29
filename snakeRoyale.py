import pygame as p
from pygame import Vector2
import sys
from board import *
from reactive_snake import *
from dispenser_snake import *
from trap_snake import *
from deliberative_snake import *
from dispensers import *
from fruits import *
from traps import *

MAX_FPS = 20

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

    ## Generate all items
    board = Board()
    fruits = Fruits()
    fruits.definePositions(board)
    traps = Traps()
    traps.definePositions(board)
    dispensers = Dispensers()

    ## Create Snake
    # deliberative_snake : olivedrab,
    # reactive_snake : orange2,
    # trap_snake : lightslategrey,
    # dispenser_snake : indianred
    reactive_snake = Reactive_Snake()
    
    screen.fill("lemonchiffon1")
    reactive_snake.drawSnake(screen)
    fruits.drawFruits(screen)
    traps.drawTraps(screen)
    dispensers.drawDispensers(screen)
    board.drawLines(screen)

    SCREEN_UPDATE = p.USEREVENT
    p.time.set_timer(SCREEN_UPDATE, 150)

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                print("\n YOU GAVE UP !\n")
                print("----------------------------------------------------------")
                print("----------------------- SCORE BOARD ----------------------")
                print("----------------------------------------------------------")
                print("Global Score: ", reactive_snake.globalScore)
                print("Snake Size: ", len(reactive_snake.body))
                print("Apples: ", reactive_snake.apples, " x2 points")
                print("Bananas: ", reactive_snake.bananas, " x3 points")
                print("Strawberries: ", reactive_snake.strawberries, " x5 points")
                print("Mushrooms: ", reactive_snake.mushrooms, "x(-1) points")
                print("Ice: ", reactive_snake.ices)
                print("Dispenser: ", reactive_snake.dispenser)
                print("----------------------------------------------------------")
                p.quit()
                sys.exit()
            if e.type == SCREEN_UPDATE:
                reactive_snake.moveSnake()
            if e.type == p.KEYDOWN:
                if e.key == p.K_UP and reactive_snake.direction != Vector2(0,1):
                    reactive_snake.direction = Vector2(0,-1)
                if e.key == p.K_DOWN and reactive_snake.direction != Vector2(0,-1):
                    reactive_snake.direction = Vector2(0,1)
                if e.key == p.K_LEFT and reactive_snake.direction != Vector2(1,0):
                    reactive_snake.direction = Vector2(-1,0)
                if e.key == p.K_RIGHT and reactive_snake.direction != Vector2(-1,0):
                    reactive_snake.direction = Vector2(1,0)
        if reactive_snake.body[0] in fruits.apples:
            # snake caught an apple
            # print("APPLE!!!")
            # delete APPLE from the board and fruits class
            fruits.apples.remove(reactive_snake.body[0])
            board.busy_cells.remove(reactive_snake.body[0])
            # increase snake size
            reactive_snake.increaseSize()
            # add points
            reactive_snake.apples += 1
            reactive_snake.globalScore += 2
        
        if reactive_snake.body[0] in fruits.bananas:
            # snake caught a banana
            # print("BANANA!!!")
            # delete APPLE from the board and fruits class
            fruits.bananas.remove(reactive_snake.body[0])
            board.busy_cells.remove(reactive_snake.body[0])
            # increase snake size
            reactive_snake.increaseSize()
            # add points
            reactive_snake.bananas += 1
            reactive_snake.globalScore += 3
            
        if reactive_snake.body[0] in fruits.strawberries:
            # snake caught a strawberry
            # print("STRAWBERRY!!!")
            # delete APPLE from the board and fruits class
            fruits.strawberries.remove(reactive_snake.body[0])
            board.busy_cells.remove(reactive_snake.body[0])
            # increase snake size
            reactive_snake.increaseSize()
            # add points
            reactive_snake.strawberries += 1
            reactive_snake.globalScore += 5
            
        if reactive_snake.body[0] in traps.mushrooms:
            # snake caught a mushroom
            # print("MUSHROOM >__<")
            # delete APPLE from the board and fruits class
            traps.mushrooms.remove(reactive_snake.body[0])
            board.busy_cells.remove(reactive_snake.body[0])
            # add points
            reactive_snake.mushrooms += 1
            reactive_snake.globalScore -= 1
            # TODO: Implement the reduction of points from other snakes (-4)
            
        if reactive_snake.body[0] in traps.ices:
            # snake caught an ice
            # print("ICE *__*")
            # delete APPLE from the board and fruits class
            traps.ices.remove(reactive_snake.body[0])
            board.busy_cells.remove(reactive_snake.body[0])
            # add points
            reactive_snake.ices += 1
            
        if reactive_snake.body[0] in dispensers.dispensers:
            # print("DISPENSER :P")
            if reactive_snake.body[0] == Vector2(4,4) and dispensers.TL_DISPENSER_STATE == 0:
                dispensers.TL_DISPENSER_STATE = 1
                reactive_snake.dispenser += 1
                # TODO: Assuming there is only one snake on the board
                reactive_snake.globalScore += 8

            if reactive_snake.body[0] == Vector2(4,15) and dispensers.TR_DISPENSER_STATE == 0:
                dispensers.TR_DISPENSER_STATE = 1
                reactive_snake.dispenser += 1
                # TODO: Assuming there is only one snake on the board
                reactive_snake.globalScore += 8

            if reactive_snake.body[0] == Vector2(15,4) and dispensers.BL_DISPENSER_STATE == 0:
                dispensers.BL_DISPENSER_STATE = 1
                reactive_snake.dispenser += 1
                # TODO: Assuming there is only one snake on the board
                reactive_snake.globalScore += 8

            if reactive_snake.body[0] == Vector2(15,15) and dispensers.BR_DISPENSER_STATE == 0:
                dispensers.BR_DISPENSER_STATE = 1
                reactive_snake.dispenser += 1
                # TODO: Assuming there is only one snake on the board
                reactive_snake.globalScore += 8
        
        if reactive_snake.body[0] in reactive_snake.body[1:] or reactive_snake.body[0].x < 0 or reactive_snake.body[0].x > board.boardSize or reactive_snake.body[0].y < 0 or reactive_snake.body[0].y > board.boardSize:
            # snake hit itself or went off the edges
            print("\n YOU LOST !\n")
            print("----------------------------------------------------------")
            print("----------------------- SCORE BOARD ----------------------")
            print("----------------------------------------------------------")
            print("Global Score: ", reactive_snake.globalScore)
            print("Snake Size: ", len(reactive_snake.body))
            print("Apples: ", reactive_snake.apples, " x2 points")
            print("Bananas: ", reactive_snake.bananas, " x3 points")
            print("Strawberries: ", reactive_snake.strawberries, " x5 points")
            print("Mushrooms: ", reactive_snake.mushrooms, "x(-1) points")
            print("Ice: ", reactive_snake.ices)
            print("Dispenser: ", reactive_snake.dispenser)
            print("----------------------------------------------------------")
            running = False

        screen.fill("lemonchiffon1")
        fruits.drawFruits(screen)
        traps.drawTraps(screen)
        dispensers.drawDispensers(screen)
        dispensers.updateDispenserState(screen)
        #TODO: Implement the cooldown factor on the dispensers
        reactive_snake.drawSnake(screen)
        board.drawLines(screen)
        p.display.update()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main()
