import win32api, os
import time
from pynput.mouse import Button, Controller

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
open("mouseclickR.txt", "w+")
os.remove("mouseclickR.txt")
open("mouseclickR.txt", "w+")
open("mouseclickL.txt", "w+")
os.remove("mouseclickL.txt")
open("mouseclickL.txt", "w+")
mouse = Controller()
while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    mousePos = mouse.position
    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            print('Left Button Pressed')
            print("yes")
            file1 = open("mouseclickL.txt", "a+")
            file1.writelines(str(mousePos) + "\n")

    if b != state_right:  # Button state changed
        state_right = b
        print(b)
        if b < 0:
            print('Right Button Pressed')
            print("yes")
            file1 = open("mouseclickR.txt", "a+")
            file1.writelines(str(mousePos) + "\n")

