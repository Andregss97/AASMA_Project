import pygame as p
from random import randrange

WIDTH = HEIGHT = 600
DIMENSION = 20
MAX_FPS = 20
SQUARE_SIZE = HEIGHT // DIMENSION

dispensers = [(15,4), (4,4), (4,15), (15,15)]

NMBR_START_APPLES = 15
NMBR_START_BANANAS = 10
NMBR_START_STRAWBERRIES = 5

apple = p.image.load('snake_imgs/apple.svg')
banana = p.image.load('snake_imgs/banana.svg')
strawberry = p.image.load('snake_imgs/strawberry.svg')


'''
Main function. Handles initializing application and updating graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    running = True
    spawned = False

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        if not spawned:
            drawGameSate(screen)
            spawned = True
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for drawing the board and pieces (to implement)
'''
def drawGameSate(screen):

    drawBoard(screen)   # draw squares of the board
    loadFood(screen)    # spawn food on the board


'''
Draw de squares on the board
'''
def drawBoard(screen):
    square_color = p.Color("white")
    lines_color = p.Color("black")
    dispenser_color = p.Color("hotpink1")
    for c in range(DIMENSION):
        for r in range(DIMENSION):
            if (c,r) in dispensers:
                p.draw.rect(screen, dispenser_color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)
            else:
                p.draw.rect(screen, square_color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    for l in range(DIMENSION):
        p.draw.lines(screen, lines_color, True, [(0, l*SQUARE_SIZE), (DIMENSION*SQUARE_SIZE, l*SQUARE_SIZE)])
        p.draw.lines(screen, lines_color, True, [(l*SQUARE_SIZE, 0), (l*SQUARE_SIZE, DIMENSION*SQUARE_SIZE)])


'''
Spawns N amount of food randomly on the board
'''
def loadFood(screen):
    occupied = []
    count_apples = 0
    count_bananas = 0
    count_strawberries = 0
    while count_apples < NMBR_START_APPLES:
        rand_X = randrange(DIMENSION)
        rand_Y = randrange(DIMENSION)
        if (rand_X, rand_Y) not in occupied:
            if (rand_X, rand_Y) not in dispensers:
                screen.blit(apple, (rand_X*SQUARE_SIZE, rand_Y*SQUARE_SIZE))
                occupied.append((rand_X, rand_Y))
                count_apples += 1
    while count_bananas < NMBR_START_BANANAS:
        rand_X = randrange(DIMENSION)
        rand_Y = randrange(DIMENSION)
        if (rand_X, rand_Y) not in occupied:
            if (rand_X, rand_Y) not in dispensers:
                screen.blit(banana, (rand_X*SQUARE_SIZE, rand_Y*SQUARE_SIZE))
                occupied.append((rand_X, rand_Y))
                count_bananas += 1
    while count_strawberries < NMBR_START_STRAWBERRIES:
        rand_X = randrange(DIMENSION)
        rand_Y = randrange(DIMENSION)
        if (rand_X, rand_Y) not in occupied:
            if (rand_X, rand_Y) not in dispensers:
                screen.blit(strawberry, (rand_X*SQUARE_SIZE, rand_Y*SQUARE_SIZE))
                occupied.append((rand_X, rand_Y))
                count_strawberries += 1



if __name__ == "__main__":
    main()
