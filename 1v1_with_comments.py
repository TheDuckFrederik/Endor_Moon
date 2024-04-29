#
import time
from pygame.locals import KEYDOWN
import pygame
#
HEIGHT, WIDTH = 320, 200
BACKROUND_IMAGE = 'assets/Background.png'
BGM = 'assets/7.mp3'
WHITE = (255, 255, 255)
player1_lives = 3
player2_lives = 3
# Player 1
player_image1 = pygame.image.load('assets/TIE.png')
player_rect1 = player_image1.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
ship_speed1 = 1
# Player 2
player_image2 = pygame.image.load('assets/X_Wing.png')
player_rect2 = player_image2.get_rect(midbottom=(WIDTH // 2, HEIGHT - 150))
ship_speed2 = 1
# Bullets (white rectangle)
bullet_img = pygame.Surface((4, 10)) # bullet area = 4px x 10px
bullet_img.fill(WHITE) # Area painted white
#
player1_bullets = [] # List for player 1's bullets
player2_bullets = [] # List for player 2's bullets
#
bullet_speed = 3
bullet_cooldown = 1000 # 1 second
time_from_last_bullet_player1 = 0 # To count time in between Player 1's bullets
time_from_last_bullet_player2 = 0 # To count time in between Player 2's bullets
#
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("1v1")
# FPS control
clock = pygame.time.Clock()
fps = 30
#
def print_screen_backround(image):
    backround = pygame.image.load(image).convert()
    screen.blit(backround, (0, 0))
#
while True:
    current_time = pygame.time.get_ticks() # Count
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # Control bullets
        if event.type == KEYDOWN:
            # Player 1
            if event.key == K_w and current_time - time_from_last_bullet_player1 >= bullet_cooldown:
                player1_bullets.append(pygame.Rect(player_rect1.centerx - 2, player_rect1.top, 4, 10))
                time_from_last_bullet_player1 = current_time
            # Player 2
            if event.key == K_UP and current_time - time_from_last_bullet_player2 >= bullet_cooldown:
                player2_bullets.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom - 10, 4, 10))
                time_from_last_bullet_player2 = current_time

# Moviment
keys = pygame.key.get_pressed()
# Player 1
if keys[K_a]:
    player_rect1.x -= ship_speed1
if keys[K_d]:
    player_rect1.x += ship_speed1
# Player 2
if keys[K_LEFT]:
    player_rect2.x -= ship_speed2
if keys[K_RIGHT]:
    player_rect2.x += ship_speed2
# Keep player in screen
player_rect1.clamp_ip(screen.get_rect()) # 1
player_rect2.clamp_ip(screen.get_rect()) # 2
# Print backround
print_screen_backround(BACKROUND_IMAGE)
# Update & print Player 1's bullets
for bullet in player1_bullets: # Recursive loop for all the Player 1's bullets
    bullet.y -= bullet_speed # Move bullet
    if bullet.bottom < 0 or bullet.top > HEIGHT: # Cheks if the bullet is the screen
        player1_bullets.remove(bullet) # If it's out it erases it
    else:
        screen.blit(bullet_img, bullet) # If it isn't out, it draws it
    # Collision detection
    if player_rect2.colliderect(bullet): # If a Player 1's bullet touches Player 2
        print('Player 2 was HIT!')
        player2_lives -= 1
        player1_bullets.remove(bullet)
# Update & print Player 2's bullets
for bullet in player2_bullets: # Recursive loop for all the Player 2's bullets
    bullet.y -= bullet_speed # Move bullet
    if bullet.bottom < 0 or bullet.top > HEIGHT: # Cheks if the bullet is the screen
        player2_bullets.remove(bullet) # If it's out it erases it
    else:
        screen.blit(bullet_img, bullet) # If it isn't out, it draws it
    # Collision detection
    if player_rect2.colliderect(bullet): # If a Player 2's bullet touches Player 1
        print('Player 1 was HIT!')
        player1_lives -= 1
        player1_bullets.remove(bullet)
# Print the ships
screen.blit(player_image1, player_rect1)
screen.blit(player_image2, player_rect2)
#
pygame.display.update()
clock.tick(fps)
#
