import pygame
pygame.init()

w_width = 800
w_height = 600
w_caption = ' ScrollingBackGround ! '
FPS = 100
BG_COLOR = (0, 0, 0)

window = pygame.display.set_mode((w_width, w_height))
# Loading our image file into pygame 
sky = pygame.image.load("bsky.png")
# Resizing the image dimensions
sky_png = pygame.transform.scale(sky, (w_width, w_height))
pygame.display.set_caption(w_caption)


# In this case , we are using 3 Frames for Scrolling Background 
bg_xcoord = [0, (w_width), (w_width*2)]
# FRAME SPEED
frame_speed = 1.2
bg_y = 0

class stax:

    def update_window(self):
        global frame_speed, bg_xcoord, bg_y

        # It basically moves the frames , so we can percieve that the background is in motion 
        for i in range(len(bg_xcoord)):
            bg_xcoord[i] -= frame_speed

        window.fill(BG_COLOR)
        window.blit(sky_png, (bg_xcoord[0], bg_y))
        window.blit(sky_png, (bg_xcoord[1], bg_y))
        window.blit(sky_png, (bg_xcoord[2], bg_y))

        # As we are using limited frames , we are repositioning them to their inital position
        for i in range(len(bg_xcoord)):
            if (bg_xcoord[i] < (-(w_width))):
                bg_xcoord[i] = w_width

        pygame.display.update()

# Its the basic pugame stuff , i dont need to explain it
def main():

    global BG_COLOR
    obj = stax()

    clock = pygame.time.Clock()
    clock.tick(FPS)
    run = True
    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

        obj.update_window()


main()
