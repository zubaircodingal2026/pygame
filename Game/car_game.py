import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (120,120,120)
RED = (220,0,0)
BLUE = (0,100,255)
YELLOW = (255,255,0)

# Road
ROAD_X = 100
ROAD_WIDTH = 300

# Fonts
font = pygame.font.SysFont(None,35)
bigfont = pygame.font.SysFont(None,70)

# Player
player = pygame.Rect(WIDTH//2-25, HEIGHT-120, 50,90)
player_speed = 8

# Enemy
enemy = pygame.Rect(random.randint(ROAD_X+20, ROAD_X+ROAD_WIDTH-70),-100,50,90)

enemy_speed = 6

score = 0
game_over = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player.x = WIDTH//2-25
                enemy.x = random.randint(ROAD_X+20, ROAD_X+ROAD_WIDTH-70)
                enemy.y = -100
                enemy_speed = 6
                score = 0
                game_over = False

    keys = pygame.key.get_pressed()

    if not game_over:

        if keys[pygame.K_LEFT]:
            player.x -= player_speed

        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        if player.left < ROAD_X:
            player.left = ROAD_X

        if player.right > ROAD_X+ROAD_WIDTH:
            player.right = ROAD_X+ROAD_WIDTH

        enemy.y += enemy_speed

        if enemy.y > HEIGHT:
            enemy.y = -120
            enemy.x = random.randint(ROAD_X+20, ROAD_X+ROAD_WIDTH-70)
            score += 1

            if score % 5 == 0:
                enemy_speed += 1

        if player.colliderect(enemy):
            game_over = True

    # Draw
    screen.fill((20,120,20))

    pygame.draw.rect(screen,GRAY,(ROAD_X,0,ROAD_WIDTH,HEIGHT))

    # Lane lines
    for y in range(0,HEIGHT,50):
        pygame.draw.rect(screen,WHITE,(WIDTH//2-5,y,10,30))

    # Cars
    pygame.draw.rect(screen,BLUE,player)
    pygame.draw.rect(screen,RED,enemy)

    score_text = font.render(f"Score: {score}",True,YELLOW)
    speed_text = font.render(f"Speed: {enemy_speed}",True,YELLOW)

    screen.blit(score_text,(20,20))
    screen.blit(speed_text,(20,60))

    if game_over:
        text = bigfont.render("GAME OVER",True,RED)
        restart = font.render("Press R to Restart",True,WHITE)

        screen.blit(text,(WIDTH//2-text.get_width()//2,250))
        screen.blit(restart,(WIDTH//2-restart.get_width()//2,340))

    pygame.display.update()
    clock.tick(60)