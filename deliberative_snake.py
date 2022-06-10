import random
import pygame as p
import numpy as np
from pygame import Vector2
from board import *
from Node import *

VISION_RANGE = 5

apple = p.image.load('snake_imgs/apple.svg')
banana = p.image.load('snake_imgs/banana.svg')
strawberry = p.image.load('snake_imgs/strawberry.svg')

mushroom = p.image.load('snake_imgs/mushroom.svg')
ice = p.image.load('snake_imgs/ice.svg')

cooldown = p.image.load('snake_imgs/cooldown.svg')

class Deliberative_Snake:

    def __init__(self):
        self.color = "olivedrab"
        self.scanColor = "lemonchiffon3"
        self.visibleArea = []
        
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = p.Vector2(1, 0)
        self.exploreTO = []
        self.size = len(self.body)
        # TODO: rearrange which snake goes where in the start
        self.globalScore = 0

        # F R U I T S
        self.apples = 0
        self.applesScanned = []
        self.bananas = 0
        self.bananasScanned = []
        self.strawberries = 0
        self.strawberriesScanned = []

        # T R A P S
        self.mushrooms = 0
        self.mushroomsScanned = []
        self.ices = 0
        self.icesScanned = []

        # D I S P E N S E R
        self.dispenser = 0
        self.dispensersScanned = []
        self.activeDispenser = False
        # shared_dispenser = 0
        # TODO: Criar várias cobras e identificar estes eventos

    def drawSnake (self, screen):
        for cell in self.body:
            x_pos = int(cell.x * SQUARE_SIZE)
            y_pos = int(cell.y * SQUARE_SIZE)
            cell_rect = p.Rect(x_pos, y_pos, SQUARE_SIZE, SQUARE_SIZE)

            p.draw.rect(screen, self.color, cell_rect)
    
    def moveSnake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def increaseSize(self):
        body_copy = self.body[:]
        body_copy.append(body_copy[-1])
        self.body = body_copy[:]

    def euclidianDistance (self, start: Vector2, end: Vector2):
        return np.sqrt(np.add(np.square(int(np.subtract(end.x,start.x))), np.square(int(np.subtract(end.y, start.y)))))

    def scanArea(self, screen, fruits, traps, dispensers):
        self.visibleArea = []
        for i in range (DIMENSION):
            for j in range (DIMENSION):
                pos = p.Vector2(i,j)
                if np.round(self.euclidianDistance(self.body[0], pos), 0) <= VISION_RANGE and pos not in self.body and pos not in self.visibleArea:
                    self.visibleArea.append(pos)
        for cell in self.visibleArea:
            if cell in fruits.apples and cell not in self.applesScanned:
                self.applesScanned.append(cell)
            if cell in fruits.bananas and cell not in self.bananasScanned:
                self.bananasScanned.append(cell)
            if cell in fruits.strawberries and cell not in self.strawberriesScanned:
                self.strawberriesScanned.append(cell)
            if cell in traps.mushrooms and cell not in self.mushroomsScanned:
                self.mushroomsScanned.append(cell)
            if cell in traps.ices and cell not in self.icesScanned:
                self.icesScanned.append(cell)
            if cell in dispensers.dispensers and cell not in self.dispensersScanned:
                self.dispensersScanned.append(cell)
            # draw observable cells
            p.draw.rect(screen, self.scanColor, p.Rect(cell.x * SQUARE_SIZE, cell.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    
    def drawFruits(self, screen):

        for apple_pos in self.applesScanned:
            screen.blit(apple.convert_alpha(), (apple_pos.x * SQUARE_SIZE, apple_pos.y * SQUARE_SIZE))

        for banana_pos in self.bananasScanned:
            screen.blit(banana.convert_alpha(), (banana_pos.x * SQUARE_SIZE, banana_pos.y * SQUARE_SIZE))

        for strawberry_pos in self.strawberriesScanned:
            screen.blit(strawberry.convert_alpha(), (strawberry_pos.x * SQUARE_SIZE, strawberry_pos.y * SQUARE_SIZE))

    def drawTraps(self, screen):

        for mushroom_pos in self.mushroomsScanned:
            screen.blit(mushroom.convert_alpha(), (mushroom_pos.x * SQUARE_SIZE, mushroom_pos.y * SQUARE_SIZE))

        for ice_pos in self.icesScanned:
            screen.blit(ice.convert_alpha(), (ice_pos.x * SQUARE_SIZE, ice_pos.y * SQUARE_SIZE))

    def drawDispensers(self, screen, dispensers):
        for dispenser in self.dispensersScanned:
            p.draw.rect(screen, dispensers.dispenser_color, p.Rect(dispenser.x * SQUARE_SIZE, dispenser.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=1)

    def updateDispenserState (self, screen, dispensers):
        for index in range(len(self.dispensersScanned)):
                if dispensers.STATE == 1:
                    dispensers.dispenser_color = p.Color("chartreuse3")
                if dispensers.STATE == 2:
                    dispensers.dispenser_color = p.Color("hotpink1")
                    screen.blit(cooldown.convert_alpha(), (self.dispensersScanned[index].x * SQUARE_SIZE, self.dispensersScanned[index].y * SQUARE_SIZE))

    def search(self, start, goals, obstacles, actions):
        # print("START " + str(start))
        # print("GOALS " + str(goals))
        open = []
        closed = []
        path = []

        start_node = Node(start, None)
        goal_nodes = [Node(g, None) for g in goals]

        open.append(start_node)

        while len(open) > 0:
            open.sort()
            node = open.pop(0)
            closed.append(node)
            if node in goal_nodes:
                while node != start_node:
                    path.append(node.state)
                    node = node.parent
                path.append(node.state)
                return path[::-1]

            children = self.getChildren(node, obstacles, actions)
            for child in children:
                if child not in closed and self.lowest_f(open, child):
                    open.append(child)

        return path[::-1]

    def lowest_f(self, open, child):
        for node in open:
            if (node == child and node.f <= child.f):
                return False
        return True

    def getChildren(self, parent, obstacles, actions):
        children = []
        for a in actions:
            neighbour_pos = parent.state + a
            if neighbour_pos not in obstacles:
                newChild = Node(neighbour_pos, parent)
                newChild.g = parent.g + 1
                newChild.h = Vector2.distance_squared_to(parent.state, neighbour_pos)
                children.append(newChild)
        return children


    def action(self, dispensers, snakes):
        actions = [Vector2(0,1), Vector2(0,-1), Vector2(1,0), Vector2(-1,0)]
        obstacles = []
        obstacles.extend(self.mushroomsScanned)
        if self.body[0] in self.exploreTO:
            self.exploreTO = []
        for s in snakes:
            obstacles.extend(s.body)
        if not self.activeDispenser and dispensers.STATE != 2:
            goals = self.dispensersScanned
        else:
            goals = self.applesScanned + self.bananasScanned + self.strawberriesScanned + self.icesScanned
        if goals == []:
            if self.exploreTO == []:
                while True:
                    rand_X = randrange(DIMENSION)
                    rand_Y = randrange(DIMENSION)
                    new_pos = Vector2(rand_X, rand_Y)
                    if new_pos not in self.body:
                        goals = [new_pos]
                        self.exploreTO = [new_pos]
                        break
            else:
                goals = self.exploreTO
        else:
            self.exploreTO = []
        
        path = self.search(self.body[0], goals, obstacles, actions)
        if self.exploreTO != []:
            print("\n * * EXPLORING * * \n")
        else:
            print("\n * * * \n")

        print(path)

        if len(path) < 2: # can't find/end of path, pick any legal move
            for a in actions:
                if self.body[0] + a not in obstacles:
                    self.direction = a
        else:
            self.direction = path[1] - path[0]
            # print("DIR: " + str(self.direction))
