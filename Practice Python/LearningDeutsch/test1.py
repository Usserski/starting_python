import pygame
import sys
import random

WIDTH = 1000
HEIGHT = 800

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (250, 0, 0)

class Banner():
    def __init__(self, text):
        self.main_banner_surface = pygame.Surface((WIDTH, 70))
        self.main_banner_surface.fill(GREEN)
        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(text, True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.main_banner_surface.get_rect().center)

    def draw(self, screen, x, y):
        screen.blit(self.main_banner_surface, (x, y))
        screen.blit(self.text_surface, self.text_rect)

class Button():
    def __init__(self, x, y, text):
        self.button_surface = pygame.Surface((150, 50))
        font = pygame.font.Font(None, 50)
        self.text_button = font.render(text, True, RED)
        self.text_rect = self.text_button.get_rect(center=(self.button_surface.get_width() / 2, self.button_surface.get_height() / 2))
        self.button_rect = pygame.Rect(x, y, 150, 50)

    def draw(self, screen, hover=False):
        if hover:
            self.button_surface.fill(GREEN)
        else:
            self.button_surface.fill(GRAY)

        self.button_surface.blit(self.text_button, self.text_rect)
        screen.blit(self.button_surface, self.button_rect.topleft)

class TextInput():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = ''
        self.font = pygame.font.Font(None, 36)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Learning Deutsch")
        self.screen_game = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play_button = Button(400, 400, 'Play')
        self.banner = Banner("Witaj w grze!")

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen_game.fill((0, 0, 0))  # Czyszczenie ekranu
        self.banner.draw(self.screen_game, 0, 0)
        self.play_button.draw(self.screen_game)
        pygame.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()