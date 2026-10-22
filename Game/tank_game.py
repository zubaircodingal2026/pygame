import pygame
import random
import math

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 180, 50)
RED = (220, 60, 60)
BLUE = (70, 120, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont(None, 30)

# ------------ BACKGROUND ------------
try:
    background = pygame.image.load("istockphoto-2227517279-612x612.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except:
    background = None
# ------------------------------------


class Bullet:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.speed = 10
        self.angle = angle
        self.radius = 5

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self):
        pygame.draw.circle(
            screen,
            YELLOW,
            (int(self.x), int(self.y)),
            self.radius
        )


class Tank:

    def __init__(self):

        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 5
        self.health = 100
        self.angle = 0

    def move(self, keys):

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed


        self.x = max(20, min(WIDTH - 20, self.x))
        self.y = max(20, min(HEIGHT - 20, self.y))


    def aim(self, keys):

        if keys[pygame.K_LEFT]:
            self.angle -= 0.08

        if keys[pygame.K_RIGHT]:
            self.angle += 0.08


    def draw(self):

        pygame.draw.rect(
            screen,
            BLUE,
            (self.x - 30, self.y - 22, 60, 45)
        )

        endx = self.x + math.cos(self.angle) * 30
        endy = self.y + math.sin(self.angle) * 30

        pygame.draw.line(
            screen,
            BLACK,
            (self.x, self.y),
            (endx, endy),
            6
        )


class Enemy:

    def __init__(self):

        side = random.choice(
            ["top", "bottom", "left", "right"]
        )


        if side == "top":
            self.x = random.randint(0, WIDTH)
            self.y = -30

        elif side == "bottom":
            self.x = random.randint(0, WIDTH)
            self.y = HEIGHT + 30

        elif side == "left":
            self.x = -30
            self.y = random.randint(0, HEIGHT)

        else:
            self.x = WIDTH + 30
            self.y = random.randint(0, HEIGHT)


        self.speed = random.randint(1, 2)


    def update(self, player):

        dx = player.x - self.x
        dy = player.y - self.y

        dist = math.hypot(dx, dy)

        if dist != 0:

            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed


    def draw(self):

        pygame.draw.rect(
            screen,
            RED,
            (self.x - 18, self.y - 18, 36, 36)
        )


player = Tank()

bullets = []

enemies = []

score = 0

spawn_timer = 0
running = True


while running:

    clock.tick(60)

    spawn_timer += 1


    if spawn_timer >= 120:

        enemies.append(Enemy())
        spawn_timer = 0



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bx = player.x + math.cos(player.angle) * 30
                by = player.y + math.sin(player.angle) * 30

                bullets.append(
                    Bullet(
                        bx,
                        by,
                        player.angle
                    )
                )



    keys = pygame.key.get_pressed()

    player.move(keys)
    player.aim(keys)



    # Bullet movement and collision

    for bullet in bullets[:]:

        bullet.update()


        if (
            bullet.x < 0 or
            bullet.x > WIDTH or
            bullet.y < 0 or
            bullet.y > HEIGHT
        ):

            bullets.remove(bullet)
            continue



        for enemy in enemies[:]:

            if math.hypot(
                enemy.x - bullet.x,
                enemy.y - bullet.y
            ) < 22:


                enemies.remove(enemy)

                if bullet in bullets:
                    bullets.remove(bullet)

                score += 1

                break




    # Enemy movement

    for enemy in enemies[:]:

        enemy.update(player)


        if math.hypot(
            enemy.x - player.x,
            enemy.y - player.y
        ) < 28:


            enemies.remove(enemy)

            player.health -= 10




    # -------- DRAW BACKGROUND --------

    if background:

        screen.blit(background, (0,0))

    else:

        screen.fill((120,180,120))


    # Draw player

    player.draw()



    # Draw bullets

    for bullet in bullets:

        bullet.draw()



    # Draw enemies

    for enemy in enemies:

        enemy.draw()



    # Health bar

    pygame.draw.rect(
        screen,
        RED,
        (20,20,200,20)
    )


    pygame.draw.rect(
        screen,
        GREEN,
        (20,20,player.health*2,20)
    )



    # Text

    score_text = font.render(
        f"Score: {score}",
        True,
        BLACK
    )

    health_text = font.render(
        f"Health: {player.health}",
        True,
        BLACK
    )


    screen.blit(score_text,(20,50))

    screen.blit(health_text,(20,80))



    # Game over

    if player.health <= 0:


        game_over = font.render(
            "GAME OVER - Press X to Quit",
            True,
            BLACK
        )


        screen.blit(
            game_over,
            (330,340)
        )


        pygame.display.flip()


        waiting = True


        while waiting:


            for e in pygame.event.get():

                if e.type == pygame.QUIT:

                    waiting = False
                    running = False


                if e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_x:

                        waiting = False
                        running = False



    pygame.display.flip()



pygame.quit()