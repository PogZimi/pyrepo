# USE LEFT CLICK TO MOVE THE CIRCLE 
# YES I WROTE THE CODE 
import pygame

pygame.init()

w_width = 800
w_height = 600
w_caption = 'MOVING CIRCLE'
FPS = 120
BG_COLOR = (0, 0, 0)

cords = [w_width // 2 - 48, w_height - 300]
circle_color = (255, 105, 180)
circle_radius = 35
mouse_pos = ()

window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption(w_caption)


class Stax:
    def update_window(self):
        window.fill(BG_COLOR)
        pygame.draw.circle(window, circle_color, cords, circle_radius)
        pygame.display.update()

    def move_circle(self, cords, mouse_pos):
        moving_speed = 0.5
        if cords[0] > mouse_pos[0]:
            cords[0] -= moving_speed
        elif cords[0] < mouse_pos[0]:
            cords[0] += moving_speed
        if cords[1] > mouse_pos[1]:
            cords[1] -= moving_speed
        elif cords[1] < mouse_pos[1]:
            cords[1] += moving_speed


def main():
    global cords
    global mouse_pos
    obj = Stax()
    is_circle_moving = False

    clock = pygame.time.Clock()
    clock.tick(FPS)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                is_circle_moving = True
            else:
                is_circle_moving = False

        if is_circle_moving:
            obj.move_circle(cords, mouse_pos)

        obj.update_window()


main()
