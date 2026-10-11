import pygame
import random

# Initialize
pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cloud Dodge")

clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 70, 50, 50)
player_speed = 7

# Clouds
clouds = []

def create_cloud():
    return pygame.Rect(random.randint(0, WIDTH - 80), -60, 80, 50)

cloud_timer = 0

font = pygame.font.SysFont(None, 36)
score = 0

running = True

while running:
    clock.tick(60)
    score += 1

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Spawn clouds
    cloud_timer += 1
    if cloud_timer > 30:
        clouds.append(create_cloud())
        cloud_timer = 0

    # Move clouds
    for cloud in clouds[:]:
        cloud.y += 5
        if cloud.top > HEIGHT:
            clouds.remove(cloud)

        if player.colliderect(cloud):
            running = False

    # Draw
    screen.fill(SKY)

    # Clouds
    for cloud in clouds:
        pygame.draw.ellipse(screen, WHITE, cloud)

    # Player
    pygame.draw.rect(screen, BLUE, player)

    # Score
    text = font.render(f"Score: {score // 10}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()