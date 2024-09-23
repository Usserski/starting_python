import pygame 
import sys
import pdfplumber
import random


WIDTH = 1000
HEIGHT = 800

class Banner():
    def __init__(self, text):
        self.banner_surface = pygame.Surface((WIDTH, 50))  # Szerokość ekranu, wysokość 50
        self.banner_surface.fill((0, 255, 0))  # Kolor niebieski
        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(text, True, (255, 255, 255))  # Biały tekst
        self.text_rect = self.text_surface.get_rect(center=(WIDTH / 2, 25))  # Pozycja tekstu w banerze

    def draw(self, screen):
        screen.blit(self.banner_surface, (0, 0))  # Rysowanie banera na górze ekranu
        screen.blit(self.text_surface, self.text_rect)  # Rysowanie tekstu na banerze

class Button():
    def __init__(self, x , y , text ):
        
        self.button_surface=pygame.Surface((150 ,50))
        font = pygame.font.Font(None , 50)
        self.text_button = font.render(text , True , (250 , 0 , 0))
        self.text_rect = self.text_button.get_rect(center=(self.button_surface.get_width() / 2, self.button_surface.get_height() / 2))
        self.button_rect = pygame.Rect(x, y, 150, 50)
        
     
     
    def draw(self, screen , hover=False):
        if hover:
            self.button_surface.fill((0,255,0))
        else:
            self.button_surface.fill((200 , 200, 200))
                                 
                                 
        self.button_surface.blit(self.text_button, self.text_rect)
        screen.blit(self.button_surface, self.button_rect.topleft)
          

       
class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Learning Deutsch")
        self.screen_game = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.play_button = Button(400 , 400 , 'Play')
        self.banner = Banner("Witaj w grze. Nacisnij 'Play' aby sprawdzić się ze swoim niemieckim ")  
        self.words_data = self.col_data()
        self.random_word = None
        
    def col_data(self):
        words_data = []
        with pdfplumber.open('D:\OneDrive\Dokumenty\GitHub\starting_python\Practice Python\LearningDeutsch\baza_slow.pdf') as file:
            for page in file.pages:
                tables = page.extract_table()
                for table in tables:
                    for row in table:
                        words_data.append(row)
                         
    
        return words_data     
            
        
    def randomize_words(self): 
        if self.words_data:
            self.random_word = random.choice(self.words_data)
            
        
    def run(self):
        while True:
            self.screen_game.fill('white')
            hover = self.play_button.button_rect.collidepoint(pygame.mouse.get_pos())
            self.banner.draw(self.screen_game)
            self.play_button.draw(self.screen_game , hover)
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if self.play_button.button_rect.collidepoint(event.pos):
                        self.randomize_words()  # Wybierz losowe słowo
                        print(f"Wylosowane słowo: {self.random_word}")
                      
                      
            pygame.display.update()
            self.clock.tick(60)
            

if __name__ == "__main__":
    game = Game()
    game.run()

