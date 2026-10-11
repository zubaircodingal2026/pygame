import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 900
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Runner")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (40, 180, 40)
GRAY = (100, 100, 100)

font = pygame.font.SysFont(None, 35)
big_font = pygame.font.SysFont(None, 70)

# Ground
GROUND_Y = 320

class Dino:
    def __init__(self):
        self.width = 50
        self.height = 60
        self.x = 80
        self.y = GROUND_Y - self.height
        self.vel = 0
        self.gravity = 0.9
        self.jump_power = -16
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vel = self.jump_power
            self.on_ground = False

    def update(self):
        self.vel += self.gravity
        self.y += self.vel

        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.vel = 0
            self.on_ground = True

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        pygame.draw.circle(screen, BLACK, (self.x + 38, int(self.y + 18)), 3)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Cactus:
    def __init__(self):
        self.width = random.randint(20, 35)
        self.height = random.randint(40, 70)
        self.x = WIDTH + random.randint(0, 200)
        self.y = GROUND_Y - self.height

    def update(self, speed):
        self.x -= speed

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


def reset_game():
    return Dino(), [Cactus()], 8, 0, False


dino, cacti, speed, score, game_over = reset_game()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                if not game_over:
                    dino.jump()

            if event.key == pygame.K_r and game_over:
                dino, cacti, speed, score, game_over = reset_game()

    if not game_over:
        dino.update()

        score += 1

        if score % 500 == 0:
            speed += 0.5

        for cactus in cacti:
            cactus.update(speed)

        if cacti[-1].x < WIDTH - random.randint(250, 350):
            cacti.append(Cactus())

        cacti = [c for c in cacti if c.x + c.width > 0]

        for cactus in cacti:
            if dino.rect().colliderect(cactus.rect()):
                game_over = True

    # Draw
    screen.fill(WHITE)

    pygame.draw.line(screen, GRAY, (0, GROUND_Y), (WIDTH, GROUND_Y), 3)

    dino.draw()

    for cactus in cacti:
        cactus.draw()

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    if game_over:
        text = big_font.render("GAME OVER", True, BLACK)
        restart = font.render("Press R to Restart", True, BLACK)

        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 120))
        screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, 200))

    pygame.display.flip()