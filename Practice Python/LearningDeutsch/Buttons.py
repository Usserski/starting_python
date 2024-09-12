import sys
import pygame

def play_button():
    font = pygame.font.Font(None , 25)
    button_surface = pygame.Surface((150 ,50))
    text = font.render("click", True , (255, 255, 255))
    text_rect = text.get_rect(center=(button_surface.get_width()/2 , button_surface.get_height()/2))
    button_rect =pygame.Rect(125 , 125, 150, 50)

