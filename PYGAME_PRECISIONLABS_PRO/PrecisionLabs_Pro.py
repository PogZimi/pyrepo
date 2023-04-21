'''
MIT License

PogZimi , dealtwixyn@gmail.com

Copyright (c) [Enter the year(s) of copyright]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

'''
NOTE : Not even a single piece of this code is taken from anywhere , all of the code is written by me .
Pls donate me a cookie 
'''

import pygame
import random 
import time 

pygame.init()
start_time = pygame.time.get_ticks()

width_w = 800
height = 600 

# WINDOW SETTINGS 
BACKGROUND = (4, 8, 255)
FPS = 160
CLOCK = pygame.time.Clock()

# CIRCLE SETTINGS
CIRCLES = 6
CIRCLE_COLOR = (22, 255, 2)
RADIUS = 25 
COORDINATES = []
DESPAWN_SEC = 1
CIRCLE_OBJECT = []
POINTS = 0
SCORE_ = pygame.font.SysFont('algerian', 20)


timer = 0

window = pygame.display.set_mode((width_w, height))
pygame.display.set_caption('PrecisionLabs Pro')
score_board = pygame.Rect((0,0), (130,25))

# Generates random coordinates for all the circles 
def generate_random_coordinates(cord):
        sample = []
        x_fac = 0 
        y_fac = 0 
        chros  = RADIUS + 20

        for i in range(CIRCLES):
            x_fac = random.randint(chros, width_w - chros)
            y_fac = random.randint(chros+10, height - chros)
            
            sample = [x_fac, y_fac]
            cord.append(sample)

# Generates random coordinates for 1 Circle 
def rand_cord():
        
        chros = RADIUS + 20
        x_fac = random.randint(chros, width_w - chros)
        y_fac = random.randint(chros + 10, height - chros)
         
        cor = [x_fac, y_fac]
        return cor 

# Draws the circles
def draw_circles(cords):
    for i in range(CIRCLES):
        pygame.draw.circle(window, CIRCLE_COLOR, (cords[i][0], cords[i][1]), RADIUS)

# Draws the ScoreBoard txt on the screen
def draw_txt(text):
        draw_txt = SCORE_.render(text, 1, (255,255,255))
        window.blit(draw_txt, (5, 1))

class Labz:

    def update_screen(self, cords, txt):
        window.fill(BACKGROUND)
        draw_circles(COORDINATES)
        pygame.draw.rect(window, (0,0,0), score_board)
        draw_txt(txt)
        pygame.display.update()
        
    # Respawns all the circles after " DESPAWN " seconds at different locations 
    def circle_despawn(self, objectList):
        global timer

        current_time = pygame.time.get_ticks()
        if current_time - timer >= DESPAWN_SEC * 1000:
            for i in range(CIRCLES):
                als = rand_cord()
                objectList[i][0] = als[0]
                objectList[i][1] = als[1]
            timer = current_time
    
    # If the cursor is moved onto the circles , the circle is moved to different location
    def chk_spawn(self, cords, mouse_cords):
        ran = rand_cord()
        global POINTS 

        for i in range(len(cords)):
              if (mouse_cords[0] > (cords[i][0] - RADIUS) and 
                  mouse_cords[0] < (cords[i][0] + RADIUS) and 
                  mouse_cords[1] > (cords[i][1] - RADIUS) and 
                  mouse_cords[1] < (cords[i][1] + RADIUS)
                 ):

                        cords[i][0] = ran[0]
                        cords[i][1] = ran[1]
                        POINTS += 0.1

def main():
    
    global POINTS, minute 
     
    # Generates random coordinates for all the circles when the game is initiated 
    generate_random_coordinates(COORDINATES)
    for i in range(CIRCLES):
        pygame.draw.circle(window , CIRCLE_COLOR , (COORDINATES[i][0] , COORDINATES[i][1]), RADIUS)
    

    # Object 
    player = Labz()
    obj = ""
    mouse_cord = ()
    MOUSE = [1, 2]
    text = " "
    rounded_num = 1.0
 
    
    for i in range(CIRCLES):
        # CIRCLE_OBJECT.append(pygame.draw.circle(window, CIRCLE_COLOR, (COORDINATES[i][0], COORDINATES[i][1]), RADIUS))
        obj = "CIRCLE_" + str(i+1)
        CIRCLE_OBJECT.append(obj)

    # Main LOOP
    RUN = True 
    while RUN:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
               
            mouse_cord = pygame.mouse.get_pos()
            MOUSE[0] = (mouse_cord[0])
            MOUSE[1] = (mouse_cord[1])
        
        # EVERY HIT GIVES 0.1 points , it rounds up the score to 1 decimal digit
        rounded_num  = round(POINTS, 1)
        # Scoreboard's text 
        text = "Score : " + str(rounded_num)
        
        # Defined above 
        player.chk_spawn(COORDINATES, MOUSE)
        player.circle_despawn(COORDINATES)
        player.update_screen(COORDINATES, text)
           
    pygame.quit()

main()
