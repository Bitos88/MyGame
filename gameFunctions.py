import sys
import pygame
from bullet import Bullet

def check_events(ship, aiSettings, screen, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keyDown_events(event, ship, aiSettings, screen, bullets)            
            elif event.type == pygame.KEYUP:
                check_keyUp_events(event, ship)
            

def check_keyDown_events(event, ship, aiSettings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.movRight = True
    elif event.key == pygame.K_LEFT:
        ship.movLeft = True
    elif event.key == pygame.K_UP:
        ship.movUp = True
    elif event.key == pygame.K_DOWN:
        ship.movDown = True
    elif event.key == pygame.K_SPACE:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)
        pygame.mixer.music.load("sounds/laser.mp3")
        pygame.mixer.music.play()
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyUp_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movRight = False
    elif event.key == pygame.K_LEFT:
        ship.movLeft = False
    elif event.key == pygame.K_UP:
        ship.movUp = False
    elif event.key == pygame.K_DOWN:
        ship.movDown = False



def updateScreen(aiSettings, screen, ship, meteors, bullets):
    #screen.fill(aiSettings.bgCOLOR)
    for bullet in bullets.sprites():
        bullet.drawBullet()

    for meteoritos in meteors.sprites():
        meteoritos.blitme()


    ship.blitme()
    pygame.display.flip()

