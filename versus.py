#
import time
from pygame.locals import *
import pygame
import random
import sys
#
def versus():
    #
    song = random.randint(1, 33)
    print(song)
    #
    if song == 1 or song == 9 or song == 17 or song == 25:
        BGM = 'assets/rotation/holy_wars.mp3'
    elif song == 2 or song == 10 or song == 18 or song == 26:
        BGM = 'assets/rotation/master_of_puppets.mp3'
    elif song == 3 or song == 11 or song == 19 or song == 27:
        BGM = 'assets/rotation/people_of_the_sun.mp3'
    elif song == 4 or song == 12 or song == 20 or song == 28:
        BGM = 'assets/rotation/killing_in_the_name.mp3'
    elif song == 5 or song == 13 or song == 21 or song == 29:
        BGM = 'assets/rotation/nobody.mp3'
    elif song == 6 or song == 14 or song == 22 or song == 30:
        BGM = 'assets/rotation/symphony_of_destruction.mp3'
    elif song == 7 or song == 15 or song == 23 or song == 31:
        BGM = 'assets/rotation/la_grange.mp3'
    elif song == 8 or song == 16 or song == 24 or song == 32:
        BGM = 'assets/rotation/too_far_gone.mp3'
    elif song == 33:
        BGM = 'assets/rotation/hypnotize.mp3'
    #
    WIDTH, HEIGHT = 320, 200
    BACKROUND_IMAGE = 'assets/Background.png'
    WHITE = (255, 255, 255)
    player1_lives = 3
    player2_lives = 3
    player1_no_lives = 0
    player2_no_lives = 0
    #
    hit1 = False
    hit2 = False
    #
    explosion = pygame.image.load('assets/explosion.png')

    #
    player_image1 = pygame.image.load('assets/TIE.png')
    player_image1_dark = pygame.image.load('assets/TIE_Shadow.png')
    player_rect1 = player_image1.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
    ship_speed1 = 1.7
    #
    player_image2 = pygame.image.load('assets/X_Wing.png')
    player_image2_dark = pygame.image.load('assets/X_Wing_Shadow.png')
    player_rect2 = player_image2.get_rect(midbottom=(WIDTH // 2, HEIGHT - 150))
    ship_speed2 = 1.7
    #
    player1_lives_image = pygame.image.load('assets/player1_live.png')
    player1_lives_rect1 = player1_lives_image.get_rect(midbottom = ((17), 35))
    player1_lives_rect2 = player1_lives_image.get_rect(midbottom = ((17) + (11), 35))
    player1_lives_rect3 = player1_lives_image.get_rect(midbottom = ((17) + (11 * 2), 35))
    player1_no_lives_image = pygame.image.load('assets/player1_no_live.png')
    #
    player2_lives_image = pygame.image.load('assets/player2_live.png')
    player2_lives_rect1 = player2_lives_image.get_rect(midbottom = ((WIDTH - 17), 35))
    player2_lives_rect2 = player2_lives_image.get_rect(midbottom = ((WIDTH - 17) - (11), 35))
    player2_lives_rect3 = player2_lives_image.get_rect(midbottom = ((WIDTH - 17) - (11 * 2), 35))
    player2_no_lives_image = pygame.image.load('assets/player2_no_live.png')
    #
    bullet_img = pygame.Surface((4, 10))
    bullet_img.fill(WHITE)
    #
    player1_bullets = []
    player2_bullets = []
    #
    bullet_speed = 3
    bullet_cooldown = 1000
    time_from_last_bullet_player1 = 0
    time_from_last_bullet_player2 = 0
    #
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("1v1")
    #
    p1ds = ('assets/Player_1_Death_Screen.png')
    player1_death_screen = pygame.image.load(p1ds).convert()
    p2ds = ('assets/Player_2_Death_Screen.png')
    player2_death_screen = pygame.image.load(p2ds).convert()
    #
    ambient_music = pygame.mixer.Sound(BGM)
    music_chanel = pygame.mixer.Channel(0)
    ambient_music.play()
    #
    clock = pygame.time.Clock()
    fps = 30
    #
    def print_screen_backround(image):
        backround = pygame.image.load(image).convert()
        screen.blit(backround, (0, 0))
    #
    while True:
        #
        screen.blit(player_image1, player_rect1)
        screen.blit(player_image2, player_rect2)
        #
        current_time = pygame.time.get_ticks()
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #
            if event.type == KEYDOWN:
                #
                if event.key == K_w and current_time - time_from_last_bullet_player1 >= bullet_cooldown:
                    player1_bullets.append(pygame.Rect(player_rect1.centerx - 2, player_rect1.top, 4, 10))
                    time_from_last_bullet_player1 = current_time
                #
                if event.key == K_UP and current_time - time_from_last_bullet_player2 >= bullet_cooldown:
                    player2_bullets.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom - 10, 4, 10))
                    time_from_last_bullet_player2 = current_time
    #

        def backround_music(music):
            ambient_music = pygame.mixer.Sound(music)
            music_chanel = pygame.mixer.Channel(0)
            ambient_music.play()
        #
        keys = pygame.key.get_pressed()
        #
        if keys[K_a]:
            player_rect1.x -= ship_speed1
        if keys[K_d]:
            player_rect1.x += ship_speed1
        #
        if keys[K_LEFT]:
            player_rect2.x -= ship_speed2
        if keys[K_RIGHT]:
            player_rect2.x += ship_speed2
        #
        player_rect1.clamp_ip(screen.get_rect())
        player_rect2.clamp_ip(screen.get_rect())
        #
        print_screen_backround(BACKROUND_IMAGE)
        #
        for bullet in player1_bullets:
            bullet.y -= bullet_speed
            if bullet.bottom < 0 or bullet.top > HEIGHT:
                player1_bullets.remove(bullet)
            #
            else:
                screen.blit(bullet_img, bullet)
            #
            if player_rect2.colliderect(bullet):
                print('Player 2 was HIT!')
                player2_lives -= 1
                player2_no_lives += 1
                player1_bullets.remove(bullet)
                hit2 = True
            else:
                hit2 = False
        #
        for bullet in player2_bullets:
            bullet.y += bullet_speed
            if bullet.bottom < 0 or bullet.top > HEIGHT:
                player2_bullets.remove(bullet)
                screen.blit(bullet_img, bullet)
            #
            else:
                screen.blit(bullet_img, bullet)
            #
            if player_rect1.colliderect(bullet):
                print('Player 1 was HIT!')
                player1_lives -= 1
                player1_no_lives += 1
                player2_bullets.remove(bullet)
                hit1 = True
            else:
                hit1 = False
            #
        if hit1 == True:
            # screen.blit(player_image1_dark, player_rect1)
            # pygame.time.delay(300)
            screen.blit(explosion, player_rect1)
            pygame.time.delay(300)
            screen.blit(player_image1, player_rect1)
        elif hit1 == False:
            screen.blit(player_image1, player_rect1)
        #
        if hit2 == True:
            # screen.blit(player_image2_dark, player_rect2)
            # pygame.time.delay(300)
            screen.blit(explosion, player_rect2)
            pygame.time.delay(300)
            screen.blit(player_image2, player_rect2)
        elif hit2 == False:
            screen.blit(player_image2, player_rect2)
        #
        if player2_lives == 3:
            screen.blit(player2_lives_image, player2_lives_rect1)
            screen.blit(player2_lives_image, player2_lives_rect2)
            screen.blit(player2_lives_image, player2_lives_rect3)
        elif player2_lives == 2:
            screen.blit(player2_lives_image, player2_lives_rect1)
            screen.blit(player2_lives_image, player2_lives_rect2)
            screen.blit(player2_no_lives_image, player2_lives_rect3)
        elif player2_lives == 1:
            screen.blit(player2_lives_image, player2_lives_rect1)
            screen.blit(player2_no_lives_image, player2_lives_rect2)
            screen.blit(player2_no_lives_image, player2_lives_rect3)
        elif player2_lives == 0:
            screen.blit(player2_no_lives_image, player2_lives_rect1)
            screen.blit(player2_no_lives_image, player2_lives_rect2)
            screen.blit(player2_no_lives_image, player2_lives_rect3)
            time.sleep(1)
            screen.blit(player2_death_screen, (0,0))
            pygame.display.update()
            pygame.time.delay(2000) # wait for 2 seconds before quitting
            pygame.quit()
            sys.exit()
        #
        if player1_lives == 3:
            screen.blit(player1_lives_image, player1_lives_rect1)
            screen.blit(player1_lives_image, player1_lives_rect2)
            screen.blit(player1_lives_image, player1_lives_rect3)
        elif player1_lives == 2:
            screen.blit(player1_lives_image, player1_lives_rect1)
            screen.blit(player1_lives_image, player1_lives_rect2)
            screen.blit(player1_no_lives_image, player1_lives_rect3)
        elif player1_lives == 1:
            screen.blit(player1_lives_image, player1_lives_rect1)
            screen.blit(player1_no_lives_image, player1_lives_rect2)
            screen.blit(player1_no_lives_image, player1_lives_rect3)
        elif player1_lives == 0:
            screen.blit(player1_no_lives_image, player1_lives_rect1)
            screen.blit(player1_no_lives_image, player1_lives_rect2)
            screen.blit(player1_no_lives_image, player1_lives_rect3)
            time.sleep(1)
            screen.blit(player1_death_screen, (0,0))
            pygame.display.update()
            pygame.time.delay(2000) # wait for 2 seconds before quitting
            pygame.quit()
            sys.exit()
        #
        pygame.display.update()
        clock.tick(fps)
#
