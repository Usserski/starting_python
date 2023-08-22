import pygame
import sys

pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Tic-Tac-Toe")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 50)

# Game variables
player_turn = 'X'
game_board = [['', '', ''], ['', '', ''], ['', '', '']]


def draw_board():
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(
                screen, black, (col * 200, row * 200, 200, 200), 2)
            text = font.render(game_board[row][col], True, black)
            text_rect = text.get_rect(
                center=(col * 200 + 100, row * 200 + 100))
            screen.blit(text, text_rect)


def check_winner():
    for row in game_board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] and game_board[0][col] != '':
            return game_board[0][col]
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != '':
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != '':
        return game_board[0][2]
    return None


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row = event.pos[1] // 200
            col = event.pos[0] // 200
            if game_board[row][col] == '':
                game_board[row][col] = player_turn
                player_turn = 'O' if player_turn == 'X' else 'X'

    screen.fill(white)
    draw_board()

    winner = check_winner()
    if winner:
        text = font.render(f"Player {winner} wins!", True, blue)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
