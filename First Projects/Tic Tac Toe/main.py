import pygame

pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
background_color = (192, 168, 132)
window.fill(background_color)


def drawning_text():
    font_name = pygame.font.match_font('Bold')
    font_size = 64
    font = pygame.font.Font(font_name, font_size)
    main_text = " Kółko krzyżyk "
    text_color = (0, 0, 0)
    text_surface = font.render(main_text, True, text_color)
    text_position = (250, 100)
    window.blit(text_surface, text_position)


def drawning_field():
    cell_position = (250, 200)
    cell_size = 100
    num_rows = 3
    num_columns = 3
    for row in range(num_rows):
        for column in range(num_columns):
            cell_x = column * cell_size
            cell_y = row * cell_size
            cell_react = pygame.Rect(cell_x, cell_y, cell_size, cell_size)
            pygame.draw.rect(cell_position, (255, 255, 255), cell_react)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        drawning_text()
        drawning_field()
        pygame.display.flip()

pygame.quit()
