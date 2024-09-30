import pygame 
import sys
import random

WIDTH = 1000
HEIGHT = 800

class Banner():
    def __init__(self, text):
        self.main_banner_surface = pygame.Surface((WIDTH, 70))  # Szerokość ekranu, wysokość 70
        self.main_banner_surface.fill((0, 255, 0))  # Kolor zielony
        font = pygame.font.Font(None, 36)  # czcionka i rozmiar tekstu
        self.text_surface = font.render(text, True, (255, 255, 255))  # Biały tekst
        self.text_rect = self.text_surface.get_rect(center=(WIDTH / 2, 35))  # Pozycja tekstu w banerze


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

class TextInput():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.text = ''
        self.font = pygame.font.Font(None, 36)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active  # Przełącz aktywność
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:  # Zatwierdź wejście
                return self.text  # Zwróć tekst, gdy użytkownik naciśnie Enter
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # Usuwanie ostatniego znaku
            else:
                self.text += event.unicode  # Dodawanie znaku do tekstu

    def draw(self, screen):
        # Rysowanie pola tekstowego
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
        self.next_button = Button(600, 400, 'Next')
        self.banner = Banner("Witaj w grze. Nacisnij 'Play' aby sprawdzić się ze swoim niemieckim ")
        self.words = self.col_data()
        self.pl_words = self.words[1]
        self.de_words = self.words[0]
        self.random_word = None
        self.score = 0
        self.font = pygame.font.Font(None, 40)
        self.game_started = False  # Flaga do śledzenia stanu gry
        self.text_input = TextInput(400, 500, 300, 50)  # Pole tekstowe do odpowiedzi
        self.question = None  # Ustaw pytanie

    def display_score(self):
        
        score_text = self.font.render(f"Twój wynik: {self.score}/{len(self.de_words)} ", True, (0, 0, 0))
        self.screen_game.blit(score_text, (WIDTH // 10 - score_text.get_width() // 32, HEIGHT // 10))

    def col_data(self):
        pl_words = []
        de_words = []
        i=1
        file_path = 'C:\\Users\\user\\Documents\\GitHub\\starting_python\\Practice Python\\LearningDeutsch\\baza_inf.txt'
        with open(file_path, encoding='utf-8') as file:
            for linia in file:
                pl, de = linia.strip().split(' - ')
                pl_words.append((i, pl))
                de_words.append((i , de))
                i+=1
                
        return  de_words , pl_words

    def randomize_words(self):
        if self.words:
            random_word = random.choice(self.pl_words)
            self.question = Banner(f'Wpisz tłumaczenie: {random_word[1]}')
            self.random_word = random_word  # Zapamiętaj losowe słowo

    def check_answer(self):
        if self.random_word:
            wpisane_tlumaczenie = self.text_input.text.strip()
            poprawne_tlumaczenie = self.de_words[self.random_word[0] - 1][1]  # Pobierz poprawne tłumaczenie z de_words
            if wpisane_tlumaczenie.lower() == poprawne_tlumaczenie.lower():
                self.score += 1
                print("Poprawne tłumaczenie!")
            else:
                print("Niestety, to nie jest poprawne tłumaczenie.")
            self.text_input.text = ''  # Wyczyść pole tekstowe
            self.randomize_words()  # Losuj nowe słowo

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.text_input.handle_event(event)  # Obsługuje zdarzenia dla pola tekstowego

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Lewy przycisk myszy
                        if self.play_button.button_rect.collidepoint(event.pos):
                            self.game_started = True  # Rozpocznij grę
                            self.randomize_words()  # Losuj pierwsze słowo

                        if self.next_button.button_rect.collidepoint(event.pos):
                            self.randomize_words()  # Losuj nowe słowo

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.game_started:
                        self.check_answer()  # Sprawdź odpowiedź

            self.screen_game.fill('white')

            # Rysowanie elementów w zależności od stanu gry
            if not self.game_started:
                self.banner.draw(self.screen_game, 0, 0)
                self.play_button.draw(self.screen_game, self.play_button.button_rect.collidepoint(pygame.mouse.get_pos()))
            else:
                if self.question:
                    self.question.draw(self.screen_game, 0, 0)
                self.display_score()  # Wyświetl wynik
                self.text_input.draw(self.screen_game)
                self.next_button.draw(self.screen_game, self.next_button.button_rect.collidepoint(pygame.mouse.get_pos()))

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()