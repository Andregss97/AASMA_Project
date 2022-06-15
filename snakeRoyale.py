pygame as p
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

def triggerIce(snakes, ix):
    for i in range(4):
        if i != ix:
            snakes[i].freeze()

def triggerMushroom(snakes, ix):
    snakes[ix].globalScore -= 1
    for i in range(4):
            if i != ix:
                snakes[i].poison()

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
    # deliberative_snake : orange2,
    # trap_snake : lightslategrey,
    # dispenser_snake : indianred
    deliberative_snake = Deliberative_Snake()
    reactive_snake = Reactive_Snake()
    dispenser_snake = Dispenser_Snake()
    trap_snake = Trap_Snake()
    snakes.append(deliberative_snake)
    snakes.append(reactive_snake)
    snakes.append(dispenser_snake)
    snakes.append(trap_snake)


    screen.fill(screen_color)

    deliberative_snake.drawSnake(screen)
    reactive_snake.drawSnake(screen)
    dispenser_snake.drawSnake(screen)
    trap_snake.drawSnake(screen)

    deliberative_snake.scanArea(screen, fruits, traps, dispensers)

    fruits.drawFruits(screen)
    traps.drawTraps(screen)
    dispensers.drawDispensers(screen)
    board.drawLines(screen)


    SCREEN_UPDATE = p.USEREVENT
    p.time.set_timer(SCREEN_UPDATE, 300)

    while running:
        print("\n########\nDEBUG: MAIN CYCLE: ")
        reactive_snake.action(fruits, dispensers, traps, snakes)
        reactive_snake.moveSnake()

        deliberative_snake.action(dispensers, snakes)
        deliberative_snake.moveSnake()

        dispenser_snake.action(fruits, dispensers, traps, snakes)
        dispenser_snake.moveSnake()

        trap_snake.action(fruits, dispensers, traps, snakes)
        trap_snake.moveSnake()

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
                print("--------------------- TRAP SNAKE --------------------")
                print("Global Score: ", trap_snake.globalScore)
                print("Snake Size: ", trap_snake.size)
                print("Apples: ", trap_snake.apples, " x2 points")
                print("Bananas: ", trap_snake.bananas, " x3 points")
                print("Strawberries: ", trap_snake.strawberries, " x5 points")
                print("Mushrooms: ", trap_snake.mushrooms, "x(-1) points")
                print("Ice: ", trap_snake.ices)
                print("Dispenser: ", trap_snake.dispenser)
                print("----------------------------------------------------------")
                p.quit()
                sys.exit()

            if e.type == p.KEYDOWN:
                if e.key == p.K_d:
                    if deliberative_snake_screen :
                        deliberative_snake_screen = False
                    else:
                        deliberative_snake_screen = True


        # TRAP SNAKE
        if trap_snake.body[0] in fruits.apples:
            # snake caught an apple
            # print("APPLE!!!")
            # delete APPLE from the board and fruits class
            fruits.apples.remove(trap_snake.body[0])
            board.busy_cells.remove(trap_snake.body[0])
            # increase snake size
            trap_snake.increaseSize()
            # add points
            trap_snake.apples += 1
            trap_snake.globalScore += fruits.applePoints

        if trap_snake.body[0] in fruits.bananas:
            # snake caught a banana
            # print("BANANA!!!")
            # delete APPLE from the board and fruits class
            fruits.bananas.remove(trap_snake.body[0])
            board.busy_cells.remove(trap_snake.body[0])
            # increase snake size
            trap_snake.increaseSize()
            # add points
            trap_snake.bananas += 1
            trap_snake.globalScore += fruits.bananaPoints

        if trap_snake.body[0] in fruits.strawberries:
            # snake caught a strawberry
            # print("STRAWBERRY!!!")
            # delete APPLE from the board and fruits class
            fruits.strawberries.remove(trap_snake.body[0])
            board.busy_cells.remove(trap_snake.body[0])
            # increase snake size
            trap_snake.increaseSize()
            # add points
            trap_snake.strawberries += 1
            trap_snake.globalScore += fruits.strawberryPoints

        if trap_snake.body[0] in traps.mushrooms:
            # snake caught a mushroom
            # print("MUSHROOM >__<")
            # delete APPLE from the board and fruits class
            traps.mushrooms.remove(trap_snake.body[0])
            board.busy_cells.remove(trap_snake.body[0])
            # add points
            trap_snake.mushrooms += 1
            #triggerMushroom(3, snakes)

        if trap_snake.body[0] in traps.ices:
            # snake caught an ice
            # print("ICE *__*")
            # delete APPLE from the board and fruits class
            traps.ices.remove(trap_snake.body[0])
            board.busy_cells.remove(trap_snake.body[0])
            # add points
            trap_snake.ices += 1
            #triggerIce(3,snakes)

        if trap_snake.body[0] in dispensers.dispensers and not trap_snake.activeDispenser:
            # print("DISPENSER :P")
            for dispenserPos in dispensers.dispensers:
                if trap_snake.body[0] == dispenserPos and dispensers.STATE == 0:
                    trap_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    trap_snake.dispenser += 1
                    dispenserTimer = p.time.get_ticks()
                if trap_snake.body[0] == dispenserPos and dispensers.STATE == 1:
                    trap_snake.activeDispenser = True
                    dispensers.num_snakes += 1
                    trap_snake.dispenser += 1
            if dispensers.STATE == 0 and trap_snake.activeDispenser:
                dispensers.STATE = 1

        ############################################################################

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
            #triggerMushroom(0, snakes)

        if deliberative_snake.body[0] in traps.ices:
            # snake caught an ice
            # print("ICE *__*")
            # delete APPLE from the board and fruits class
            traps.ices.remove(deliberative_snake.body[0])
            deliberative_snake.icesScanned.remove(deliberative_snake.body[0])
            board.busy_cells.remove(deliberative_snake.body[0])
            # add points
            deliberative_snake.ices += 1
            #triggerIce(0,snakes)

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
            print("\n DELIBERATIVE SNAKE LOST !\n", deliberative_snake.body[0])
            print("Head: ", deliberative_snake.body[0])
            print("Body: " + str(deliberative_snake.body[0:3]) + "...]")
            score = True

        if reactive_snake.body[0] in reactive_snake.body[1:] or reactive_snake.body[0].x < 0 or reactive_snake.body[0].x >= board.boardSize or reactive_snake.body[0].y < 0 or reactive_snake.body[0].y >= board.boardSize:
            # snake hit itself or went off the edges
            print("\n REACTIVE SNAKE LOST !\n", reactive_snake.body[0])
            print("Head: ", reactive_snake.body[0])
            print("Body: " + str(reactive_snake.body[0:3]) + "...]")
            score = True

        if dispenser_snake.body[0] in dispenser_snake.body[1:] or dispenser_snake.body[0].x < 0 or dispenser_snake.body[0].x >= board.boardSize or dispenser_snake.body[0].y < 0 or dispenser_snake.body[0].y >= board.boardSize:
            # snake hit itself or went off the edges
            print("\n DISPENSER SNAKE LOST !\n", dispenser_snake.body[0])
            print("Head: ", dispenser_snake.body[0])
            print("Body: " + str(dispenser_snake.body[0:3]) + "...]")
            score = True

        if trap_snake.body[0] in trap_snake.body[1:] or trap_snake.body[0].x < 0 or trap_snake.body[0].x >= board.boardSize or trap_snake.body[0].y < 0 or trap_snake.body[0].y >= board.boardSize:
            # snake hit itself or went off the edges
            print("\n TRAP SNAKE LOST !\n")
            print("Head: ", trap_snake.body[0])
            print("Body: " + str(trap_snake.body[0:3]) + "...]")
            score = True

        if deliberative_snake.size == 50 or deliberative_snake.globalScore >= 150:
            # snake achieved the maximum size or points and WON!
            print("\n DELIBERATIVE SNAKE WINS !\n")
            score = True

        if reactive_snake.size == 50 or reactive_snake.globalScore >= 150:
            # snake achieved the maximum size or points and WON!
            print("\n REACTIVE SNAKE WINS !\n")
            score = True

        if dispenser_snake.size == 50 or dispenser_snake.globalScore == 150:
            # snake achieved the maximum size or points and WON!
            print("\n DISPENSER SNAKE WINS !\n")
            score = True

        if trap_snake.size == 50 or trap_snake.globalScore == 150:
            # snake achieved the maximum size or points and WON!
            print("\n TRAP SNAKE WINS !\n")
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
            print("--------------------- TRAP SNAKE --------------------")
            print("Global Score: ", trap_snake.globalScore)
            print("Snake Size: ", trap_snake.size)
            print("Apples: ", trap_snake.apples, " x2 points")
            print("Bananas: ", trap_snake.bananas, " x3 points")
            print("Strawberries: ", trap_snake.strawberries, " x5 points")
            print("Mushrooms: ", trap_snake.mushrooms, "x(-1) points")
            print("Ice: ", trap_snake.ices)
            print("Dispenser: ", trap_snake.dispenser)
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
            trap_snake.drawSnake(screen)

            if deliberative_snake.exploreTO != [] and deliberative_snake.exploreTO[0] not in deliberative_snake.visibleArea and deliberative_snake.exploreTO[0] not in deliberative_snake.body:
                p.draw.rect(screen, "red", p.Rect(deliberative_snake.exploreTO[0].x * SQUARE_SIZE, deliberative_snake.exploreTO[0].y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)
            board.drawLines(screen)
            pass
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
            trap_snake.drawSnake(screen)

            board.drawLines(screen)
        p.display.update()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main()