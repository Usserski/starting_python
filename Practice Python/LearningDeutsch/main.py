import pygame 
import sys
import random

WIDTH = 1000
HEIGHT = 800

class Banner():
    def __init__(self, text):
        self.main_banner_surface = pygame.Surface((WIDTH, 50))  # Szerokość ekranu, wysokość 50
        self.main_banner_surface.fill((0, 255, 0))  # Kolor zielony
        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(text, True, (255, 255, 255))  # Biały tekst
        self.text_rect = self.text_surface.get_rect(center=(WIDTH / 2, 25))  # Pozycja tekstu w banerze

    def draw(self, screen, x, y):
        screen.blit(self.main_banner_surface, (x, y))  # Rysowanie banera na górze ekranu
        screen.blit(self.text_surface, self.text_rect)  # Rysowanie tekstu na banerze

class Button():
    def __init__(self, x, y, text):
        self.button_surface = pygame.Surface((150, 50))
        font = pygame.font.Font(None, 50)
        self.text_button = font.render(text, True, (250, 0, 0))
        self.text_rect = self.text_button.get_rect(center=(self.button_surface.get_width() / 2, self.button_surface.get_height() / 2))
        self.button_rect = pygame.Rect(x, y, 150, 50)

    def draw(self, screen, hover=False):
        if hover:
            self.button_surface.fill((0, 255, 0))  # Kolor zielony przy najechaniu
        else:
            self.button_surface.fill((200, 200, 200))  # Szary kolor

        self.button_surface.blit(self.text_button, self.text_rect)
        screen.blit(self.button_surface, self.button_rect.topleft)

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Learning Deutsch")
        self.screen_game = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play_button = Button(400, 400, 'Play')
        self.next_button = Button(600, 400, 'Next')
        self.banner = Banner("Witaj w grze. Nacisnij 'Play' aby sprawdzić się ze swoim niemieckim ")
        self.words_data = self.col_data()
        self.random_word = None
        self.question_banner = None  # Zmienna do pytania
        self.game_started = False

    def col_data(self):
        words_data = []
        file_path = 'D:\\OneDrive\\Dokumenty\\GitHub\\starting_python\\Practice Python\\LearningDeutsch\\baza_inf.txt' 
        with open(file_path, encoding='utf-8') as file:
            for linia in file:
                pl_word, de_word = linia.strip().split(' - ')
                words_data.append((pl_word, de_word))
        return words_data

    def randomize_words(self):
        if self.words_data:
            self.random_word = random.choice(self.words_data)
            self.question_banner = Banner(f"Podaj tłumaczenie: {self.random_word[0]}")  # Ustaw pytanie

    def run(self):
        while True:
            for event in pygame.event.get():
                self.banner.draw(self.screen_game, 0, 0)
                hover = self.play_button.button_rect.collidepoint(pygame.mouse.get_pos())
                self.play_button.draw(self.screen_game, hover)
                self.screen_game.fill('white')
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.button_rect.collidepoint(event.pos):
                        
                        self.randomize_words()  # Losuj słow
                        self.game_started = True
                        
                        
                self.screen_game.fill('white')

                if not self.game_started:  # Jeśli gra się nie rozpoczęła, wyświetl przycisk
                    hover = self.play_button.button_rect.collidepoint(pygame.mouse.get_pos())
                    self.play_button.draw(self.screen_game, hover)
                    self.banner.draw(self.screen_game, 0, 0)
                else:  # Jeśli gra się rozpoczęła, wyświetl baner z pytaniem
                    self.question_banner.draw(self.screen_game, 0, 60)  # Rysuj baner z pytaniem
                    self.next_button.draw(self.screen_game , hover)
                    print(self.words_data)

            
            
            pygame.display.flip()  # Odśwież ekran
            self.clock.tick(60)  # Ustawienie liczby klatek na sekundę

if __name__ == "__main__":
    game = Game()
    game.run()