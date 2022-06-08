import pygame as p
from pygame import Vector2
import sys
from board import *
from deliberative_snake import *
from dispenser_snake import *
from trap_snake import *
from deliberative_snake import *
from dispensers import *
from fruits import *
from traps import *

MAX_FPS = 10

'''
Main function. Handles initializing application and updating graphics
'''
def main():
    p.init()

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    screen_color = "lemonchiffon1"
    running = True

    ## Generate all items
    board = Board()
    fruits = Fruits()
    fruits.definePositions(board)
    traps = Traps()
    traps.definePositions(board)
    dispensers = Dispensers()

    ## Create Snake
    # deliberative_snake : olivedrab,
    # deliberative_snake : orange2,
    # trap_snake : lightslategrey,
    # dispenser_snake : indianred
    deliberative_snake = Deliberative_Snake()
    
    screen.fill(screen_color)
    deliberative_snake.drawSnake(screen)
    deliberative_snake.scanArea(screen)
    fruits.drawFruits(screen)
    traps.drawTraps(screen)
    dispensers.drawDispensers(screen)
    board.drawLines(screen)

    SCREEN_UPDATE = p.USEREVENT
    p.time.set_timer(SCREEN_UPDATE, 300)

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                print("\n YOU GAVE UP !\n")
                print("----------------------------------------------------------")
                print("----------------------- SCORE BOARD ----------------------")
                print("----------------------------------------------------------")
                print("Global Score: ", deliberative_snake.globalScore)
                print("Snake Size: ", deliberative_snake.size)
                print("Apples: ", deliberative_snake.apples, " x2 points")
                print("Bananas: ", deliberative_snake.bananas, " x3 points")
                print("Strawberries: ", deliberative_snake.strawberries, " x5 points")
                print("Mushrooms: ", deliberative_snake.mushrooms, "x(-1) points")
                print("Ice: ", deliberative_snake.ices)
                print("Dispenser: ", deliberative_snake.dispenser)
                print("----------------------------------------------------------")
                p.quit()
                sys.exit()
            if e.type == SCREEN_UPDATE:
                pass
                deliberative_snake.moveSnake()
            if e.type == p.KEYDOWN:
                if e.key == p.K_UP and deliberative_snake.direction != Vector2(0,1):
                    deliberative_snake.direction = Vector2(0,-1)
                if e.key == p.K_DOWN and deliberative_snake.direction != Vector2(0,-1):
                    deliberative_snake.direction = Vector2(0,1)
                if e.key == p.K_LEFT and deliberative_snake.direction != Vector2(1,0):
                    deliberative_snake.direction = Vector2(-1,0)
                if e.key == p.K_RIGHT and deliberative_snake.direction != Vector2(-1,0):
                    deliberative_snake.direction = Vector2(1,0)
        if deliberative_snake.body[0] in fruits.apples:
            # snake caught an apple
            # print("APPLE!!!")
            # delete APPLE from the board and fruits class
            fruits.apples.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # increase snake size
            deliberative_snake.increaseSize()
            # add points
            deliberative_snake.apples += 1
            deliberative_snake.globalScore += 2
        
        if deliberative_snake.body[0] in fruits.bananas:
            # snake caught a banana
            # print("BANANA!!!")
            # delete APPLE from the board and fruits class
            fruits.bananas.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # increase snake size
            deliberative_snake.increaseSize()
            # add points
            deliberative_snake.bananas += 1
            deliberative_snake.globalScore += 3
            
        if deliberative_snake.body[0] in fruits.strawberries:
            # snake caught a strawberry
            # print("STRAWBERRY!!!")
            # delete APPLE from the board and fruits class
            fruits.strawberries.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # increase snake size
            deliberative_snake.increaseSize()
            # add points
            deliberative_snake.strawberries += 1
            deliberative_snake.globalScore += 5
            
        if deliberative_snake.body[0] in traps.mushrooms:
            # snake caught a mushroom
            # print("MUSHROOM >__<")
            # delete APPLE from the board and fruits class
            traps.mushrooms.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # add points
            deliberative_snake.mushrooms += 1
            deliberative_snake.globalScore -= 1
            # TODO: Implement the reduction of points from other snakes (-4)
            
        if deliberative_snake.body[0] in traps.ices:
            # snake caught an ice
            # print("ICE *__*")
            # delete APPLE from the board and fruits class
            traps.ices.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # add points
            deliberative_snake.ices += 1
            
        if deliberative_snake.body[0] in dispensers.dispensers:
            # print("DISPENSER :P")
            for dispenserPos in dispensers.dispensers:
                if deliberative_snake.body[0] == dispenserPos and dispensers.STATE == 0:
                    dispensers.STATE = 1
                    dispenserTimer = p.time.get_ticks()
        
        else:
            # Check dispenser timer and put in cooldown
            if dispensers.STATE == 1 and p.time.get_ticks() - dispenserTimer >= 5000:
                fruits.definePositionsDispenser(board)
                dispensers.STATE = 2
                deliberative_snake.dispenser += 1
                # TODO: Assuming there is only one snake on the board // Add if to check which snakes have the propertie REWARD at true, divide the points and distribute to each one
                deliberative_snake.globalScore += 8
                dispenserCooldown = p.time.get_ticks()
            
            if dispensers.STATE == 2 and p.time.get_ticks() - dispenserCooldown >= 5000:
                dispensers.STATE = 0

        
        if deliberative_snake.body[0] in deliberative_snake.body[1:] or deliberative_snake.body[0].x < 0 or deliberative_snake.body[0].x >= board.boardSize or deliberative_snake.body[0].y < 0 or deliberative_snake.body[0].y >= board.boardSize:
            # snake hit itself or went off the edges
            print("\n YOU LOST !\n")
            print("----------------------------------------------------------")
            print("----------------------- SCORE BOARD ----------------------")
            print("----------------------------------------------------------")
            print("Global Score: ", deliberative_snake.globalScore)
            print("Snake Size: ", deliberative_snake.size)
            print("Apples: ", deliberative_snake.apples, " x2 points")
            print("Bananas: ", deliberative_snake.bananas, " x3 points")
            print("Strawberries: ", deliberative_snake.strawberries, " x5 points")
            print("Mushrooms: ", deliberative_snake.mushrooms, "x(-1) points")
            print("Ice: ", deliberative_snake.ices)
            print("Dispenser: ", deliberative_snake.dispenser)
            print("----------------------------------------------------------")
            running = False

        elif deliberative_snake.size == 40 or deliberative_snake.globalScore >= 100:
            # snake achieved the maximum size or points and WON!
            print("\n YOU WIN !\n")
            print("----------------------------------------------------------")
            print("----------------------- SCORE BOARD ----------------------")
            print("----------------------------------------------------------")
            print("Global Score: ", deliberative_snake.globalScore)
            print("Snake Size: ", deliberative_snake.size)
            print("Apples: ", deliberative_snake.apples, " x2 points")
            print("Bananas: ", deliberative_snake.bananas, " x3 points")
            print("Strawberries: ", deliberative_snake.strawberries, " x5 points")
            print("Mushrooms: ", deliberative_snake.mushrooms, "x(-1) points")
            print("Ice: ", deliberative_snake.ices)
            print("Dispenser: ", deliberative_snake.dispenser)
            print("----------------------------------------------------------")
            running = False

        screen.fill("lemonchiffon1")
        deliberative_snake.scanArea(screen)
        fruits.drawFruits(screen)
        traps.drawTraps(screen)
        dispensers.drawDispensers(screen)
        dispensers.updateDispenserState(screen)
        #TODO: Implement the cooldown factor on the dispensers
        deliberative_snake.drawSnake(screen)
        board.drawLines(screen)
        p.display.update()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main()
