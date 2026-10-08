import pygame
import sys

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH = 600
HEIGHT = 700
LINE_WIDTH = 8
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // 3
CIRCLE_RADIUS = 70
CIRCLE_WIDTH = 10
CROSS_WIDTH = 12
SPACE = 55

# Colors
BG = (240, 240, 240)
LINE = (0, 0, 0)
CIRCLE = (0, 100, 255)
CROSS = (255, 50, 50)
TEXT = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont(None, 50)

board = [[0 for _ in range(3)] for _ in range(3)]
player = 1
game_over = False
winner = None


def draw_lines():
    screen.fill(BG)

    pygame.draw.line(screen, LINE, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE, (400, 0), (400, 600), LINE_WIDTH)

    pygame.draw.line(screen, LINE, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE, (0, 400), (600, 400), LINE_WIDTH)


def draw_figures():
    for row in range(3):
        for col in range(3):

            if board[row][col] == 1:
                pygame.draw.circle(
                    screen,
                    CIRCLE,
                    (col * 200 + 100, row * 200 + 100),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )

            elif board[row][col] == 2:
                pygame.draw.line(
                    screen,
                    CROSS,
                    (col * 200 + SPACE, row * 200 + SPACE),
                    (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE),
                    CROSS_WIDTH,
                )

                pygame.draw.line(
                    screen,
                    CROSS,
                    (col * 200 + SPACE, row * 200 + 200 - SPACE),
                    (col * 200 + 200 - SPACE, row * 200 + SPACE),
                    CROSS_WIDTH,
                )


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def board_full():
    for row in board:
        if 0 in row:
            return False
    return True


def check_win(player):
    global winner

    for col in range(3):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            winner = player
            return True

    for row in range(3):
        if (
            board[row][0] == player
            and board[row][1] == player
            and board[row][2] == player
        ):
            winner = player
            return True

    if (
        board[0][0] == player
        and board[1][1] == player
        and board[2][2] == player
    ):
        winner = player
        return True

    if (
        board[0][2] == player
        and board[1][1] == player
        and board[2][0] == player
    ):
        winner = player
        return True

    return False


def show_message(text):
    pygame.draw.rect(screen, BG, (0, 600, 600, 100))
    msg = font.render(text, True, TEXT)
    rect = msg.get_rect(center=(300, 650))
    screen.blit(msg, rect)


def restart():
    global board, player, game_over, winner
    board = [[0 for _ in range(3)] for _ in range(3)]
    player = 1
    game_over = False
    winner = None
    draw_lines()


draw_lines()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            x = event.pos[0]
            y = event.pos[1]

            if y < 600:

                row = y // 200
                col = x // 200

                if available_square(row, col):

                    mark_square(row, col, player)

                    if check_win(player):
                        game_over = True

                    elif board_full():
                        game_over = True
                        winner = 0

                    player = 2 if player == 1 else 1

    draw_lines()
    draw_figures()

    if game_over:
        if winner == 1:
            show_message("Player O Wins!  Press R")
        elif winner == 2:
            show_message("Player X Wins!  Press R")
        else:
            show_message("Draw!  Press R")
    else:
        if player == 1:
            show_message("Player O Turn")
        else:
            show_message("Player X Turn")

    pygame.display.update()