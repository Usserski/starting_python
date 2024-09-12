import pygame 
import sys
from DeutschLearn import readIO

WIDTH = 800
HEIGHT = 600

#class Button():
 #   def __init__(self):
  #     font = pygame.font.Font(none , 24)
   #    button_surface = pygame.Surface((150,50))
    #   text_button = font.render(text , True , (255 , 0 , 0))
     #  text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
      # return button_surface
       
       
class Game():
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Learning Deutsch")
        self.screen_game = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.button_surface=pygame.Surface((150 ,50))
        self.button_pos = [250 , 250] 
        font = pygame.font.Font(None , 50)
        self.text_button = font.render('text' , True , (250 , 0 , 0))
        self.text_rect = self.text_button.get_rect(center=(self.button_surface.get_width()/2, self.button_surface.get_height()/2))
        self.button_rect = pygame.Rect(125 , 125, 150 , 50)



    def run(self):
        while True:
            self.button_surface.blit(self.text_button , self.text_rect)
            self.screen_game.blit(self.button_surface, (self.button_rect.x , self.button_rect.y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if self.button_rect.collidepoint(event.pos):
                      print("Button clicked!")
            
            pygame.display.update()
            self.clock.tick(60)
            self.screen_game.fill('white')


Game().run()

