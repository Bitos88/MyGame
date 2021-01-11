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
    rectangulo = imagen_defondo.get_rect()
    screen.blit(imagen_defondo, (0, 0))
    pygame.display.set_caption("ALIEN INVASION") #Titulo de nuestra ventana
    pygame.mixer.init()
    pygame.display.init()

    bgCOLOR = (230, 230, 230)

    ship = Ship(aiSettings, screen)
    meteor = Meteor(aiSettings, screen)
    bullets = Group()
    meteoritos = Group()

    tiempo = 1
    puntuacion = 0

    letra = pygame.font.SysFont("Arial", 18)

    while True:


        if tiempo == 1 or tiempo %100 == 0:
            meteor = Meteor(aiSettings, screen)
            meteoritos.add(meteor)
        
        gf.check_events(ship, aiSettings, screen, bullets)
        ship.update()
        bullets.update()
        meteoritos.update()
        gf.updateScreen(aiSettings, screen, ship, meteoritos, bullets)

        ship.animation()
        


        for bullet in bullets.copy():
            if bullet.rect.left >= 1200:
                bullets.remove(bullet)

        for x in meteoritos.copy():
            if x.rect.right <= 0:
                meteoritos.remove(x)

        if pygame.sprite.groupcollide(meteoritos, bullets, True, True):
            puntuacion +=1

            print(puntuacion)


        gf.updateScreen(aiSettings, screen, ship, meteoritos, bullets)
        screen.blit(imagen_defondo, (0,0))

        tiempo += 1


runGame()