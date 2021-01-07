import pygame

class Ship():

    def __init__(self, aiSettings, screen):
        self.screen = screen
        self.aiSettings = aiSettings

        self.image = pygame.image.load("images/ship_ss.bmp")
        self.rect = self.image.get_rect()
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

