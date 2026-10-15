import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Thief Escape")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,100,255)
RED = (220,50,50)
YELLOW = (255,220,0)
GREEN = (0,180,0)

font = pygame.font.SysFont(None, 36)
big = pygame.font.SysFont(None, 64)

player = pygame.Rect(100, 100, 40, 40)
player_speed = 6

police = pygame.Rect(650, 450, 40, 40)
police_speed = 3

gold = pygame.Rect(random.randint(20,760), random.randint(20,560), 25, 25)

score = 0
game_over = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player.x, player.y = 100, 100
                police.x, police.y = 650, 450
                gold.x = random.randint(20,760)
                gold.y = random.randint(20,560)
                score = 0
                game_over = False

    keys = pygame.key.get_pressed()

    if not game_over:

        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        if keys[pygame.K_UP]:
            player.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.y += player_speed

        player.clamp_ip(screen.get_rect())

        # Police AI
        if police.x < player.x:
            police.x += police_speed
        elif police.x > player.x:
            police.x -= police_speed

        if police.y < player.y:
            police.y += police_speed
        elif police.y > player.y:
            police.y -= police_speed

        if player.colliderect(gold):
            score += 1
            gold.x = random.randint(20,760)
            gold.y = random.randint(20,560)

            if score % 5 == 0:
                police_speed += 1

        if player.colliderect(police):
            game_over = True

    screen.fill((30,120,30))

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, police)
    pygame.draw.circle(screen, YELLOW, gold.center, 12)

    pygame.draw.rect(screen, BLACK, player, 2)
    pygame.draw.rect(screen, BLACK, police, 2)

    score_text = font.render(f"Gold: {score}", True, WHITE)
    speed_text = font.render(f"Police Speed: {police_speed}", True, WHITE)

    screen.blit(score_text, (20,20))
    screen.blit(speed_text, (20,60))

    if game_over:
        t = big.render("YOU WERE CAUGHT!", True, RED)
        r = font.render("Press R to Restart", True, WHITE)
        screen.blit(t, (WIDTH//2 - t.get_width()//2, 220))
        screen.blit(r, (WIDTH//2 - r.get_width()//2, 300))

    pygame.display.flip()
    clock.tick(60)