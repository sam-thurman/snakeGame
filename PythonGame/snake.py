import random
import pygame
import tkinter as tk
from tkinter import messagebox
from collections import Counter
'''
Drawing in pygame starts in upper left hand corner of object
'''

class Cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color


    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0]+self.dirnx, self.pos[1] + self.dirny)
        

    def draw(self, surface, eyes=False):
        dis = self.w//self.rows
        i = self.pos[0] # grid row
        j = self.pos[1] # grid col
                                                # add 1s and minus 2s to stay inside grid lines
        pygame.draw.rect(surface, self.color, ((i*dis)+1, (j*dis)+1, dis-2, dis-2))
        # draw eyes
        if eyes:
            centre = dis//2
            radius = 3
            circMid1 = ((i*dis)+centre-radius, (j*dis)+8)
            circMid2 = ((i*dis)+dis-radius*2, (j*dis)+8)
            pygame.draw.circle(surface, (255,255,255), circMid1, radius)
            pygame.draw.circle(surface, (255,255,255), circMid2, radius)

# Snake obj contains multiple Cube objs
class Snake(object):
    # "snake body", will contain the Cubes
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color

        # create head Cube at current position (preset) and append it to body.
        self.head = Cube(pos)
        self.body.append(self.head)

        # directions for x and y (either -1, 0, or 1) keepin track of the direction we're moving
        # only one value can be !=0 (can only move in one direction at once)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # dict of all key values, indicating keys that are pressed or not
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    # add key to turns that is the current position of head of snake
                    # set it equal to the direction we turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    # once we reach the last cube, remove turn from list
                    self.turns.pop(p)

            # check if we've reached a window edge
            else:
                # if yes, move back in opposite direction, causing a loss
                    # ex. (if moving left, hitting left wall, move right)
                if c.dirnx == -1 and c.pos[0]<=0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1]<=0: c.pos = (c.pos[0], c.rows-1)
                # if no edge is met, move cube 1 position in current direction
                else: c.move(c.dirnx, c.dirny)


    def reset(self, pos):
        pass

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        # check which way the tail of snake is moving (so we know the directions and location of the added Cube)
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))
        # add direction to added cube
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy


    def draw(self, surface):
        for i, c in enumerate(self.body):
            # check if Cube is head
            if i == 0:
                # if yes, add eyes and draw
                c.draw(surface, True)
            else:
                # else draw without eyes
                c.draw(surface)

def drawGrid(w, rows, surface):
    size_btwn = w//rows
    x = 0
    y = 0
    for i in range(rows):
        x += size_btwn
        y += size_btwn
                                                # start, end positions 
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w)) # vertical line
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) # horizontal line

def redrawWindow(surface):
    global width, rows, snake, snack
    # fill the screen (with black)
    surface.fill((0,0,0))
    # draw the grid
    drawGrid(width, rows, surface)
    # draw the snake
    snake.draw(surface)
    # draw the snack
    snack.draw(surface)
    # update display
    pygame.display.update()
    pass

def randomSnack():
    global rows, snake
    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        # check if random position is the same as current position of any snake cubes
        if len(list(filter(lambda z: z.pos == (x,y), positions)))>0:
            continue
        else:
            break
    
    return (x,y)


def message_box(subject, content):
    pass

def main():
    global width, rows, snake, snack

    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
             #color(red)  #position
    snake = Snake((255, 0, 0), (10,10))
    snack = Cube(randomSnack(), color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        # create 50 ms time delay
        pygame.time.delay(50)
        # make sure our game doesn't run faster than 10 fps
        clock.tick(10)
        # move snake
        snake.move()
        # log and check positions
        positions = [x.pos for x in snake.body]
        #check if there are more than one body squares in the same position
        if filter(lambda x: x.value>1,Counter(positions)):
            win.fill("green")
            pygame.draw.text(f"Game Over, you're score was {len(snake.body)}",
                     topleft=(100,350), fontsize=30)
        
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(randomSnack(), color=(0,255,0))
        
        redrawWindow(win)

    pass

main()