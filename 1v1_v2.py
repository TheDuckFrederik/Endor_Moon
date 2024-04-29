import time
from pygame.locals import *
import pygame
#
WIDTH, HEIGHT = 320, 200
BACKGROUND_IMAGE = 'assets/Background.png'
BGM = 'assets/7.mp3'
WHITE = (255,255,255)
player1_lives = 3
player2_lives = 3
#
player_image1 = pygame.image.load('assets/TIE.png')
player_rect1 = player_image1.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
ship_speed = 1
#
player_image2 = pygame.image.load('assets/X_Wing.png')
player_rect2 = player_image2.get_rect(midbottom=(WIDTH // 2, HEIGHT - 150))
ship_speed = 1
#
bullet_img = pygame.Surface((4,10))
bullet_img.fill(WHITE)
player1_bullets = []
player2_bullets = []
bullet_speed = 3
bullet_cooldown = 1000 ###
temps_ultima_bala_jugador1 = 0
temps_ultima_bala_jugador2 = 0
#
pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1 v 1")
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))
#
while True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                bales_jugador1.append(pygame.Rect(player_rect1.centerx - 2, player_rect1.top, 4, 10))
                temps_ultima_bala_jugador1 = current_time
            if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                temps_ultima_bala_jugador2 = current_time
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player_rect1.x -= ship_speed
    if keys[K_d]:
        player_rect1.x += ship_speed
    if keys[K_LEFT]:
        player_rect2.x -= ship_speed
    if keys[K_RIGHT]:
        player_rect2.x += ship_speed
    player_rect1.clamp_ip(pantalla.get_rect())
    player_rect2.clamp_ip(pantalla.get_rect())
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    for bala in bales_jugador1:
        bala.y -= velocitat_bales
        if bala.bottom < 0 or bala.top > HEIGHT:
            bales_jugador1.remove(bala) # si ha sortit elimina la bala
        else:
            pantalla.blit(bullet_img, bala)
        if player_rect2.colliderect(bala):
            print("BOOM 1!")
            bales_jugador1.remove(bala)  # eliminem la bala

    for bala in bales_jugador2:
        bala.y += velocitat_bales
        if bala.bottom < 0 or bala.top > HEIGHT:
            bales_jugador2.remove(bala)
        else:
            pantalla.blit(bullet_img, bala)
        if player_rect1.colliderect(bala):
            print("BOOM 2!")
            bales_jugador2.remove(bala)

    #dibuixar els jugadors:
    pantalla.blit(player_image1, player_rect1)
    pantalla.blit(player_image2, player_rect2)

    pygame.display.update()
    clock.tick(fps)
