import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0,color=(255,0,0)):

        pass

    def move(self, dirnx, dirny):

        pass

    def draw(self, surface, eyes=False):

        pass

# Snake obj contains Cube objs
class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass
    
    def draw(self, surface):
        pass


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
    pass

def redrawWindow(surface):
    global width, rows

    # fill the screen (with black)
    surface.fill((0,0,0))
    # draw the grid
    drawGrid(width, rows, surface)
    # update display
    pygame.display.update()
    pass

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows

    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
             #color(red)  #position
    s = Snake((255, 0, 0), (10,10))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        # create 50 ms time delay
        pygame.time.delay(50)
        # make sure our game doesn't run faster than 10 fps
        clock.tick(10)

        redrawWindow(win)

    pass



main()