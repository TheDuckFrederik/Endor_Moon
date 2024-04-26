#
import time
from pygame.locals import *
import pygame
import random
from versus import versus
import sys
#
HEIGHT, WIDTH = 320, 200
BACKROUND_IMAGE = 'assets/Background.png'
#
msg = 'Endor Moon'
pygame.init()
#screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.FULLSCREEN)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Endor Moon")
#
def print_screen_backround(image):
    backround = pygame.image.load(image).convert()
    screen.blit(backround, (0, 0))
#
def start_animation():
    print_screen_backround(BACKROUND_IMAGE)
    pygame.display.update()
    #
    font = pygame.font.SysFont(None, 52)
    #
    for i in range(120):
        time.sleep(0.01)
        #
        print_screen_backround(BACKROUND_IMAGE)
        img = font.render(msg, True, (i + 50, i + i, i))
        screen.blit(img, (20, 200 - i))
        #
        pygame.display.update()
    #
    time.sleep(3)
#
def credit_animation():
    print_screen_backround(BACKROUND_IMAGE)
    pygame.display.update()
    #
    font = pygame.font.SysFont(None, 52)
    #
    for i in range(120):
        time.sleep(0.01)
        #
        print_screen_backround(BACKROUND_IMAGE)
        img = font.render(msg, True, (i + 50, i + i, i))
        screen.blit(img, (20, 200 - i))
        #
        pygame.display.update()
#
def print_menu():
    print_screen_backround(BACKROUND_IMAGE)
    #
    transparent_area = pygame.Surface((240, 120), pygame.SRCALPHA)
    pygame.draw.rect(transparent_area, (0, 0, 0, 100), (0, 0, 240, 120))
    #
    screen.blit(transparent_area, (40, 40))
    #
    font = pygame.font.SysFont(None, 36)
    img1 = font.render("1 - Play", True, (255, 255, 255))
    img2 = font.render("2 - Credits", True, (255, 255, 255))
    img3 = font.render("3 - Exit", True, (255, 255, 255))
    #
    screen.blit(img1, (70, 50))
    screen.blit(img2, (70, 90))
    screen.blit(img3, (70, 130))
    #
    pygame.display.update()
#
def backround_music(music):
    ambient_music = pygame.mixer.Sound(music)
    music_chanel = pygame.mixer.Channel(0)
    ambient_music.play()
#
# backround_music(BGM)
start_animation()
print_menu()
#
while True:
    pygame.display.update()
    #
    keys = pygame.key.get_pressed()
    #
    if keys[K_1]:
        versus()
    if keys[K_2]:
        msg = "Joc per:"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "Unai O. Pujol"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "Musica per:"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "RATM"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "Megadeth"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "ZZ Top"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "Metallica"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "Skindred"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        msg = "B.I.G"
        credit_animation()
        #
        time.sleep(0.5)
        pygame.display.update()
        #
        pygame.time.delay(2000) # wait for 2 seconds before quitting
        pygame.quit()
        sys.exit()
    #
    if keys[K_3]:
        pygame.display.update()
        pygame.time.delay(2000) # wait for 2 seconds before quitting
        pygame.quit()
        sys.exit()
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#
