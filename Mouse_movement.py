import win32api, os
from pynput.mouse import Button, Controller
from win32api import GetSystemMetrics

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
A = 1
mouse = Controller()
mousePos = mouse.position
run = False
if not run:
    run2 = True
run2 = True

# run2 deletes previous files
while run2:
    a = input('*RESTARTING WILL DELETE PREVIOUS EVENTS* \n'"    Restart(Y/N):")
    a = a.lower()
    if a == "y" or a == "yes":
        run = True
        run2 = False
        open("mouse.txt", "w+")
        os.remove("mouse.txt")
        open("mouse.txt", "w+")
        open("mouseclickR.txt", "w+")
        os.remove("mouseclickR.txt")
        open("mouseclickR.txt", "w+")
        open("mouseclickL.txt", "w+")
        os.remove("mouseclickL.txt")
        open("mouseclickL.txt", "w+")
while run:
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
    if mousePos == mouse.position:
        A += 1
    else:
        for i in range(1):
            for j in range(1):
                print(mouse.position)
                file1 = open("mouse.txt", "a+")
                file1.writelines(str(mousePos) + "\n")
                mouse.position
                mousePos = mouse.position
                if mousePos == mouse.position:
                    mouse.position = mousePos
