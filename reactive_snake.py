from random import random
from xmlrpc.client import MAXINT, MININT
import pygame as p
import numpy as np
from pygame import Vector2
from board import *

class Reactive_Snake:

    def __init__(self):
        self.color = "orange2"

        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = p.Vector2(1, 0)
        self.objective = p.Vector2
        self.size = len(self.body)
        self.activeDispenser = False
        # TODO: rearrange which snake goes where in the start
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
        # shared_dispenser = 0
        # TODO: Criar várias cobras e identificar estes eventos

    def action(self, fruits, dispensers, traps):
        # Determines which action given the GREEDY priority and updates direction
        if not self.activeDispenser:
            positions = dispensers.dispensers + fruits.strawberries + fruits.bananas  + fruits.apples + traps.ices + traps.mushrooms
            points = [dispensers.dispenserPoints] * len(dispensers.dispensers) + [fruits.strawberryPoints] * len(fruits.strawberries) + [fruits.bananaPoints] * len(fruits.bananas) + \
                [fruits.applePoints] * len(fruits.apples) +  [traps.icePoints] * len(traps.ices) + [traps.mushroomPoints] * len(traps.mushrooms)

        else:
            positions = fruits.strawberries + fruits.bananas + fruits.apples + traps.ices + traps.mushrooms
            points = [fruits.strawberryPoints] * len(fruits.strawberries) + [fruits.bananaPoints] * len(fruits.bananas) + \
                [fruits.applePoints] * len(fruits.apples) + [traps.icePoints] * len(traps.ices) + [traps.mushroomPoints] * len(traps.mushrooms) 

        '''if(self.objective in positions):
            self.direction = self.directionToGo(self.objective)
        else:'''
        self.direction = self.selectObjective(positions, points)

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


    def selectObjective(self, objective_positions, points):
        # Calculates best objective (Worth more and close by)
        min_dist = MAXINT
        max_points = MININT
        for i in range(len(objective_positions)):
            distance = self.body[0].distance_to(objective_positions[i])
            if points[i] >= max_points:
                if distance < min_dist:
                    min_dist = distance
                    max_points = points[i]
                    move_pos = objective_positions[i]
                
        self.objective = move_pos
        return self.directionToGo(self.objective)

    def directionToGo(self, pos):
        # Check distance between snake and goto position
        distance = self.body[0].distance_to(pos)
        # Possible Moves
        moveUp = self.body[0] + Vector2(0, 1)
        moveDown = self.body[0] + Vector2(0, -1)
        moveLeft = self.body[0] + Vector2(-1, 0)
        moveRight = self.body[0] + Vector2(1, 0)

        # Check if moving UP is efficiant
        if distance >= pos.distance_to(moveUp):
            if self.direction != Vector2(0, -1) and moveUp not in self.body:
                return Vector2(0, 1)
            elif pos.distance_to(moveLeft) < pos.distance_to(moveRight) and moveLeft not in self.body:
                return Vector2(-1, 0)
            elif pos.distance_to(moveLeft) > pos.distance_to(moveRight) and moveRight not in self.body:
                return Vector2(1, 0)
            elif pos.distance_to(moveLeft) == pos.distance_to(moveRight):
                if moveRight not in self.body:
                    return Vector2(1, 0)
                elif moveLeft not in self.body:
                    return Vector2(-1, 0)
            elif moveRight not in self.body:
                    return Vector2(1, 0)
            elif moveLeft not in self.body:
                return Vector2(-1, 0)
            else:
                return self.direction

        # Check if moving DOWN is efficiant
        if distance >= pos.distance_to(moveDown):
            if self.direction != Vector2(0, 1) and moveDown not in self.body:
                return Vector2(0, -1)
            elif pos.distance_to(moveLeft) < pos.distance_to(moveRight) and moveLeft not in self.body:
                return Vector2(-1, 0)
            elif pos.distance_to(moveLeft) > pos.distance_to(moveRight) and moveRight not in self.body:
                return Vector2(1, 0)
            elif pos.distance_to(moveLeft) == pos.distance_to(moveRight):
                if moveRight not in self.body:
                    return Vector2(1, 0)
                elif moveLeft not in self.body:
                    return Vector2(-1, 0)
            elif moveRight not in self.body:
                    return Vector2(1, 0)
            elif moveLeft not in self.body:
                return Vector2(-1, 0)
            else:
                return self.direction
        
        # Check if moving RIGHT is efficiant
        if distance >= pos.distance_to(moveRight):
            if self.direction != Vector2(-1, 0) and moveRight not in self.body:
                return Vector2(1, 0)
            elif pos.distance_to(moveUp) < pos.distance_to(moveDown) and moveUp not in self.body:
                return Vector2(0, 1)
            elif pos.distance_to(moveUp) > pos.distance_to(moveDown) and moveDown not in self.body:
                return Vector2(0, -1)
            elif pos.distance_to(moveUp) == pos.distance_to(moveDown):
                if moveUp not in self.body:
                    return Vector2(0, 1)
                elif moveDown not in self.body:
                    return Vector2(0, -1)
            elif moveUp not in self.body:
                    return Vector2(0, 1)
            elif moveDown not in self.body:
                return Vector2(0, -1)
            else:
                return self.direction

        # Check if moving LEFT is efficiant
        if distance >= pos.distance_to(moveLeft):
            if self.direction != Vector2(1, 0) and moveLeft not in self.body:
                return Vector2(-1, 0)
            elif pos.distance_to(moveUp) < pos.distance_to(moveDown) and moveUp not in self.body:
                return Vector2(0, 1)
            elif pos.distance_to(moveUp) > pos.distance_to(moveDown) and moveDown not in self.body:
                return Vector2(0, -1)
            elif pos.distance_to(moveUp) == pos.distance_to(moveDown):
                if moveUp not in self.body:
                    return Vector2(0, 1)
                elif moveDown not in self.body:
                    return Vector2(0, -1)
            elif moveUp not in self.body:
                    return Vector2(0, 1)
            elif moveDown not in self.body:
                return Vector2(0, -1)
            else:
                return self.direction
        
        