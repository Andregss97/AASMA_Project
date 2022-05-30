import pygame as p
from pygame import Vector2
import sys
from Board import *
from reactive_snake import *
from dispenser_snake import *
from trap_snake import *
from deliberative_snake import *
from Dispensers import *

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
    #food_spawned = False
    agents = []

    ## Generate all items
    board = Board()
    dispensers = Dispensers()

    ## Create Snake
    # deliberative_snake : olivedrab,
    # reactive_snake : orange2,
    # trap_snake : lightslategrey,
    # dispenser_snake : indianred
    reactive_snake = Reactive_Snake()
    agents.append(reactive_snake)


    dispensers.drawDispensers(screen)
    board.draw(screen, agents)

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

        board.update(agents)
            
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

        board.draw(screen, agents)
        dispensers.updateDispenserState(screen)
        p.display.update()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main()
