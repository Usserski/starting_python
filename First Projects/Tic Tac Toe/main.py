import pygame
import pygame.font
import numpy as np
pygame.init()

WIDTH, HEIGHT = 900, 900

BG_COLOR = (192, 168, 4)
LINE_COLOR = (192, 123, 45)

COLS, ROWS = 3, 3
LINE_WIDTH = 15
SQSIZE = WIDTH // COLS

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko krzyżyk")

window.fill(BG_COLOR)


class Board:

    def __init__(self):
        self.squares = np.squares((ROWS, COLS))

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player

    def empty_sqr(row, col):
        return self.squares[row][col] == 0


class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1
        self.do_lines()
        self.next_turn()

    def do_lines(self):
        # pionowe
        pygame.draw.line(window, LINE_COLOR, (SQSIZE, 0),
                         (SQSIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(window, LINE_COLOR, (WIDTH - SQSIZE, 0),
                         (WIDTH-SQSIZE, HEIGHT), LINE_WIDTH)


# poziome
        pygame.draw.line(window, LINE_COLOR, (0, SQSIZE),
                         (WIDTH, SQSIZE), LINE_WIDTH)

        pygame.draw.line(window, LINE_COLOR, (0, HEIGHT - SQSIZE),
                         (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1


def main():
    game = Game()
    board = game.board

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                if board.empty_sqr(row, col):
                    board.mark_sqe(row, col, 1)
        pygame.display.update()


if __name__ == "__main__":
    main()
