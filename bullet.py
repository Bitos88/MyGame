import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, aiSettings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, aiSettings.bulletHeight, 
        aiSettings.bulletWidth)
        self.rect.midleft = ship.rect.midright

        self.rect.midleft = ship.rect.midright

        self.x = float(self.rect.x)

        self.color = aiSettings.bulletColor
        self.speedBullet = aiSettings.bulletSpeed


    def update(self):
        self.x += self.speedBullet
        self.rect.x = self.x

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)