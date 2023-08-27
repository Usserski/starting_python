import pygame
import pygame.font
pygame.init()

WIDTH, HEIGHT = 1000, 800

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko krzyżyk")


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    mouse_position = pygame.mouse.get_pos()

    pygame.quit()


if __name__ == "__main__":
    main()
