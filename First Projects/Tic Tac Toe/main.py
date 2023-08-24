import pygame
import pygame.font
pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
background_color = (192, 168, 132)
window.fill(background_color)
pygame.display.set_caption("Kółko krzyżyk")
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
main_text = "kółko krzyżyk"
main_text_cord = (250, 100)
warning_text = " Nacisnij na pole gry"
warning_text_cord = (250, 700)


def drawning_text(surface, main_text, text_position):
    font_name = pygame.font.match_font('Bold')
    font_size = 64
    font = pygame.font.Font(font_name, font_size)
    text_color = (0, 0, 0)
    text_surface = font.render(main_text, True, text_color)
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

    return cell_react


def check_collision(point, rect):
    x, y = point
    rx, ry, height, width = rect
    return rx < x < rx + width and ry < y < ry + height


def is_mouse_over_area(mouse_pos, area_rect):
    return area_rect.collidepoint(mouse_pos)


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        drawning_text(window, main_text, main_text_cord)
        cell_react = drawning_field()
        pygame.display.update()
        mouse_position = pygame.mouse.get_pos()
        if is_mouse_over_area(mouse_position, cell_react):
            pygame.draw.rect(window, green, cell_react, 50)
        else:
            pygame.draw.rect(window, black, cell_react, 60)

    pygame.quit()


if __name__ == "__main__":
    main()
