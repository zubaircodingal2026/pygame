import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Player settings
player_width = 60
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 7

# Bullet settings
bullet_width = 5
bullet_height = 15
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_active = False

# Enemy settings
enemy_width = 50
enemy_height = 30
enemy_speed = 4

enemy_x = 100
enemy_y = 50

enemy2_x = 220
enemy2_y = 100

enemy3_x = 340
enemy3_y = 50

enemy4_x = 460
enemy4_y = 100

enemy5_x = 580
enemy5_y = 50
# Score
score = 0

# Game loop
running = True

while running:

    clock.tick(60)

    screen.fill(BLACK)

    for event in pygame.event.get():

              if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                   player_x -= player_speed

                elif event.key == pygame.K_RIGHT:
                    player_x += player_speed

                elif event.key == pygame.K_SPACE and not bullet_active:
                    bullet_active = True
                    bullet_x = player_x + player_width // 2 - bullet_width // 2
                    bullet_y = player_y

    # Keep player inside the screen
    if player_x < 0:
        player_x = 0

    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    # Move enemies
    enemy_x += enemy_speed
    enemy2_x += enemy_speed
    enemy3_x += enemy_speed
    enemy4_x += enemy_speed
    enemy5_x += enemy_speed

    if enemy_x <= 0 or enemy_x >= WIDTH - enemy_width:
        enemy_speed *= -1
        enemy_y += 20
        enemy2_y += 20
        enemy3_y += 20
        enemy4_y += 20
        enemy5_y += 20

    # Move bullet
    if bullet_active:
        bullet_y -= bullet_speed

        if bullet_y < 0:
            bullet_active = False

    # Collision with first enemy
    if bullet_active:
        if (enemy_x < bullet_x < enemy_x + enemy_width and
            enemy_y < bullet_y < enemy_y + enemy_height):

            bullet_active = False
            score += 1

            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemy_y = 50

    # Draw player
    pygame.draw.rect(
        screen,
        GREEN,
        (player_x, player_y, player_width, player_height)
    )

    # Draw enemies
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.draw.rect(screen, RED, (enemy2_x, enemy2_y, enemy_width, enemy_height))
    pygame.draw.rect(screen, RED, (enemy3_x, enemy3_y, enemy_width, enemy_height))
    pygame.draw.rect(screen, RED, (enemy4_x, enemy4_y, enemy_width, enemy_height))
    pygame.draw.rect(screen, RED, (enemy5_x, enemy5_y, enemy_width, enemy_height))

    # Draw bullet
    if bullet_active:
        pygame.draw.rect(
            screen,
            YELLOW,
            (bullet_x, bullet_y, bullet_width, bullet_height)
        )

    # Draw score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()