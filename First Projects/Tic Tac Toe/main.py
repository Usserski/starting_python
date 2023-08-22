import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
background_color = (192, 168, 132)
window.fill(background_color)
pygame.display.set_caption("Kółko krzyżyk")


def drawning_text():
    font_name = pygame.font.match_font('Bold')
    font_size = 64
    font = pygame.font.Font(font_name, font_size)
    main_text = " kółko krzyżyk  "
    text_color = (0, 0, 0)
    text_surface = font.render(main_text, True, text_color)
    text_position = (250, 100)
    window.blit(text_surface, text_position)


def drawning_field():
    cell_size = 100
    field_center = 250
    field_color = (255, 255, 255)
    num_rows = 3
    num_columns = 3

    for row in range(num_rows):
        for column in range(num_columns):
            cell_x = column * cell_size + field_center
            cell_y = row * cell_size + field_center
            cell_react = pygame.Rect(cell_x, cell_y, cell_size, cell_size)
            pygame.draw.rect(window, field_color, cell_react, width=1)


def write_symbol(point, rect):
    x, y = point
    rx, ry, height, width = rect
    return rx < x < rx + width and ry < y < ry + height


button_rect = (150, 150, 100, 100)
button_state = "Pusty"
black = (0, 0, 0)


def main():
    running = True
    button_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        drawning_text()
        drawning_field()
        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            button_count += 1
            if button_count % 2 == 0:
                pygame.draw.circle(window, black, mouse_position, 50)

            # if button_count % 2 != 0:
                #pygame.draw.line(window, black, mouse_position, 50)
               # pygame.draw.line(window, black, mouse_position, 50)

    pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
