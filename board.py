import pygame as p
from random import randrange

WIDTH = HEIGHT = 600
DIMENSION = 20
MAX_FPS = 20
SQUARE_SIZE = HEIGHT // DIMENSION

NMBR_START_APPLES = 15
NMBR_START_BANANAS = 10
NMBR_START_STRAWBERRIES = 5

NMBR_START_MUSHROOMS = 3
NMBR_START_ICE = 2

apple = p.image.load('snake_imgs/apple.svg')
banana = p.image.load('snake_imgs/banana.svg')
strawberry = p.image.load('snake_imgs/strawberry.svg')
mushroom = p.image.load('snake_imgs/mushroom.svg')
ice = p.image.load('snake_imgs/ice.svg')

# Dispenser States : 1 - ACTIVE , 0 - ON COOLDOWN
TL_DISPENSER_STATE = 0  # top-left dispenser state
TR_DISPENSER_STATE = 0  # top-right dispenser state
BL_DISPENSER_STATE = 0  # bottom-left dispenser state
BR_DISPENSER_STATE = 0  # bottom-right dispenser state

cooldown = p.image.load('snake_imgs/cooldown.svg')

class Board:
    boardSize = DIMENSION
    tileSize = DIMENSION*SQUARE_SIZE
    busy_cells = [(4,4), (4,15), (15,4), (15,15)] #busy_cells initialized with DISPENSER locations
    dispensers = [(4,4), (4,15), (15,4), (15,15)]
    food_cells = []
    trap_cells = []

    '''
    Draw de squares on the board
    '''
    def drawBoard(self, screen):
        square_color = p.Color("lemonchiffon1")
        dispenser_color = p.Color("hotpink1")

        for c in range(self.boardSize):
            for r in range(self.boardSize):
                if (c,r) in self.dispensers:
                    p.draw.rect(screen, dispenser_color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)
                else:
                    p.draw.rect(screen, square_color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    def drawLines (self, screen):
        lines_color = p.Color("black")
        for l in range(self.boardSize):
            p.draw.lines(screen, lines_color, True, [(0, l * SQUARE_SIZE), (self.tileSize, l * SQUARE_SIZE)])
            p.draw.lines(screen, lines_color, True, [(l * SQUARE_SIZE, 0), (l * SQUARE_SIZE, self.tileSize)])

    def updateDispenserState (self, screen):
        for index in range(len(self.dispensers)):
            if index == 0:
                if TL_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index][0] * SQUARE_SIZE, self.dispensers[index][1] * SQUARE_SIZE))
            if index == 1:
                if TR_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index][0] * SQUARE_SIZE, self.dispensers[index][1] * SQUARE_SIZE))
            if index == 2:
                if BL_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index][0] * SQUARE_SIZE, self.dispensers[index][1] * SQUARE_SIZE))
            if index == 3:
                if BR_DISPENSER_STATE == 1:
                    screen.blit(cooldown, (self.dispensers[index][0] * SQUARE_SIZE, self.dispensers[index][1] * SQUARE_SIZE))
    
    '''
    Spawns N amount of food randomly on the board
    '''
    def spawnFood(self, screen):
        count_apples = 0
        count_bananas = 0
        count_strawberries = 0
        while count_apples < NMBR_START_APPLES:
            rand_X = randrange(self.boardSize)
            rand_Y = randrange(self.boardSize)
            if (rand_X, rand_Y) not in self.busy_cells:
                if (rand_X, rand_Y) not in self.dispensers:
                    screen.blit(apple, (rand_X * SQUARE_SIZE, rand_Y * SQUARE_SIZE))
                    self.busy_cells.append((rand_X, rand_Y))
                    count_apples += 1
        while count_bananas < NMBR_START_BANANAS:
            rand_X = randrange(self.boardSize)
            rand_Y = randrange(self.boardSize)
            if (rand_X, rand_Y) not in self.busy_cells:
                if (rand_X, rand_Y) not in self.dispensers:
                    screen.blit(banana, (rand_X * SQUARE_SIZE, rand_Y * SQUARE_SIZE))
                    self.busy_cells.append((rand_X, rand_Y))
                    count_bananas += 1
        while count_strawberries < NMBR_START_STRAWBERRIES:
            rand_X = randrange(self.boardSize)
            rand_Y = randrange(self.boardSize)
            if (rand_X, rand_Y) not in self.busy_cells:
                if (rand_X, rand_Y) not in self.dispensers:
                    screen.blit(strawberry, (rand_X * SQUARE_SIZE, rand_Y * SQUARE_SIZE))
                    self.busy_cells.append((rand_X, rand_Y))
                    count_strawberries += 1

    def spawnTraps(self, screen):
        count_mushrooms = 0
        count_ice = 0
        while count_mushrooms < NMBR_START_MUSHROOMS:
            rand_X = randrange(self.boardSize)
            rand_Y = randrange(self.boardSize)
            if (rand_X, rand_Y) not in self.busy_cells:
                if (rand_X, rand_Y) not in self.dispensers:
                    screen.blit(mushroom, (rand_X * SQUARE_SIZE, rand_Y * SQUARE_SIZE))
                    self.busy_cells.append((rand_X, rand_Y))
                    count_mushrooms += 1
        while count_ice < NMBR_START_ICE:
            rand_X = randrange(self.boardSize)
            rand_Y = randrange(self.boardSize)
            if (rand_X, rand_Y) not in self.busy_cells:
                if (rand_X, rand_Y) not in self.dispensers:
                    screen.blit(ice, (rand_X * SQUARE_SIZE, rand_Y * SQUARE_SIZE))
                    self.busy_cells.append((rand_X, rand_Y))
                    count_ice += 1

    ## TODO: Implement Board functions
