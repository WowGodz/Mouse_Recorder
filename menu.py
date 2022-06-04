import subprocess
import sys

import os
import pygame
import win32api
from pynput.mouse import Controller
from pygame.locals import *
import time


def loggin():
    pygame.init()

    clock = pygame.time.Clock()

    # it will display on screen
    screen = pygame.display.set_mode([600, 500])

    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''

    # create rectangle
    input_rect = pygame.Rect(350, 200, 140, 32)

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False
    password = open('password.txt', 'r')
    password = password.readline()

    font = pygame.font.SysFont(None, 40)

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    ser = "Enter Password"


    a = 0
    while True:
        keys = pygame.key.get_pressed()
        screen.fill((255, 255, 255))

        draw_text(ser, font, (0, 0, 0), screen, 100, 200)
        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text != password:
                        user_text = ''
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

                if user_text == password and a == 0:
                    a = 1
                    print(a)
                if a == 1:
                    if event.key == pygame.K_RETURN:
                        ser = 'Please Wait ...'
                        a = 0
                        user_text = ''
                        time.sleep(1. / 1)
                        time.sleep(1. / 1)
                        secure()
        # it will set background color of screen

        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        # display.flip() will update only a portion of the
        # screen to updated, not full area

        pygame.display.flip()

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def secure():
    # Setup pygame/window ---------------------------------------- #
    mainClock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption('recorder')
    screen = pygame.display.set_mode((800, 500), 0, 32)

    font = pygame.font.SysFont(None, 20)

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    click = False

    def main_menu(user_text=''):
        global click
        start1_img = pygame.image.load('start1.png')
        start1 = pygame.transform.scale(start1_img, (200, 50))
        start2 = pygame.transform.scale(start1_img, (100, 25))
        s_img = pygame.image.load('s.png')
        s = pygame.transform.scale(s_img, (100, 25))
        click_img = pygame.image.load('click.png')
        click1 = pygame.transform.scale(click_img, (100, 25))
        stop_img = pygame.image.load('stop.png')
        stop = pygame.transform.scale(stop_img, (100, 25))
        record_img = pygame.image.load('record.png')
        record1 = pygame.transform.scale(record_img, (200, 50))
        # basic font for user typed
        base_font = pygame.font.Font(None, 32)
        # create rectangle
        input_rect = pygame.Rect(200, 300, 140, 32)

        # color_active stores color(lightskyblue3) which
        # gets active when input box is clicked by user
        color_active = pygame.Color('lightskyblue3')

        # color_passive store color(chartreuse4) which is
        # color of input box.
        color_passive = pygame.Color('chartreuse4')
        color = color_passive
        active = False
        a = 0
        b = 0
        run = True
        settings = 'settings'
        while run:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                record.run = False
            screen.fill((0, 0, 0))
            r1 = 10
            g1 = 10
            b1 = 10
            r2 = 10
            g2 = 10
            b2 = 10
            apps = open("app.txt", 'r+')
            apps = apps.read()
            draw_text(settings, font, (255, 255, 255), screen, 20, 20)
            draw_text('apps', font, (255, 255, 255), screen, 400, 20)
            draw_text(apps + '\n', font, (255, 255, 255), screen, 1, 420)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(50, 100, 200, 50)
            button_2 = pygame.Rect(50, 200, 200, 50)
            if button_1.collidepoint((mx, my)):
                r1 = 50
                if click:
                    start()
            if button_2.collidepoint((mx, my)):
                r2 = 50
                if click:
                    print(1)
                    record()
            pygame.draw.rect(screen, (r1, g1, b1), button_1)
            pygame.draw.rect(screen, (r2, g2, b2), button_2)
            screen.blit(start1, (50, 100))
            screen.blit(record1, (50, 200))
            screen.blit(click1, (250, 100))
            screen.blit(s, (330, 100))
            screen.blit(stop, (400, 100))
            screen.blit(click1, (250, 200))
            screen.blit(s, (330, 200))
            screen.blit(start2, (400, 200))
            password = open('password.txt', 'r+')
            password = password.readline()
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                # if user types QUIT then the screen will close
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:

                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]

                    # Unicode standard is used for string
                    # formation
                    else:
                        user_text += event.unicode

                    if user_text == '/log' and a == 0:
                        a = 1
                        print(a)
                    if a == 1:
                        if event.key == pygame.K_RETURN:
                            log()
                            a = 0
                            user_text = ''
                    if user_text == '/start' and b == 0:
                        if event.key == pygame.K_RETURN:
                            start()
                            b += 1
                            user_text = ''
                    elif user_text != '/start':
                        b = 0
                    if event.key == pygame.K_RETURN:
                        user_text = ''
                    if user_text == password:

                        settings = 'Do want to change your password'
                    else:
                        settings = 'settings'
            # it will set background color of screen

            if active:
                color = color_active
            else:
                color = color_passive

            # draw rectangle and argument passed which should
            # be on screen
            text = pygame.draw.rect(screen, color, input_rect)

            text_surface = base_font.render(user_text, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(100, text_surface.get_width() + 10)


            pygame.display.update()
            mainClock.tick(60)

    def start():
        speed = 100
        fps = [time.sleep(1. / speed)]
        mouse = Controller()
        mousePos = mouse.position
        mousePos1 = mouse.position
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()

            "opens file"
            file1 = open("mouse.txt")
            file2 = open("mouseclickR.txt")
            "two sets of data are being used in points"
            "mouse positions x and y"
            points = set()
            points1 = set()
            with open("mouse.txt", "r") as f:
                # each line separately
                for idx, line in enumerate(f):
                    # strip \n  & strip ( and ) & split at ,
                    pointstring = line.strip().strip("()").split(",")
                    # guard against empty/non well formed lines
                    if pointstring and len(pointstring) == 2:
                        if mousePos == points and keys[pygame.K_s]:
                            x, y = line.strip().strip("()").split(",")
                            mouse.position = x, y  # = or (x, y)[0], (x, y)[1] same as -----> = x,y
                            time.sleep(1. / speed)
                            if keys[pygame.K_s]:
                                run = False

                    else:
                        "if for some reason is doesn't work, it'll look for whats wrong in the txt file"
                        print(f"Error in line {idx}: '{line}'")

            "starts using the points in the txt File"

            mousePos = points

    def record():
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
            run = True
            open("mouse.txt", "w+")
            os.remove("mouse.txt")
            open("mouse.txt", "w+")
            open("mouseclickR.txt", "w+")
            os.remove("mouseclickR.txt")
            open("mouseclickR.txt", "w+")
            open("mouseclickL.txt", "w+")
            os.remove("mouseclickL.txt")
            open("mouseclickL.txt", "w+")
            run2 = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                run = False
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

    def log():
        import os, sys
        import subprocess

        run = False
        if not run:
            run2 = True
        run2 = True

        # run2 deletes previous files
        while run2:
            open("app", "w+")
            os.remove("app.txt")
            open("app.txt", "w+")
            run = True
            run2 = False
        while run:
            cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            for line in proc.stdout:
                if line.rstrip():
                    # only print lines that are not empty
                    # decode() is necessary to get rid of the binary string (b')
                    # rstrip() to remove `\r\n`
                    print(line.decode().rstrip())
                    file1 = open("app.txt", "a+")
                    file1.writelines(str(line.decode().rstrip()) + "\n")
                    run = False

    main_menu()


loggin()
