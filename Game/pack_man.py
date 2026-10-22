import pygame
import random
import math
import sys

pygame.init()

WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

TILE = 32

maze = [
"####################",
"#........#.........#",
"#.####...#...####..#",
"#..................#",
"#.####.#####.####..#",
"#..................#",
"#.####...#...####..#",
"#........#.........#",
"#..................#",
"####################"
]

player = pygame.Rect(40, 40, 24, 24)
ghost = pygame.Rect(560, 280, 24, 24)

dots = []

for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == ".":
            dots.append((col * TILE + 16, row * TILE + 16))

score = 0
speed = 4
ghost_speed = 1   # 👈 Ghost is now slower

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    old = player.copy()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "#":
                wall = pygame.Rect(col*TILE, row*TILE, TILE, TILE)
                if player.colliderect(wall):
                    player = old

    for dot in dots[:]:
        if math.hypot(player.centerx-dot[0], player.centery-dot[1]) < 18:
            dots.remove(dot)
            score += 10

    # Slower Ghost
    if ghost.x < player.x:
        ghost.x += ghost_speed
    elif ghost.x > player.x:
        ghost.x -= ghost_speed

    if ghost.y < player.y:
        ghost.y += ghost_speed
    elif ghost.y > player.y:
        ghost.y -= ghost_speed

    if player.colliderect(ghost):
        print("Game Over!")
        running = False

    screen.fill(BLACK)

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "#":
                pygame.draw.rect(screen, BLUE, (col*TILE, row*TILE, TILE, TILE))

    for dot in dots:
        pygame.draw.circle(screen, WHITE, dot, 4)

    pygame.draw.circle(screen, YELLOW, player.center, 12)
    pygame.draw.circle(screen, RED, ghost.center, 12)

    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 610))

    if len(dots) == 0:
        win = font.render("YOU WIN!", True, YELLOW)
        screen.blit(win, (240, 300))

    pygame.display.flip()

pygame.quit()
sys.exit()