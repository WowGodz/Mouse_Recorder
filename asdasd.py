import sys
import os
import pygame
from pynput.mouse import Button, Controller
import time
pygame.init()
window = pygame.display.set_mode((1, 1))
mouse = Controller()
mousePos = mouse.position
run = True

while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    "opens file"
    file1 = open("mouse.txt")
    "two sets of data are being used in points"
    "mouse positions x and y"
    points = set()
    speed = 100
    if keys[pygame.K_RIGHT]:
        speed += 10
    speed = speed
    with open("mouse.txt", "r") as f:
        # each line separately
        for idx, line in enumerate(f):
            # strip \n  & strip ( and ) & split at ,

            pointstring = line.strip().strip("()").split(",")
            # guard against empty/non well formed lines

            if pointstring and len(pointstring) == 2:
                if mousePos == points:
                    mouse.position = line.strip().strip("()").split(",")
                    time.sleep(1. / speed)
                    print(speed)
            else:
                "if for some reason is doesn't work, it'll look for whats wrong in the txt file"
                print(f"Error in line {idx}: '{line}'")
    "starts using the points in the txt File"
    mousePos = points
    pygame.display.update()