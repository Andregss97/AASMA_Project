import pygame as p
import sys
from board import *
from deliberative_snake import *
from dispenser_snake import *
from trap_snake import *
from reactive_snake import *
from dispensers import *
from fruits import *
from traps import *

MAX_FPS = 3

apple_icon = p.image.load('snake_imgs/apple_icon.svg')
banana_icon = p.image.load('snake_imgs/banana_icon.svg')
strawberry_icon = p.image.load('snake_imgs/strawberry_icon.svg')

mushroom_icon = p.image.load('snake_imgs/mushroom_icon.svg')
ice_icon = p.image.load('snake_imgs/ice_icon.svg')

dispenser_icon = p.image.load('snake_imgs/dispenser.svg')
dispenser_icon = p.transform.scale(dispenser_icon, (20, 20))

reactive_snake_icon = p.image.load('snake_imgs/reactive_snake.svg')
deliberative_snake_icon = p.image.load('snake_imgs/deliberative_snake.svg')
trap_snake_icon = p.image.load('snake_imgs/trap_snake.svg')
dispenser_snake_icon = p.image.load('snake_imgs/dispenser_snake.svg')

size_white = p.image.load('snake_imgs/size_w.svg')
size_black = p.image.load('snake_imgs/size_b.svg')
score_white = p.image.load('snake_imgs/score_w.svg')
score_black = p.image.load('snake_imgs/score_b.svg')

