import pygame
import random 
import time 

width = 1200
height = 900

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('LOADING_SCREEN')
BOOL_VAL = None
DELAY = 1 

left_small = pygame.Rect(width//2 - 200, width//2 + 65, 2, 25)
right_small = pygame.Rect(width//2 + 200, width//2 + 65, 2 , 25)

upper_big = pygame.Rect(left_small.x , left_small.y - 3, (right_small.x - left_small.x + 2), 4)
lower_big = pygame.Rect(left_small.x , left_small.y + left_small.height, (right_small.x - left_small.x + 2) , 4 )

WHITE_REC_LOADER = pygame.Rect(left_small.x + left_small.width , left_small.y , 30, left_small.height+1)
var = (upper_big.width - left_small.width) - 10

def increment():
    global var 
    random_num = random.randint(32, 41)
    time.sleep(DELAY)
    if(WHITE_REC_LOADER.width + random_num < var):
       WHITE_REC_LOADER.width = WHITE_REC_LOADER.width + random_num
    else: 
       WHITE_REC_LOADER.width = WHITE_REC_LOADER.width + 9

class LOADING_SCREEN:
    def update_screen(self):
        window.fill((0,0,0))
        pygame.draw.rect(window, (255,255,255), left_small)
        pygame.draw.rect(window, (255,255,255), right_small)
        pygame.draw.rect(window, (255,255,255), upper_big)
        pygame.draw.rect(window, (255,255,255), lower_big)
        pygame.draw.rect(window, (255,255,255), WHITE_REC_LOADER)
        pygame.display.update()
      
o = LOADING_SCREEN()
var = 0 
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    increment()
    var = (upper_big.width - left_small.width) - 34
    if(WHITE_REC_LOADER.width > var):
            run = False
    o.update_screen()
