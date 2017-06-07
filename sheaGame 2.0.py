#!/usr/bin/env python3
#by stinger787
#thanks to Seth Kenlon, Jess Weichler

import pygame #load pygame keywords
import sys #let python your file systems
import os #help python identify your os

'''OBJECTS'''
# put classes & functions here



'''SETUP'''
#code runs once


screenX = 960 #width
screenY = 720 #height

alpha = (0, 0, 0)
black = (1, 1, 1)
white = (255, 255, 255)


fps = 40 #frame rate
afps = 4 #animation cycles
clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropRect = screen.get_rect()

player = player()
player.rect.x = 0
player.rect


'''MAINLOOP'''
# code runs many times

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('g'):
                pygame.quit()
                sys.exit()
                main = False

    screen.blit(backdrop, backdropRect)

    pygame.display.flip()
    clock.tick(fps)


