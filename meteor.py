import pygame
import random
from pygame.sprite import Sprite

class Meteor(Sprite):
    def __init__(self, aiSettings, screen):
        super(Meteor, self).__init__()
        Sprite.__init__(self)

        self.screen = screen
        self.aiSettings = aiSettings

        self.image = pygame.image.load("images/meteorito.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.aiSettings.screenW + self.rect.width
        self.rect.y = random.randint(self.rect.height * 2, 800 - self.rect.height)

        self.x = float(self.rect.x)

    def update(self):
        self.rect.x -= self.aiSettings.meteorSpeed

    def blitme(self):
        self.screen.blit(self.image, self.rect)