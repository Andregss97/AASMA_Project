import pygame as p
from pygame import Vector2
from board import *
from Node import *

class Trap_Snake:

    def __init__(self):
        self.color = "lightslategrey"

        self.body = [Vector2(2,DIMENSION-1), Vector2(1,DIMENSION-1), Vector2(0,DIMENSION-1)]
        self.direction = p.Vector2(1, 0)
        self.size = len(self.body)
        self.globalScore = 0

        # F R U I T S
        self.apples = 0
        self.bananas = 0
        self.strawberries = 0

        # T R A P S
        self.mushrooms = 0
        self.ices = 0

        # D I S P E N S E R
        self.dispenser = 0
        self.activeDispenser = False

        self.frozen = False
        self.frozenTS = 0
        self.poisoned = False
        self.poisonedTS = 0
        self.dead = False
        self.winner = False

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
        self.size = len(self.body)

    def search(self, start, goals, obstacles, actions):
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
            if neighbour_pos not in obstacles and neighbour_pos.x >= 0 and neighbour_pos.x < DIMENSION and neighbour_pos.y >= 0 and neighbour_pos.y < DIMENSION:
                newChild = Node(neighbour_pos, parent)
                newChild.g = parent.g + 1
                newChild.h = Vector2.distance_squared_to(parent.state, neighbour_pos)
                newChild.f = newChild.g + newChild.h
                children.append(newChild)
        return children

    def action(self, fruits, dispensers, traps, snakes):
        actions = [Vector2(0,1), Vector2(0,-1), Vector2(1,0), Vector2(-1,0)]
        obstacles = []
        goals = []
        for s in snakes:
            if s != None:
                obstacles.extend(s.body)
        if not self.anyFrozen(snakes):
            goals = traps.ices + traps.mushrooms
        if goals == []:
            if not self.activeDispenser and dispensers.STATE != 2:
                goals = fruits.apples + fruits.bananas + fruits.strawberries + dispensers.dispensers
            else:
                goals = fruits.apples + fruits.bananas + fruits.strawberries

        path = self.search(self.body[0], goals, obstacles, actions)

        if len(path) < 2: # can't find/end of path, pick any legal move
            for a in actions:
                if self.body[0] + a not in obstacles:
                    self.direction = a
        else:
            self.direction = path[1] - path[0]

    def died(self):
        self.body = []
        self.color = "gray"
        self.dead = True

    def won(self):
        self.color = "lightslategrey"
        self.winner = True

    def anyFrozen(self, snakes):
        if not self.frozen:
            for s in snakes:
                if s != None and s.frozen and s != self:
                    return True
        return False
