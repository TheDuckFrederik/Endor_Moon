import time
from pygame.locals import *
import pygame
import random

def versus():
    song = random.randint(1, 33)
    print(song)
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

    WIDTH, HEIGHT = 320, 200
    BACKROUND_IMAGE = 'assets/Background.png'
    WHITE = (255, 255, 255)
    player1_lives = 3
    player2_lives = 3
    player1_no_lives = 0
    player2_no_lives = 0

    explosion = pygame.image.load('assets/explosion.png')
    explosion1_rect = explosion.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
    explosion2_rect = explosion.get_rect(midbottom=(WIDTH // 2, HEIGHT - 150))

    p1ds = ('assets/Player_1_Death_Screen.png')
    p2ds = ('assets/Player_2_Death_Screen.png')

    bullet_img = pygame.Surface((4, 10))
    bullet_img.fill(WHITE)

    player1_bullets = []
    player2_bullets = []

    bullet_speed = 3
    bullet_cooldown = 1000
    time_from_last_bullet_player1 = 0
    time_from_last_bullet_player2 = 0

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("1v1")

    ambient_music = pygame.mixer.Sound(BGM)
    music_chanel = pygame.mixer.Channel(0)
    ambient_music.play()

    clock = pygame.time.Clock()
    fps = 30

    def print_screen_backround(image):
        backround = pygame.image.load(image).convert()
        screen.blit(backround, (0, 0))

    player_image1 = pygame.image.load('assets/TIE.png')
    player_rect1 = player_image1.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
    ship_speed1 = 1.6

    player_image2 = pygame.image.load('assets/X_Wing.png')
    player_rect2 = player_image2.get_rect(midbottom=(WIDTH // 2, HEIGHT - 150))
    ship_speed2 = 1.6

    player1_lives_image = pygame.image.load('assets/player2_full_heart.png')
    player1_lives_rect1 = player1_lives_image.get_rect(midbottom = ((17), 35))
    player1_lives_rect2 = player1_lives_image.get_rect(midbottom = ((17) + (32), 35))
    player1_lives_rect3 = player1_lives_image.get_rect(midbottom = ((17) + (32 * 2), 35))
    player1_no_lives_image = pygame.image.load('assets/player2_broken_heart.png')

    player2_lives_image = pygame.image.load('assets/player2_full_heart.png')
    player2_lives_rect1 = player2_lives_image.get_rect(midbottom = ((17) + (WIDTH - 32 * 2), 35))
    player2_lives_rect2 = player2_lives_image.get_rect(midbottom = ((17) + (WIDTH - 32 * 2), 35))
    player2_lives_rect3 = player2_lives_image.get_rect(midbottom = ((17) + (WIDTH - 32 * 3), 35))
    player2_no_lives_image = pygame.image.load('assets/player2_broken_heart.png')

    game_over = False

    while not game_over:
        clock.tick(fps)
        time_from_last_bullet_player1 += 1
        time_from_last_bullet_player2 += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                elif event.key == pygame.K_LEFT:
                    player1_move = -ship_speed1
                elif event.key == pygame.K_RIGHT:
                    player1_move = ship_speed1
                elif event.key == pygame.K_a:
                    player2_move = -ship_speed2
                elif event.key == pygame.K_d:
                    player2_move = ship_speed2
                elif event.key == pygame.K_SPACE:
                    if time_from_last_bullet_player1 >= bullet_cooldown:
                        bullet_player1 = [bullet_img.copy(), player_rect1.midtop]
                        player1_bullets.append(bullet_player1)
                        time_from_last_bullet_player1 = 0
                    if time_from_last_bullet_player2 >= bullet_cooldown:
                        bullet_player2 = [bullet_img.copy(), player_rect2.midtop]
                        player2_bullets.append(bullet_player2)
                        time_from_last_bullet_player2 = 0

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player1_move = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player2_move = 0

        player_rect1.move_ip(player1_move, 0)
        player_rect2.move_ip(player2_move, 0)

        if player_rect1.left < 0:
            player_rect1.left = 0
        if player_rect1.right > WIDTH:
            player_rect1.right = WIDTH
        if player_rect2.left < 0:
            player_rect2.left = 0
        if player_rect2.right > WIDTH:
            player_rect2.right = WIDTH

        player1_bullets = [bullet[0].move(0, -bullet_speed) or bullet[1].move_ip(0, -bullet_speed) for bullet in player1_bullets if 0 <= bullet[1].top <= HEIGHT]
        player2_bullets = [bullet[0].move(0, -bullet_speed) or bullet[1].move_ip(0, -bullet_speed) for bullet in player2_bullets if 0 <= bullet[1].top <= HEIGHT]

        if pygame.sprite.spritecollideany(player1_bullets, player2_bullets):
            explosion1 = explosion.subsurface(pygame.Rect(0, 0, 64, 64))
            screen.blit(explosion1, explosion1_rect)
            player1_lives -= 1
            player1_bullets = []
            player2_bullets = []

        if pygame.sprite.spritecollideany(player2_bullets, player1_bullets):
            explosion2 = explosion.subsurface(pygame.Rect(0, 0, 64, 64))
            screen.blit(explosion2, explosion2_rect)
            player2_lives -= 1
            player1_bullets = []
            player2_bullets = []

        if player1_lives == 0:
            screen.blit(player1_death_screen, (0, 0))
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        elif player2_lives == 0:
            screen.blit(player2_death_screen, (0, 0))
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        print_screen_backround(BACKROUND_IMAGE)
        screen.blit(player_image1, player_rect1)
        screen.blit(player_image2, player_rect2)

        for bullet in player1_bullets:
            screen.blit(bullet[0], bullet[1])

        for bullet in player2_bullets:
            screen.blit(bullet[0], bullet[1])

        pygame.display.flip()


versus()
