import pygame
import os
import sys
import random
from pygame.locals import *

# initialize pygame
pygame.init()

# sound
pygame.mixer.init()
# instance
shootSound = pygame.mixer.Sound('shoot.wav')
blastSound = pygame.mixer.Sound('blast.wav')

# create an instance of Clock()
'''
    This method should be called once per frame.
    It will compute how many milliseconds have passed since the previous call.
    It helps to control the speed of the alien
'''
frames_per_seconds = pygame.time.Clock()

pygame.display.set_caption("Killing Aliens")

# use set_mode() to create pixel surface to draw
# use surfaces to draw images onto the screen
size = width, height = 1000, 600
surface = pygame.display.set_mode(size)

# define color
# background = pygame.Color(100, 149, 237)
white = [255, 255, 255]
shoot_color = (255, 0, 0)
background = pygame.Color(white)

# load image alien & resize img allien
img_alien = pygame.image.load('alien.jpeg')
img_alien = pygame.transform.scale(img_alien, (50, 60))
img_alien_rect = img_alien.get_rect()

# load image gun
img_gun = pygame.image.load('gun.jpeg')
img_gun = pygame.transform.scale(img_gun, (110, 70))
img_gun = pygame.transform.rotate(img_gun, 90)
img_gun_rect = img_gun.get_rect()

# text
score = 0
ping_text = "Score: " + str(score)
font = pygame.font.SysFont(None, 25)
txt_score = font.render(ping_text, True, (0, 0, 0))


def shoot(pos_alien, pos_gun):
    print(pos_alien, " - ", pos_gun)
    if pos_alien == pos_gun or pos_alien + 1 == pos_gun or pos_alien - 1 == pos_gun:
        blastSound.play()
        print("you get it!")
        score += 1


x = 0
pos = 2
while True:
    # fill the color on the surface
    surface.fill(background)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x >= width - 60:
                    x = width - 60
                else:
                    x = x + pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x < 0:
                    x = 0
                else:
                    x = x - pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # play the sound
                shootSound.play()
                shoot(img_alien_rect.x, x)
                # line(surface, color, start_pos, end_pos, width=1) -> Rect
                pygame.draw.line(surface, shoot_color,
                                 (x, 450), (x, 470), width=4)

    # show text
    txt_score = font.render(ping_text, True, (0, 0, 0))
    surface.blit(txt_score, (width - 200, height/2))

    # show img  & set position of the gun. first time and move img gun
    surface.blit(img_gun, (x, height - 120))

    # move img alien
    img_alien_rect = img_alien_rect.move(1, 0)
    # blit() draw one image onto another position
    surface.blit(img_alien, img_alien_rect)

    # checking img inside the screen
    if img_alien_rect.left < 0 or img_alien_rect.right > width:
        img_alien_rect.x = 0
        img_alien_rect.y = 0

    # pygame.display.flip() => Update the full display Surface to the screen
    pygame.display.flip()
    frames_per_seconds.tick(30)
