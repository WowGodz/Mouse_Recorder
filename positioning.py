import time
import sys, os
from pynput.mouse import Controller

speed = 200
fps = [time.sleep(1. / speed)]
mouse = Controller()
run = True
file = open('mouseclickL.txt', 'r')
while run:
    "opens file"
    "two sets of data are being used in points"
    "mouse positions x and y"
    points = set()
    for idx, line in enumerate(file):
        s = line.strip().strip("()").split(",")
        if s and len(s) == 2:
            z, b = line.strip().strip("()").split(",")
            print(z, b)
            time.sleep(1. / 1)
    with open("mouse.txt", "r") as f:
        # each line separately
        for idx, line in enumerate(f):
            # strip \n  & strip ( and ) & split at ,
            pointstring = line.strip().strip("()").split(",")
            # guard against empty/non well formed lines
            if pointstring and len(pointstring) == 2:
                x, y = line.strip().strip("()").split(",")
                mouse.position = (x, y)  # = or (x, y)[0], (x, y)[1] same as -----> = x,y
                time.sleep(1. / speed)

            else:
                "if for some reason is doesn't work, it'll look for whats wrong in the txt file"
                print(f"Error in line {idx}: '{line}'")

    for idx, line in enumerate(file):
        s = line.strip().strip("()").split(",")
        if s and len(s) == 2:
            z, b = line.strip().strip("()").split(",")
            print(z, b)
            time.sleep(1. / 1)
    if mouse.position == (z, b):
        print('yes')
