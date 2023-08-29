import pygame
import pygame.font
import numpy as np

pygame.init()

WIDTH, HEIGHT = 900, 900

BG_COLOR = (192, 168, 4)
LINE_COLOR = (192, 123, 45)
CROSS_COLOR = (45, 23, 45)
CIRCLE_COLOR = (54, 45, 54)

CROSS_WIDTH = 15
CIRC_WIDTH = 15
LINE_WIDTH = 15

COLS, ROWS = 3, 3

SQSIZE = WIDTH // COLS
RADIUS = SQSIZE // 4

OFFSET = 50


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko krzyżyk")

window.fill(BG_COLOR)


class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def final_state(self):

        # vertical
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        # horizontal
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.square[row][0]

        # desc diagonal
            if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                return self.squares[0][0]
        # asc diagonal
            if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
                return self.squares[2][0]

        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqrs(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqrs(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0


class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1
        self.do_lines()

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

    def draw_fig(self, row, col):
        if self.player == 1:

            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE-OFFSET,
                        row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(window, CROSS_COLOR, start_desc,
                             end_desc, CROSS_WIDTH)

            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE-OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(window, CROSS_COLOR, start_asc,
                             end_asc, CROSS_WIDTH)

        elif self.player == 2:

            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(window, CIRCLE_COLOR, center,
                               RADIUS,   CIRC_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def check_win(self, row, col):


def main():
    game = Game()
    board = game.board
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                if board.empty_sqr(row, col):
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
                    game.check_win()

        pygame.display.update()


if __name__ == "__main__":
    main()
