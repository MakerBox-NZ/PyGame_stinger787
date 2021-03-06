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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0 #move along X
        self.momentumY = 0 #move along Y

        #gravity variables
        self.collide_delta = 0
        self.jump_delta = 6
        
        self.score = 0#set score
                                                                                                                                                                                                                            
        self.image = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.image.convert_alpha() #optimise for alpha
        self.image.set_colorkey(alpha) #set alpha
        

        self.rect = self.image.get_rect()
        
    def control(self, x, y):
        #control player movement
        self.momentumX += x
        self.momentumY += y

    def update(self, enemy_list, platform_list):
        #update sprite position
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX

        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY

        #gravity
        if self.collide_delta < 6 and self.jump_delta < 6:
            self.jump_delta = 6*2
            self.momentumY -=33 #how high to jump

            self.collide_delta +=6
            self.jump_delta  +=6

        #collisions
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in enemy_hit_list:
            self.score -= 1
            print(self.score)

        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        if self.momentumX > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.rect.x = currentX+9
                self.momentumY = 0
                self.collide_delta = 0 #stop jumping
                
        if self.momentumY > 0:
            for block in block_hit_list:
                self.rect.y = currentY
                self.momentumY = 0
                self.collide_delta = 0 #stop jumping


    def gravity(self):
        self.momentumY += 3.2  #how fast player falls

        if self.rect.y > 960 and self .momentumY >= 0:
            self.momentumY = 0
            self.rect.y = screenY-20

        
        
class Enemy(pygame.sprite.Sprite):
    #spawn an enemy
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0 #counter variable
    
    def move(self):
        #enemy movement
        if self.counter >= 0 and self.counter <= 30:
            self.rect.x += 2
        elif self.counter>= 30 and self.counter <=60:
            self.rect.x -=2
        else:
            self.counter = 0
            print('reset')

        self.counter += 1

class platform(pygame.sprite.Sprite):
    #x location, y location, img width, img height, img file
    def __init__(self,xloc,yloc,imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([imgw, imgh])
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.blockpic = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

        #paint into blocks
        self.image.blit(self.blockpic,(0,0,),(0,0,imgw,imgh))

    def level1():
        #create level 1
        platform_list = pygame.sprite.Group()
        block = platform(0, 350, 970, 43,os.path.join('images','block0.png'))
        platform_list.add(block) #after each block

        return platform_list #at end of function level1
        
            
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
backdrop = pygame.image.load(os.path.join('images','backdrop.png')).convert()
backdropRect = screen.get_rect()

platform_list = platform.level1() #set stage to level 1

player = player()
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10 #how fast to move

#enemy code
enemy = Enemy(420,280, 'enemy.png') #spawn enemy    #X, Y, img
enemy_list = pygame.sprite.Group() #create enemy group
enemy_list.add(enemy) #add enemy to group


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
                player.control(movesteps, 0)
            if event.key == pygame.K_RIGHT:
                print('right stop')
                player.control(-movesteps, 0)
            if event.key == pygame.K_UP:
                player.control(0, movesteps)
                print('up stop')
            if event.key == pygame.K_DOWN:
                print('down stop')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
                player.control(-movesteps, 0)
            if event.key == pygame.K_RIGHT:
                print('right')
                player.control(movesteps, 0)
            if event.key == pygame.K_UP:
                print('up')
                player.control(0, -movesteps)
            if event.key == pygame.K_DOWN:
                print('down')
                player.control(0, movesteps)

    screen.blit(backdrop, backdropRect)

    platform_list.draw(screen) #draw platforms on screen
    #player.gravity() #check gravity
    player.update(enemy_list, platform_list) #update player postion
    movingsprites.draw(screen) #draw playe
    
    enemy_list.draw(screen) #refresh enemies
    enemy.move() #move enemy sprite
    pygame.display.flip()
    clock.tick(fps)


