# import sys module
import subprocess
import sys
import os
import pygame
import win32api
from pynput.mouse import Controller
from pygame.locals import *
import time
import clipboard
# pygame.init() will initialize all
# imported module


pygame.init()

clock = pygame.time.Clock()
click = False


# it will display on screen
def main():
    f = 0
    g = 0
    global click
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
    font2 = pygame.font.SysFont('comicsans', 15)

    class drop_menu:
        def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    text1 = "/log"
    text2 = "/reset password"
    while True:
        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()
        r1 = 10
        g1 = 10
        b1 = 10
        r2 = 10
        g2 = 10
        b2 = 10
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        log = pygame.Rect(350, 230, 100, 23)
        reset = pygame.Rect(350, 257, 100, 23)
        if button_1.collidepoint((mx, my)):
            r1 = 50
            if click:
                print(1)
        if button_2.collidepoint((mx, my)):
            r2 = 50
            if click:
                print(1)
        if log.collidepoint((mx, my)):
            if click and user_text == '/':
                user_text = text1
        if reset.collidepoint((mx, my)):
            if click and user_text == '/':
                user_text = text2
        pygame.draw.rect(screen, (r1, g1, b1), button_1)
        pygame.draw.rect(screen, (r2, g2, b2), button_2)
        click = False
        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
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

                if event.key == (pygame.K_LCTRL and pygame.K_v):
                    text = clipboard.paste()  # text will have the content of clipboard
                    user_text = text
                if event.key == (pygame.K_LCTRL and pygame.K_c):
                    clipboard.copy(user_text)  # text will have the content of clipboard
            if keys[pygame.K_DOWN] and user_text == '/':
                user_text = text1
            a = 0
            if user_text == password and a == 0:
                a = 1
            if a == 1:
                if event.type == keys[pygame.K_RETURN]:
                    subprocess.call("menu.py 2", shell=True)
                    sys.exit()
            else:
                a = 0

        s = user_text
        len(s)
        for i in range(len(s)):
            if (s == '/') and i in range(len(s)) == range(1):
                f += 1
                if f > 20:
                    pygame.draw.rect(screen, (100, 100, 100), (350, 237, 5, 5), 11, 1)
                    draw_text('/log', font2, (0, 0, 0), screen, 355, 230)
                    if g > 10:
                        pygame.draw.rect(screen, (100, 100, 100), (350, 262, 5, 5), 11, 1)
                        draw_text('/reset password', font2, (0, 0, 0), screen, 355, 253)
        if f > 20 and user_text != '/':
            f = 0
        if f > 20:
            g += 1
        if g > 20 and user_text != '/':
            g = 0
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
        draw_text('Enter Password', font, (0, 0, 0), screen, 100, 200)


        pygame.display.flip()
        pygame.display.update()
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


main()
