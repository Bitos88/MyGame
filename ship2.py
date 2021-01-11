import pygame
import random
from pygame.sprite import Sprite


class Ship2(Sprite):
    def __init__(self, aiSettings, screen):
        super(Ship2, self).__init__()

        self.screen = screen
        self.aiSettings = aiSettings

        self.image = pygame.image.load("images/navep1.png")
        self.sprite = ("images/navep1.png","images/navep2.png","images/navep3.png","images/navep4.png","images/navep5.png")
        #self.imagen_redimensionada = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.transColor = (0,0,0)
        self.image.set_colorkey(self.transColor)

        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        
        self.centery = float(self.rect.centery)
        self.center = float(self.rect.centerx)

        self.movRight = False
        self.movLeft = False
        self.movUp = False
        self.movDown = False

    def update(self):
        if self.movRight and self.rect.right < self.screen_rect.right:
            self.center += self.aiSettings.shipSpeed
        elif self.movLeft and self.rect.left > 0:
            self.center -= self.aiSettings.shipSpeed

        elif self.movUp and self.rect.top > 0:
            self.centery -= self.aiSettings.shipSpeed
        elif self.movDown and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.aiSettings.shipSpeed


        self.rect.centerx = self.center
        self.rect.centery = self.centery


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def animation(self):
        for x in self.sprite:
            self.image = pygame.image.load(x)