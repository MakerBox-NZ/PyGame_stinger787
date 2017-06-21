#!/usr/bin/env python3
#by stinger787
#thanks to Seth Kenlon, Jess Weichler

import pygame #load pygame keywords
import sys #let python your file systems
import os #help python identify your os

'''OBJECTS'''
# put classes & functions here
class player(pygame.sprite.Sprite):
    #spawn a player
    def _init_
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0 #move along X
        self.momentumY = 0 #move along Y
                                                                                                                                                                                                                            
        self.image = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.image.convert_alpha() #optimise for alpha
        self.image.set_colorkey(alpha) #set alpha
        

        self.rect = self.image.get_rect()
        
    def control(self, x, y):
        #control player movement
        self.momentumX += x
        self.momentumY += y

    def update(self):
        #update sprite position

        

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
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)



'''MAINLOOP'''
# code runs many times

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('g'):
                pygame.quit()
                sys.exit()
                main = False
            if event.key == pygame.K_LEFT:
                print('left stop')
            if event.key == pygame.K_RIGHT:
                print('right stop')
            if event.key == pygame.K_UP:
                print('up stop')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
            if event.key == pygame.K_RIGHT:
                print('right')
            if event.key == pygame.K_UP:
                print('up')

    screen.blit(backdrop, backdropRect)

    pygame.display.flip()
    clock.tick(fps)


