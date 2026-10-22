import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 170, 255)
GREEN = (100, 220, 100)
RED = (255, 120, 120)
GRAY = (220, 220, 220)

# Fonts
title_font = pygame.font.SysFont("arial", 40, bold=True)
font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 22)

clock = pygame.time.Clock()

choices = ["Rock", "Paper", "Scissors"]


class Button:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)

        txt = font.render(self.text, True, BLACK)
        screen.blit(
            txt,
            (
                self.rect.centerx - txt.get_width() // 2,
                self.rect.centery - txt.get_height() // 2,
            ),
        )

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


rock_btn = Button(70, 380, 150, 60, "Rock", BLUE)
paper_btn = Button(275, 380, 150, 60, "Paper", GREEN)
scissor_btn = Button(480, 380, 150, 60, "Scissors", RED)

player_choice = ""
computer_choice = ""
result = "Click a button to start!"

player_score = 0
computer_score = 0


def winner(player, computer):
    if player == computer:
        return "Draw"

    if (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
    ):
        return "Player"

    return "Computer"


running = True

while running:
    screen.fill(WHITE)

    title = title_font.render("Rock Paper Scissors", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    score = font.render(
        f"Player: {player_score}     Computer: {computer_score}",
        True,
        BLACK,
    )
    screen.blit(score, (170, 80))

    player_text = font.render(
        f"Your Choice: {player_choice}",
        True,
        BLACK,
    )
    screen.blit(player_text, (60, 150))

    computer_text = font.render(
        f"Computer: {computer_choice}",
        True,
        BLACK,
    )
    screen.blit(computer_text, (60, 200))

    result_text = font.render(result, True, RED)
    screen.blit(result_text, (60, 270))

    info = small_font.render(
        "First to any score wins. Close the window to quit.",
        True,
        BLACK,
    )
    screen.blit(info, (120, 320))

    rock_btn.draw()
    paper_btn.draw()
    scissor_btn.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if rock_btn.clicked(event.pos):
                player_choice = "Rock"

            elif paper_btn.clicked(event.pos):
                player_choice = "Paper"

            elif scissor_btn.clicked(event.pos):
                player_choice = "Scissors"

            else:
                continue

            computer_choice = random.choice(choices)

            win = winner(player_choice, computer_choice)

            if win == "Draw":
                result = "It's a Draw!"
            elif win == "Player":
                result = "You Win!"
                player_score += 1
            else:
                result = "Computer Wins!"
                computer_score += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()