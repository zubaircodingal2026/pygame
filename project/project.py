import pygame
import sys

pygame.init()

# -----------------------
# Window
# -----------------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grandma's Letter Writer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
LIGHTBLUE = (180, 220, 255)

font = pygame.font.SysFont("arial", 28)
button_font = pygame.font.SysFont("arial", 24)

text = ""
cursor = True
cursor_timer = 0

# Text box
textbox = pygame.Rect(30, 30, 840, 470)

# Buttons
save_button = pygame.Rect(200, 530, 180, 45)
clear_button = pygame.Rect(520, 530, 180, 45)

clock = pygame.time.Clock()

running = True

while running:

    clock.tick(60)

    cursor_timer += 1
    if cursor_timer >= 30:
        cursor = not cursor
        cursor_timer = 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]

            elif event.key == pygame.K_RETURN:
                text += "\n"

            else:
                text += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if save_button.collidepoint(event.pos):
                with open("letter.txt", "w", encoding="utf-8") as f:
                    f.write(text)
                print("Saved!")

            elif clear_button.collidepoint(event.pos):
                text = ""

    screen.fill(GRAY)

    # Text area
    pygame.draw.rect(screen, WHITE, textbox)
    pygame.draw.rect(screen, BLACK, textbox, 2)

    # Draw wrapped text
    x = textbox.x + 10
    y = textbox.y + 10

    lines = text.split("\n")

    for line in lines:
        words = line.split(" ")
        current = ""

        for word in words:
            test = current + word + " "

            if font.size(test)[0] < textbox.width - 20:
                current = test
            else:
                img = font.render(current, True, BLACK)
                screen.blit(img, (x, y))
                y += 32
                current = word + " "

        img = font.render(current, True, BLACK)
        screen.blit(img, (x, y))
        y += 32

    # Cursor
    if cursor:
        pygame.draw.line(screen, BLACK, (x, y), (x, y + 25), 2)

    # Save Button
    pygame.draw.rect(screen, LIGHTBLUE, save_button)
    pygame.draw.rect(screen, BLACK, save_button, 2)
    txt = button_font.render("Save", True, BLACK)
    screen.blit(txt, (save_button.centerx - txt.get_width() // 2,
                      save_button.centery - txt.get_height() // 2))

    # Clear Button
    pygame.draw.rect(screen, LIGHTBLUE, clear_button)
    pygame.draw.rect(screen, BLACK, clear_button, 2)
    txt = button_font.render("Clear", True, BLACK)
    screen.blit(txt, (clear_button.centerx - txt.get_width() // 2,
                      clear_button.centery - txt.get_height() // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()