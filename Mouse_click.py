import os, sys
from pynput.mouse import Button, Controller
import win32api
from pynput.mouse import Listener
import logging

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

mouse = Controller()
mousePos = mouse.position
mouseclick = mouse.click(Button.left, 1)
run = True
open("mouseclick.txt", "w+")
os.remove("mouseclick.txt")
open("mouseclick.txt", "w+")
while run:
    mouseclick = mouse.click(Button.left, 1)
    if mouseclick:
        print("yes")
        file1 = open("mouseclick.txt", "a+")
        file1.writelines(str(mousePos) + "\n")
        run = False
