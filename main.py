import pygame
import sys, os
from config import Config
from ship import Ship
import gameFunctions as gf
from pygame.sprite import Group
from meteor import Meteor


def runGame(): #funcion que iniciara el juego 
    pygame.init()
    aiSettings = Config()
    screen = pygame.display.set_mode((aiSettings.screenW, aiSettings.screenH)) #instanciamos el objeto para definir las dimensiones de la ventana
    imagen_defondo = pygame.image.load("images/space.jpg").convert()
    screen.blit(imagen_defondo, [0, 0])
    pygame.display.set_caption("ALIEN INVASION") #Titulo de nuestra ventana

    bgCOLOR = (230, 230, 230)

    ship = Ship(aiSettings, screen)
    meteor = Meteor(aiSettings, screen)
    meteors = Group()
    bullets = Group()

    x = 1

    while True:
        if x %200 == 0:
            print(x)
        gf.check_events(ship, aiSettings, screen, bullets)
        ship.update()
        bullets.update()
        meteor.update()
        gf.updateScreen(aiSettings, screen, ship, meteor, bullets)
        
        x +=1 

        for bullet in bullets.copy():
            if bullet.rect.left >= 1200:
                bullets.remove(bullet)


runGame()