'''
Main function. Handles initializing application and updating graphics
'''
def main():
    p.init()

    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption('Snake Royale')
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    screen_color = "lemonchiffon1"
    deliberative_screen_color = "gray12"
    deliberative_snake_screen = False
    snakes = []
    running = 1
    stepCount = 0
    score = False

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
    deliberative_snake = Deliberative_Snake()
    reactive_snake = Reactive_Snake()
    dispenser_snake = Dispenser_Snake()
    trap_snake = Trap_Snake()
    snakes.append(deliberative_snake)
    snakes.append(reactive_snake)
    snakes.append(dispenser_snake)
    
    screen.fill(screen_color)

    deliberative_snake.drawSnake(screen)
    reactive_snake.drawSnake(screen)
    dispenser_snake.drawSnake(screen)

    deliberative_snake.scanArea(screen, fruits, traps, dispensers)

    fruits.drawFruits(screen)
    traps.drawTraps(screen)
    dispensers.drawDispensers(screen)
    board.drawLines(screen)


    SCREEN_UPDATE = p.USEREVENT
    p.time.set_timer(SCREEN_UPDATE, 300)

    while running:
        reactive_snake.action(fruits, dispensers, traps, snakes)
        reactive_snake.moveSnake()

        deliberative_snake.action(dispensers, snakes)
        deliberative_snake.moveSnake()

        dispenser_snake.action(fruits, dispensers, traps, snakes)
        dispenser_snake.moveSnake()

        for e in p.event.get():
            if e.type == p.QUIT:
                print("\n YOU GAVE UP !\n")
                print("----------------------------------------------------------")
                print("----------------------- SCORE BOARD ----------------------")
                print("----------------------------------------------------------")
                print("------------------- DELIBERATIVE SNAKE -------------------")
                print("Global Score: ", deliberative_snake.globalScore)
                print("Snake Size: ", deliberative_snake.size)
                print("Apples: ", deliberative_snake.apples, " x2 points")
                print("Bananas: ", deliberative_snake.bananas, " x3 points")
                print("Strawberries: ", deliberative_snake.strawberries, " x5 points")
                print("Mushrooms: ", deliberative_snake.mushrooms, "x(-1) points")
                print("Ice: ", deliberative_snake.ices)
                print("Dispenser: ", deliberative_snake.dispenser)
                print("----------------------------------------------------------")
                print("--------------------- REACTIVE SNAKE ---------------------")
                print("Global Score: ", reactive_snake.globalScore)
                print("Snake Size: ", reactive_snake.size)
                print("Apples: ", reactive_snake.apples, " x2 points")
                print("Bananas: ", reactive_snake.bananas, " x3 points")
                print("Strawberries: ", reactive_snake.strawberries, " x5 points")
                print("Mushrooms: ", reactive_snake.mushrooms, "x(-1) points")
                print("Ice: ", reactive_snake.ices)
                print("Dispenser: ", reactive_snake.dispenser)
                print("----------------------------------------------------------")
                print("--------------------- DISPENSER SNAKE --------------------")
                print("Global Score: ", dispenser_snake.globalScore)
                print("Snake Size: ", dispenser_snake.size)
                print("Apples: ", dispenser_snake.apples, " x2 points")
                print("Bananas: ", dispenser_snake.bananas, " x3 points")
                print("Strawberries: ", dispenser_snake.strawberries, " x5 points")
                print("Mushrooms: ", dispenser_snake.mushrooms, "x(-1) points")
                print("Ice: ", dispenser_snake.ices)
                print("Dispenser: ", dispenser_snake.dispenser)
                print("----------------------------------------------------------")
                p.quit()
                sys.exit()
                
            if e.type == p.KEYDOWN:
                if e.key == p.K_d:
                    if deliberative_snake_screen :
                        deliberative_snake_screen = False
                    else:
                        deliberative_snake_screen = True

        # DELIBERATIVE SNAKE
        if deliberative_snake.body[0] in fruits.apples:
            # snake caught an apple
            # print("APPLE!!!")
            # delete APPLE from the board and fruits class
            fruits.apples.remove(deliberative_snake.body[0])
            deliberative_snake.applesScanned.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # increase snake size
            deliberative_snake.increaseSize()
            # add points
            deliberative_snake.apples += 1
            deliberative_snake.globalScore += fruits.applePoints

        if deliberative_snake.body[0] in fruits.bananas:
            # snake caught a banana
            # print("BANANA!!!")
            # delete APPLE from the board and fruits class
            fruits.bananas.remove(deliberative_snake.body[0])
            deliberative_snake.bananasScanned.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # increase snake size
            deliberative_snake.increaseSize()
            # add points
            deliberative_snake.bananas += 1
            deliberative_snake.globalScore += fruits.bananaPoints

        if deliberative_snake.body[0] in fruits.strawberries:
            # snake caught a strawberry
            # print("STRAWBERRY!!!")
            # delete APPLE from the board and fruits class
            fruits.strawberries.remove(deliberative_snake.body[0])
            deliberative_snake.strawberriesScanned.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # increase snake size
            deliberative_snake.increaseSize()
            # add points
            deliberative_snake.strawberries += 1
            deliberative_snake.globalScore += fruits.strawberryPoints

        if deliberative_snake.body[0] in traps.mushrooms:
            # snake caught a mushroom
            # print("MUSHROOM >__<")
            # delete APPLE from the board and fruits class
            traps.mushrooms.remove(deliberative_snake.body[0])
            deliberative_snake.mushroomsScanned.remove(deliberative_snake.body[0])
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
            deliberative_snake.icesScanned.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # add points
            deliberative_snake.ices += 1

        if deliberative_snake.body[0] in dispensers.dispensers and not deliberative_snake.activeDispenser:
            # print("DISPENSER :P")
            for dispenserPos in dispensers.dispensers:
                if deliberative_snake.body[0] == dispenserPos and dispensers.STATE == 0:
                    deliberative_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    deliberative_snake.dispenser += 1
                    dispenserTimer = p.time.get_ticks()
                if deliberative_snake.body[0] == dispenserPos and dispensers.STATE == 1:
                    deliberative_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    deliberative_snake.dispenser += 1   
            if dispensers.STATE == 0 and deliberative_snake.activeDispenser:
                dispensers.STATE = 1  

        ############################################################################

        # REACTIVE SNAKE

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
            reactive_snake.globalScore += fruits.applePoints
        
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
            reactive_snake.globalScore += fruits.bananaPoints
            
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
            reactive_snake.globalScore += fruits.strawberryPoints
            
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

        if reactive_snake.body[0] in dispensers.dispensers and not reactive_snake.activeDispenser:
            # print("DISPENSER :P")
            for dispenserPos in dispensers.dispensers:
                if reactive_snake.body[0] == dispenserPos and dispensers.STATE == 0:
                    reactive_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    reactive_snake.dispenser += 1
                    dispenserTimer = p.time.get_ticks()
                if reactive_snake.body[0] == dispenserPos and dispensers.STATE == 1:
                    reactive_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    reactive_snake.dispenser += 1   
            if dispensers.STATE == 0 and reactive_snake.activeDispenser:
                dispensers.STATE = 1                 

        ############################################################################

        # DISPENSER SNAKE

        if dispenser_snake.body[0] in fruits.apples:
            # snake caught an apple
            # print("APPLE!!!")
            # delete APPLE from the board and fruits class
            fruits.apples.remove(dispenser_snake.body[0])
            board.busy_cells.remove(dispenser_snake.body[0])
            # increase snake size
            dispenser_snake.increaseSize()
            # add points
            dispenser_snake.apples += 1
            dispenser_snake.globalScore += fruits.applePoints
        
        if dispenser_snake.body[0] in fruits.bananas:
            # snake caught a banana
            # print("BANANA!!!")
            # delete APPLE from the board and fruits class
            fruits.bananas.remove(dispenser_snake.body[0])
            board.busy_cells.remove(dispenser_snake.body[0])
            # increase snake size
            dispenser_snake.increaseSize()
            # add points
            dispenser_snake.bananas += 1
            dispenser_snake.globalScore += fruits.bananaPoints
            
        if dispenser_snake.body[0] in fruits.strawberries:
            # snake caught a strawberry
            # print("STRAWBERRY!!!")
            # delete APPLE from the board and fruits class
            fruits.strawberries.remove(dispenser_snake.body[0])
            board.busy_cells.remove(dispenser_snake.body[0])
            # increase snake size
            dispenser_snake.increaseSize()
            # add points
            dispenser_snake.strawberries += 1
            dispenser_snake.globalScore += fruits.strawberryPoints
            
        if dispenser_snake.body[0] in traps.mushrooms:
            # snake caught a mushroom
            # print("MUSHROOM >__<")
            # delete APPLE from the board and fruits class
            traps.mushrooms.remove(dispenser_snake.body[0])
            board.busy_cells.remove(dispenser_snake.body[0])
            # add points
            dispenser_snake.mushrooms += 1
            dispenser_snake.globalScore -= 1
            # TODO: Implement the reduction of points from other snakes (-4)
            
        if dispenser_snake.body[0] in traps.ices:
            # snake caught an ice
            # print("ICE *__*")
            # delete APPLE from the board and fruits class
            traps.ices.remove(dispenser_snake.body[0])
            board.busy_cells.remove(dispenser_snake.body[0])
            # add points
            dispenser_snake.ices += 1
            
        if dispenser_snake.body[0] in dispensers.dispensers and not dispenser_snake.activeDispenser:
            # print("DISPENSER :P")
            for dispenserPos in dispensers.dispensers:
                if dispenser_snake.body[0] == dispenserPos and dispensers.STATE == 0:
                    dispenser_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    dispenser_snake.dispenser += 1
                    dispenserTimer = p.time.get_ticks()
                elif dispenser_snake.body[0] == dispenserPos and dispensers.STATE == 1:
                    dispenser_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    dispenser_snake.dispenser += 1
            if dispensers.STATE == 0 and dispenser_snake.activeDispenser:
                dispensers.STATE = 1    
                    
        ##############################################################################
        
        else:
            # Check dispenser timer and put in cooldown
            if dispensers.STATE == 1 and p.time.get_ticks() - dispenserTimer >= 5000:
                fruits.definePositionsDispenser(board)
                dispensers.STATE = 2

                # TODO: Assuming there is only one snake on the board // Add if to check which snakes have the propertie REWARD at true, divide the points and distribute to each one
                if dispensers.num_snakes <= 2:
                    if deliberative_snake.activeDispenser:
                        deliberative_snake.globalScore += 8//dispensers.num_snakes
                    if reactive_snake.activeDispenser:
                        reactive_snake.globalScore += 8//dispensers.num_snakes
                    if dispenser_snake.activeDispenser:
                        dispenser_snake.globalScore += 8//dispensers.num_snakes
                elif dispensers.num_snakes == 3:
                    if deliberative_snake.activeDispenser:
                        deliberative_snake.globalScore += 2
                    if reactive_snake.activeDispenser:
                        reactive_snake.globalScore += 2
                    if dispenser_snake.activeDispenser:
                        dispenser_snake.globalScore += 2
                elif dispensers.num_snakes == 4:
                    deliberative_snake.globalScore += 1
                    reactive_snake.globalScore += 1
                    dispenser_snake.globalScore += 1
       
                dispenserCooldown = p.time.get_ticks()
            
            if dispensers.STATE == 2 and p.time.get_ticks() - dispenserCooldown >= 5000:
                dispensers.STATE = 0
                deliberative_snake.activeDispenser = False
                reactive_snake.activeDispenser = False
                dispenser_snake.activeDispenser = False
                dispensers.num_snakes = 0

        # SCORE BOARD

        if deliberative_snake.body[0] in deliberative_snake.body[1:] or deliberative_snake.body[0].x < 0 or deliberative_snake.body[0].x >= board.boardSize or deliberative_snake.body[0].y < 0 or deliberative_snake.body[0].y >= board.boardSize:
            # snake hit itself or went off the edges
            print("\n DELIBERATIVE SNAKE LOST !\n")
            p.display.set_caption('Snake Royale - DELIBERATIVE SNAKE LOST !')
            score = True

        if reactive_snake.body[0] in reactive_snake.body[1:] or reactive_snake.body[0].x < 0 or reactive_snake.body[0].x >= board.boardSize or reactive_snake.body[0].y < 0 or reactive_snake.body[0].y >= board.boardSize:
            # snake hit itself or went off the edges
            print("\n REACTIVE SNAKE LOST !\n")
            p.display.set_caption('Snake Royale - REACTIVE SNAKE LOST !')
            score = True

        if dispenser_snake.body[0] in dispenser_snake.body[1:] or dispenser_snake.body[0].x < 0 or dispenser_snake.body[0].x >= board.boardSize or dispenser_snake.body[0].y < 0 or dispenser_snake.body[0].y >= board.boardSize:
            # snake hit itself or went off the edges
            print("\n DISPENSER SNAKE LOST !\n")
            p.display.set_caption('Snake Royale - DISPENSER SNAKE LOST !')
            score = True

        if deliberative_snake.size == 50 or deliberative_snake.globalScore >= 150:
            # snake achieved the maximum size or points and WON!
            print("\n DELIBERATIVE SNAKE WINS !\n")
            p.display.set_caption('Snake Royale - DELIBERATIVE SNAKE WINS !')
            score = True
        
        if reactive_snake.size == 50 or reactive_snake.globalScore >= 150:
            # snake achieved the maximum size or points and WON!
            print("\n REACTIVE SNAKE WINS !\n")
            p.display.set_caption('Snake Royale - REACTIVE SNAKE WINS !')
            score = True
        
        if dispenser_snake.size == 50 or dispenser_snake.globalScore == 150:
            # snake achieved the maximum size or points and WON!
            print("\n DISPENSER SNAKE WINS !\n")
            p.display.set_caption('Snake Royale - DISPENSER SNAKE WINS !')
            score = True

        if score:
            print("----------------------------------------------------------")
            print("----------------------- SCORE BOARD ----------------------")
            print("----------------------------------------------------------")
            print("------------------- DELIBERATIVE SNAKE -------------------")
            print("Global Score: ", deliberative_snake.globalScore)
            print("Snake Size: ", deliberative_snake.size)
            print("Apples: ", deliberative_snake.apples, " x2 points")
            print("Bananas: ", deliberative_snake.bananas, " x3 points")
            print("Strawberries: ", deliberative_snake.strawberries, " x5 points")
            print("Mushrooms: ", deliberative_snake.mushrooms, "x(-1) points")
            print("Ice: ", deliberative_snake.ices)
            print("Dispenser: ", deliberative_snake.dispenser)
            print("----------------------------------------------------------")
            print("--------------------- REACTIVE SNAKE ---------------------")
            print("Global Score: ", reactive_snake.globalScore)
            print("Snake Size: ", reactive_snake.size)
            print("Apples: ", reactive_snake.apples, " x2 points")
            print("Bananas: ", reactive_snake.bananas, " x3 points")
            print("Strawberries: ", reactive_snake.strawberries, " x5 points")
            print("Mushrooms: ", reactive_snake.mushrooms, "x(-1) points")
            print("Ice: ", reactive_snake.ices)
            print("Dispenser: ", reactive_snake.dispenser)
            print("----------------------------------------------------------")
            print("--------------------- DISPENSER SNAKE --------------------")
            print("Global Score: ", dispenser_snake.globalScore)
            print("Snake Size: ", dispenser_snake.size)
            print("Apples: ", dispenser_snake.apples, " x2 points")
            print("Bananas: ", dispenser_snake.bananas, " x3 points")
            print("Strawberries: ", dispenser_snake.strawberries, " x5 points")
            print("Mushrooms: ", dispenser_snake.mushrooms, "x(-1) points")
            print("Ice: ", dispenser_snake.ices)
            print("Dispenser: ", dispenser_snake.dispenser)
            print("----------------------------------------------------------")
            running = 0
            
        #######################################################################

        if deliberative_snake_screen:
            screen.fill(deliberative_screen_color)
            deliberative_snake.scanArea(screen, fruits, traps, dispensers)
            deliberative_snake.drawFruits(screen)
            deliberative_snake.drawTraps(screen)
            deliberative_snake.drawDispensers(screen, dispensers)
            deliberative_snake.updateDispenserState(screen, dispensers)

            deliberative_snake.drawSnake(screen)
            reactive_snake.drawSnake(screen)
            dispenser_snake.drawSnake(screen)
            drawScoreBoard(screen, deliberative_snake_screen, deliberative_snake, reactive_snake, trap_snake, dispenser_snake, stepCount)

            stepCount += 1

            if deliberative_snake.exploreTO != [] and deliberative_snake.exploreTO[0] not in deliberative_snake.visibleArea and deliberative_snake.exploreTO[0] not in deliberative_snake.body:
                p.draw.rect(screen, "red", p.Rect(deliberative_snake.exploreTO[0].x * SQUARE_SIZE, deliberative_snake.exploreTO[0].y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)
            board.drawLines(screen)
        else:
            screen.fill(screen_color)
            deliberative_snake.scanArea(screen, fruits, traps, dispensers)
            fruits.drawFruits(screen)
            traps.drawTraps(screen)
            dispensers.drawDispensers(screen)
            dispensers.updateDispenserState(screen)

            deliberative_snake.drawSnake(screen)
            reactive_snake.drawSnake(screen)
            dispenser_snake.drawSnake(screen)

            drawScoreBoard(screen, deliberative_snake_screen, deliberative_snake, reactive_snake, trap_snake, dispenser_snake, stepCount)

            stepCount += 1

            board.drawLines(screen)
        p.display.update()
        clock.tick(MAX_FPS)
    while 1:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            if e.type == p.KEYDOWN:
                if e.key == p.K_d:
                    if deliberative_snake_screen :
                        deliberative_snake_screen = False
                    else:
                        deliberative_snake_screen = True
        if deliberative_snake_screen:
            screen.fill(deliberative_screen_color)
            deliberative_snake.scanArea(screen, fruits, traps, dispensers)
            deliberative_snake.drawFruits(screen)
            deliberative_snake.drawTraps(screen)
            deliberative_snake.drawDispensers(screen, dispensers)
            deliberative_snake.updateDispenserState(screen, dispensers)

            deliberative_snake.drawSnake(screen)
            reactive_snake.drawSnake(screen)
            dispenser_snake.drawSnake(screen)
            drawScoreBoard(screen, deliberative_snake_screen, deliberative_snake, reactive_snake, trap_snake, dispenser_snake, stepCount)

            if deliberative_snake.exploreTO != [] and deliberative_snake.exploreTO[0] not in deliberative_snake.visibleArea and deliberative_snake.exploreTO[0] not in deliberative_snake.body:
                p.draw.rect(screen, "red", p.Rect(deliberative_snake.exploreTO[0].x * SQUARE_SIZE, deliberative_snake.exploreTO[0].y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)
            board.drawLines(screen)
        else:
            screen.fill(screen_color)
            deliberative_snake.scanArea(screen, fruits, traps, dispensers)
            fruits.drawFruits(screen)
            traps.drawTraps(screen)
            dispensers.drawDispensers(screen)
            dispensers.updateDispenserState(screen)

            deliberative_snake.drawSnake(screen)
            reactive_snake.drawSnake(screen)
            dispenser_snake.drawSnake(screen)
            board.drawLines(screen)

            drawScoreBoard(screen, deliberative_snake_screen, deliberative_snake, reactive_snake, trap_snake, dispenser_snake, stepCount)
        p.display.update()

def drawScoreBoard(screen, flag: bool, deliberative_snake: Deliberative_Snake, reactive_snake: Reactive_Snake, trap_snake: Trap_Snake, dispenser_snake: Dispenser_Snake, stepCount: int):
    ## Score Board
    text = p.font.SysFont("monospace", 16)    
    subtitle = p.font.SysFont("monospace", 20, True)
    title = p.font.SysFont("monospace", 32, True)
    basic_color = (0,0,0)
    if flag:
        basic_color = (255,255,255)
        deliberative_snake_visionTxt = subtitle.render("Deliberative Snake Vision  ON", 1, basic_color)
        screen.blit(deliberative_snake_visionTxt, (32 * SQUARE_SIZE, 0.5 * SQUARE_SIZE))
        stepsTxt = text.render("Steps {0}".format(stepCount), 1, basic_color)
        screen.blit(stepsTxt, (41 * SQUARE_SIZE, 2 * SQUARE_SIZE))
        
        ## DELIBERATIVE SNAKE
        screen.blit(score_white.convert_alpha(), (32.4 * SQUARE_SIZE, 8.8 * SQUARE_SIZE))
        deliberative_global_score = subtitle.render("Score:{0}".format(deliberative_snake.globalScore), 1, 'olivedrab')
        screen.blit(deliberative_global_score, (33.5 * SQUARE_SIZE, 9.1 * SQUARE_SIZE))
        screen.blit(size_white.convert_alpha(), (37.4 * SQUARE_SIZE, 8.8 * SQUARE_SIZE))
        deliberative_size = subtitle.render("Size:{0}".format(deliberative_snake.size), 1, 'olivedrab')
        screen.blit(deliberative_size, (38.5 * SQUARE_SIZE, 9.1 * SQUARE_SIZE))

        ## REACTIVE SNAKE
        screen.blit(score_white.convert_alpha(), (32.4 * SQUARE_SIZE, 13.8 * SQUARE_SIZE))
        reactive_global_score = subtitle.render("Score:{0}".format(reactive_snake.globalScore), 1, 'orange2')
        screen.blit(reactive_global_score, (33.5 * SQUARE_SIZE, 14.1 * SQUARE_SIZE))
        screen.blit(size_white.convert_alpha(), (37.4 * SQUARE_SIZE, 13.8 * SQUARE_SIZE))
        reactive_size = subtitle.render("Size:{0}".format(reactive_snake.size), 1, 'orange2')
        screen.blit(reactive_size, (38.5 * SQUARE_SIZE, 14.1 * SQUARE_SIZE))

        ## DISPENSER SNAKE
        screen.blit(score_white.convert_alpha(), (32.4 * SQUARE_SIZE, 18.8 * SQUARE_SIZE))
        dispenser_global_score = subtitle.render("Score:{0}".format(dispenser_snake.globalScore), 1, 'indianred')
        screen.blit(dispenser_global_score, (33.5 * SQUARE_SIZE, 19.1 * SQUARE_SIZE))
        screen.blit(size_white.convert_alpha(), (37.4 * SQUARE_SIZE, 18.8 * SQUARE_SIZE))
        dispenser_size = subtitle.render("Size:{0}".format(dispenser_snake.size), 1, 'indianred')
        screen.blit(dispenser_size, (38.5 * SQUARE_SIZE, 19.1 * SQUARE_SIZE))

        ## TRAP SNAKE
        screen.blit(score_white.convert_alpha(), (32.4 * SQUARE_SIZE, 23.8 * SQUARE_SIZE))
        trap_global_score = subtitle.render("Score:{0}".format(trap_snake.globalScore), 1, 'lightslategrey')
        screen.blit(trap_global_score, (33.5 * SQUARE_SIZE, 24.1 * SQUARE_SIZE))
        screen.blit(size_white.convert_alpha(), (37.4 * SQUARE_SIZE, 23.8 * SQUARE_SIZE))
        trap_size = subtitle.render("Size:{0}".format(trap_snake.size), 1, 'lightslategrey')
        screen.blit(trap_size, (38.5 * SQUARE_SIZE, 24.1 * SQUARE_SIZE))

    else:
        pressD = text.render("[ Press D ] deliberative snake vision", 1, basic_color)
        screen.blit(pressD, (30.2 * SQUARE_SIZE, 0.5 * SQUARE_SIZE))
        stepsTxt = text.render("Steps {0}".format(stepCount), 1, basic_color)
        screen.blit(stepsTxt, (41 * SQUARE_SIZE, 2 * SQUARE_SIZE))
        
        ## DELIBERATIVE SNAKE
        screen.blit(score_black.convert_alpha(), (32.4 * SQUARE_SIZE, 8.8 * SQUARE_SIZE))
        deliberative_global_score = subtitle.render("Score:{0}".format(deliberative_snake.globalScore), 1, 'olivedrab')
        screen.blit(deliberative_global_score, (33.5 * SQUARE_SIZE, 9.1 * SQUARE_SIZE))
        screen.blit(size_black.convert_alpha(), (37.4 * SQUARE_SIZE, 8.8 * SQUARE_SIZE))
        deliberative_size = subtitle.render("Size:{0}".format(deliberative_snake.size), 1, 'olivedrab')
        screen.blit(deliberative_size, (38.5 * SQUARE_SIZE, 9.1 * SQUARE_SIZE))

        ## REACTIVE SNAKE
        screen.blit(score_black.convert_alpha(), (32.4 * SQUARE_SIZE, 13.8 * SQUARE_SIZE))
        reactive_global_score = subtitle.render("Score:{0}".format(reactive_snake.globalScore), 1, 'orange2')
        screen.blit(reactive_global_score, (33.5 * SQUARE_SIZE, 14.1 * SQUARE_SIZE))
        screen.blit(size_black.convert_alpha(), (37.4 * SQUARE_SIZE, 13.8 * SQUARE_SIZE))
        reactive_size = subtitle.render("Size:{0}".format(reactive_snake.size), 1, 'orange2')
        screen.blit(reactive_size, (38.5 * SQUARE_SIZE, 14.1 * SQUARE_SIZE))

        ## DISPENSER SNAKE
        screen.blit(score_black.convert_alpha(), (32.4 * SQUARE_SIZE, 18.8 * SQUARE_SIZE))
        dispenser_global_score = subtitle.render("Score:{0}".format(dispenser_snake.globalScore), 1, 'indianred')
        screen.blit(dispenser_global_score, (33.5 * SQUARE_SIZE, 19.1 * SQUARE_SIZE))
        screen.blit(size_black.convert_alpha(), (37.4 * SQUARE_SIZE, 18.8 * SQUARE_SIZE))
        dispenser_size = subtitle.render("Size:{0}".format(dispenser_snake.size), 1, 'indianred')
        screen.blit(dispenser_size, (38.5 * SQUARE_SIZE, 19.1 * SQUARE_SIZE))

        ## TRAP SNAKE
        screen.blit(score_black.convert_alpha(), (32.4 * SQUARE_SIZE, 23.8 * SQUARE_SIZE))
        trap_global_score = subtitle.render("Score:{0}".format(trap_snake.globalScore), 1, 'lightslategrey')
        screen.blit(trap_global_score, (33.5 * SQUARE_SIZE, 24.1 * SQUARE_SIZE))
        screen.blit(size_black.convert_alpha(), (37.4 * SQUARE_SIZE, 23.8 * SQUARE_SIZE))
        trap_size = subtitle.render("Size:{0}".format(trap_snake.size), 1, 'lightslategrey')
        screen.blit(trap_size, (38.5 * SQUARE_SIZE, 24.1 * SQUARE_SIZE))

    snakeRoyaleTxt = title.render("Snake Royale", 1, basic_color)
    screen.blit(snakeRoyaleTxt, (34 * SQUARE_SIZE, 3 * SQUARE_SIZE))
    scoreBoardTxt = subtitle.render("- Score Board -", 1, basic_color)
    screen.blit(scoreBoardTxt, (35 * SQUARE_SIZE, 4.5 * SQUARE_SIZE))

    ## DELIBERATIVE SNAKE
    screen.blit(deliberative_snake_icon.convert_alpha(), (31 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    deliberativeTxt = subtitle.render("Deliberative Snake", 1, 'olivedrab')
    screen.blit(deliberativeTxt, (32.5 * SQUARE_SIZE, 6.5 * SQUARE_SIZE))
    screen.blit(apple_icon.convert_alpha(), (30.1 * SQUARE_SIZE, 7.5 * SQUARE_SIZE))
    deliberative_apple_score = subtitle.render("{0}".format(deliberative_snake.apples), 1, 'olivedrab')
    screen.blit(deliberative_apple_score, (31.2 * SQUARE_SIZE, 7.8 * SQUARE_SIZE))
    screen.blit(banana_icon.convert_alpha(), (32.6 * SQUARE_SIZE, 7.5 * SQUARE_SIZE))
    deliberative_banana_score = subtitle.render("{0}".format(deliberative_snake.bananas), 1, 'olivedrab')
    screen.blit(deliberative_banana_score, (33.7 * SQUARE_SIZE, 7.8 * SQUARE_SIZE))
    screen.blit(strawberry_icon.convert_alpha(), (35.1 * SQUARE_SIZE, 7.5 * SQUARE_SIZE))
    deliberative_strawberry_score = subtitle.render("{0}".format(deliberative_snake.strawberries), 1, 'olivedrab')
    screen.blit(deliberative_strawberry_score, (36.2 * SQUARE_SIZE, 7.8 * SQUARE_SIZE))
    screen.blit(mushroom_icon.convert_alpha(), (37.6 * SQUARE_SIZE, 7.5 * SQUARE_SIZE))
    deliberative_mushroom_score = subtitle.render("{0}".format(deliberative_snake.mushrooms), 1, 'olivedrab')
    screen.blit(deliberative_mushroom_score, (38.7 * SQUARE_SIZE, 7.8 * SQUARE_SIZE))
    screen.blit(ice_icon.convert_alpha(), (40.1 * SQUARE_SIZE, 7.5 * SQUARE_SIZE))
    deliberative_ice_score = subtitle.render("{0}".format(deliberative_snake.ices), 1, 'olivedrab')
    screen.blit(deliberative_ice_score, (41.2 * SQUARE_SIZE, 7.8 * SQUARE_SIZE))
    screen.blit(dispenser_icon.convert_alpha(), (42.6 * SQUARE_SIZE, 7.8 * SQUARE_SIZE))
    deliberative_dispenser_score = subtitle.render("{0}".format(deliberative_snake.dispenser), 1, 'olivedrab')
    screen.blit(deliberative_dispenser_score, (43.5 * SQUARE_SIZE, 7.8 * SQUARE_SIZE))

    ## REACTIVE SNAKE
    screen.blit(reactive_snake_icon.convert_alpha(), (31 * SQUARE_SIZE, 11 * SQUARE_SIZE))
    reactiveTxt = subtitle.render("Reactive Snake", 1, 'orange2')
    screen.blit(reactiveTxt, (32.5 * SQUARE_SIZE, 11.5 * SQUARE_SIZE))
    screen.blit(apple_icon.convert_alpha(), (30.1 * SQUARE_SIZE, 12.5 * SQUARE_SIZE))
    reactive_apple_score = subtitle.render("{0}".format(reactive_snake.apples), 1, 'orange2')
    screen.blit(reactive_apple_score, (31.2 * SQUARE_SIZE, 12.8 * SQUARE_SIZE))
    screen.blit(banana_icon.convert_alpha(), (32.6 * SQUARE_SIZE, 12.5 * SQUARE_SIZE))
    reactive_banana_score = subtitle.render("{0}".format(reactive_snake.bananas), 1, 'orange2')
    screen.blit(reactive_banana_score, (33.7 * SQUARE_SIZE, 12.8 * SQUARE_SIZE))
    screen.blit(strawberry_icon.convert_alpha(), (35.1 * SQUARE_SIZE, 12.5 * SQUARE_SIZE))
    reactive_strawberry_score = subtitle.render("{0}".format(reactive_snake.strawberries), 1, 'orange2')
    screen.blit(reactive_strawberry_score, (36.2 * SQUARE_SIZE, 12.8 * SQUARE_SIZE))
    screen.blit(mushroom_icon.convert_alpha(), (37.6 * SQUARE_SIZE, 12.5 * SQUARE_SIZE))
    reactive_mushroom_score = subtitle.render("{0}".format(reactive_snake.mushrooms), 1, 'orange2')
    screen.blit(reactive_mushroom_score, (38.7 * SQUARE_SIZE, 12.8 * SQUARE_SIZE))
    screen.blit(ice_icon.convert_alpha(), (40.1 * SQUARE_SIZE, 12.5 * SQUARE_SIZE))
    reactive_ice_score = subtitle.render("{0}".format(reactive_snake.ices), 1, 'orange2')
    screen.blit(reactive_ice_score, (41.2 * SQUARE_SIZE, 12.8 * SQUARE_SIZE))
    screen.blit(dispenser_icon.convert_alpha(), (42.6 * SQUARE_SIZE, 12.8 * SQUARE_SIZE))
    reactive_dispenser_score = subtitle.render("{0}".format(reactive_snake.dispenser), 1, 'orange2')
    screen.blit(reactive_dispenser_score, (43.5 * SQUARE_SIZE, 12.8 * SQUARE_SIZE))

    ## DISPENSER SNAKE
    screen.blit(dispenser_snake_icon.convert_alpha(), (31 * SQUARE_SIZE, 16 * SQUARE_SIZE))
    dispenserTxt = subtitle.render("Dispenser Snake", 1, 'indianred')
    screen.blit(dispenserTxt, (32.5 * SQUARE_SIZE, 16.5 * SQUARE_SIZE))
    screen.blit(apple_icon.convert_alpha(), (30.1 * SQUARE_SIZE, 17.5 * SQUARE_SIZE))
    dispenser_apple_score = subtitle.render("{0}".format(dispenser_snake.apples), 1, 'indianred')
    screen.blit(dispenser_apple_score, (31.2 * SQUARE_SIZE, 17.8 * SQUARE_SIZE))
    screen.blit(banana_icon.convert_alpha(), (32.6 * SQUARE_SIZE, 17.5 * SQUARE_SIZE))
    dispenser_banana_score = subtitle.render("{0}".format(dispenser_snake.bananas), 1, 'indianred')
    screen.blit(dispenser_banana_score, (33.7 * SQUARE_SIZE, 17.8 * SQUARE_SIZE))
    screen.blit(strawberry_icon.convert_alpha(), (35.1 * SQUARE_SIZE, 17.5 * SQUARE_SIZE))
    dispenser_strawberry_score = subtitle.render("{0}".format(dispenser_snake.strawberries), 1, 'indianred')
    screen.blit(dispenser_strawberry_score, (36.2 * SQUARE_SIZE, 17.8 * SQUARE_SIZE))
    screen.blit(mushroom_icon.convert_alpha(), (37.6 * SQUARE_SIZE, 17.5 * SQUARE_SIZE))
    dispenser_mushroom_score = subtitle.render("{0}".format(dispenser_snake.mushrooms), 1, 'indianred')
    screen.blit(dispenser_mushroom_score, (38.7 * SQUARE_SIZE, 17.8 * SQUARE_SIZE))
    screen.blit(ice_icon.convert_alpha(), (40.1 * SQUARE_SIZE, 17.5 * SQUARE_SIZE))
    dispenser_ice_score = subtitle.render("{0}".format(dispenser_snake.ices), 1, 'indianred')
    screen.blit(dispenser_ice_score, (41.2 * SQUARE_SIZE, 17.8 * SQUARE_SIZE))
    screen.blit(dispenser_icon.convert_alpha(), (42.6 * SQUARE_SIZE, 17.8 * SQUARE_SIZE))
    dispenser_dispenser_score = subtitle.render("{0}".format(dispenser_snake.dispenser), 1, 'indianred')
    screen.blit(dispenser_dispenser_score, (43.5 * SQUARE_SIZE, 17.8 * SQUARE_SIZE))

    ## TRAP SNAKE
    screen.blit(trap_snake_icon.convert_alpha(), (31 * SQUARE_SIZE, 21 * SQUARE_SIZE))
    trapTxt = subtitle.render("Trap Snake", 1, 'lightslategrey')
    screen.blit(trapTxt, (32.5 * SQUARE_SIZE, 21.5 * SQUARE_SIZE))
    screen.blit(apple_icon.convert_alpha(), (30.1 * SQUARE_SIZE, 22.5 * SQUARE_SIZE))
    trap_apple_score = subtitle.render("{0}".format(trap_snake.apples), 1, 'lightslategrey')
    screen.blit(trap_apple_score, (31.2 * SQUARE_SIZE, 22.8 * SQUARE_SIZE))
    screen.blit(banana_icon.convert_alpha(), (32.6 * SQUARE_SIZE, 22.5 * SQUARE_SIZE))
    trap_banana_score = subtitle.render("{0}".format(trap_snake.bananas), 1, 'lightslategrey')
    screen.blit(trap_banana_score, (33.7 * SQUARE_SIZE, 22.8 * SQUARE_SIZE))
    screen.blit(strawberry_icon.convert_alpha(), (35.1 * SQUARE_SIZE, 22.5 * SQUARE_SIZE))
    trap_strawberry_score = subtitle.render("{0}".format(trap_snake.strawberries), 1, 'lightslategrey')
    screen.blit(trap_strawberry_score, (36.2 * SQUARE_SIZE, 22.8 * SQUARE_SIZE))
    screen.blit(mushroom_icon.convert_alpha(), (37.6 * SQUARE_SIZE, 22.5 * SQUARE_SIZE))
    trap_mushroom_score = subtitle.render("{0}".format(trap_snake.mushrooms), 1, 'lightslategrey')
    screen.blit(trap_mushroom_score, (38.7 * SQUARE_SIZE, 22.8 * SQUARE_SIZE))
    screen.blit(ice_icon.convert_alpha(), (40.1 * SQUARE_SIZE, 22.5 * SQUARE_SIZE))
    trap_ice_score = subtitle.render("{0}".format(trap_snake.ices), 1, 'lightslategrey')
    screen.blit(trap_ice_score, (41.2 * SQUARE_SIZE, 22.8 * SQUARE_SIZE))
    screen.blit(dispenser_icon.convert_alpha(), (42.6 * SQUARE_SIZE, 22.8 * SQUARE_SIZE))
    trap_dispenser_score = subtitle.render("{0}".format(trap_snake.dispenser), 1, 'lightslategrey')
    screen.blit(trap_dispenser_score, (43.5 * SQUARE_SIZE, 22.8 * SQUARE_SIZE))


if __name__ == "__main__":
    main()
