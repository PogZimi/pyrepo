import pygame 
import os 

# Enable font library 
pygame.font.init()
# Enable sound library in pygame 
pygame.mixer.init()
pygame.init()

# Display 
w_width = 900
w_height = 500

width = 55
height = 40
dimension_ship = (width,height)

win_dll = (w_width, w_height)
win = pygame.display.set_mode(win_dll)
pygame.display.set_caption('Thickware')


icon = pygame.image.load(os.path.join('Resources', 'images', 'saturnIV.png'))
protp = pygame.image.load(os.path.join('Resources', 'images', 'starship12.png'))
protj = pygame.image.load(os.path.join('resources', 'images', 'starship21.png'))
bg_image = pygame.image.load(os.path.join('Resources', 'images', 'space.png'))

# Sound 
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('resources', 'sound', 'Hit_sound.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('resources', 'sound', 'Firing.mp3'))

# Text / Font 
HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)

velocity = 3
bullet_vel = 6
max_bullet = 2

falcon_hit = pygame.USEREVENT + 1
titan_hit = pygame.USEREVENT + 2

protp  =  pygame.transform.rotate(pygame.transform.scale(protp, dimension_ship),90)
protj = pygame.transform.rotate(pygame.transform.scale(protj, dimension_ship),270)
bg_image = pygame.transform.scale(bg_image, win_dll)
border_plot = pygame.Rect(w_width//2 - 5, 0, 10, w_height)

grey = (155,155,155)
dark_grey = (55,55,55)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
yellow = (255,255,0)
origin = (0,0)
purple = (205, 0, 255)

FPS = 135

# []
x1 = 100
y1 = 250
# [] 
x2 = 700
y2 = 250

pygame.display.set_icon(icon)

def update():
    pygame.display.update()

# BG COLOUR SETTING 
def update_screen(apollo, dragon, falcon_bullets , titan_bullets, r_health, p_health):
    win.blit(bg_image, origin)
    pygame.draw.rect(win, black, border_plot);
    win.blit(protp, (apollo.x, apollo.y))
    win.blit(protj, (dragon.x, dragon.y))
     
    red_text = HEALTH_FONT.render("Health : " + str(r_health), 1, white)
    blue_text = HEALTH_FONT.render("Health : " + str(p_health), 1, white)  
    
    r_x = w_width - red_text.get_width() - 9
    win.blit(red_text, (r_x, 10))
    win.blit(blue_text, (10, 10))

    for bullet in titan_bullets:
         pygame.draw.rect(win,red,bullet)
    for bullet in falcon_bullets:
         pygame.draw.rect(win,blue,bullet)
    update()

# Keybind settings 
def y_move(keys, falcon_series):

    move_right = falcon_series.x + velocity 
    move_left = falcon_series.x - velocity 
     
    if keys[ord('w')] and falcon_series.y - velocity > 0  :                 # UPWARDS [ Y ]
       falcon_series.y -= velocity;  
    elif keys[ord('s')] and (falcon_series.y + velocity) < w_height - falcon_series.width+1:                # DOWNWARDS[ Y ]
       falcon_series.y += velocity;         
    elif keys[ord('a')] and move_left > 0:                # LEFT [X]
       falcon_series.x -= velocity
    elif keys[ord('d')] and (move_right) < border_plot.x - falcon_series.width :   # Manually changing rocket's horizontal velocity & checking if it touches the border (if it succeeds in it then only its able to move)
       falcon_series.x += velocity 

def r_move(keys, soyuz):
    if keys[pygame.K_UP] and soyuz.y - velocity > 0:
       soyuz.y -= velocity
    elif keys[pygame.K_DOWN] and soyuz.y + velocity < w_height - soyuz.height - 12.5:
       soyuz.y += velocity 
    elif keys[pygame.K_RIGHT] and (soyuz.x + velocity) < w_width - soyuz.width + 10:
       soyuz.x += velocity
    elif keys[pygame.K_LEFT] and (soyuz.x - velocity) > border_plot.x + 20 :
       soyuz.x -= velocity

def handle_movements(falcon_bullets, titan_bullets, falcon, titan):
    # Bullet is an rectangle(which acts as a bullet) in our bullet_list 
    for bullet in falcon_bullets:
          bullet.x += bullet_vel 
          if titan.colliderect(bullet):
            pygame.event.post(pygame.event.Event(titan_hit))
            falcon_bullets.remove(bullet)
          elif bullet.x > w_width:
             falcon_bullets.remove(bullet)

    for bullet in titan_bullets:
          bullet.x -= bullet_vel 
          if falcon.colliderect(bullet):
            pygame.event.post(pygame.event.Event(falcon_hit))           
            titan_bullets.remove(bullet)
          elif bullet.x < 0:
             titan_bullets.remove(bullet)

# Text = winner won!!! 
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, purple)

    win.blit(draw_text, (w_width // 2 - draw_text.get_width() / 2, w_height // 2))
    pygame.display.update()
    pygame.time.delay(5000)

def game():

    falcon9 = pygame.Rect(x1,y1,width,height)
    Titan = pygame.Rect(x2,y2,width,height)

    titan_bullets = []
    falcon_bullets = []
   
    p_health = 10
    r_health = 10

    clock = pygame.time.Clock()
     
    run = True 
    while run :

         clock.tick(FPS)
 
         for event in pygame.event.get():
             if(event.type == pygame.QUIT):
                  run = False 
                                                                                                                  
             if(event.type == pygame.KEYDOWN):
                 if(event.key == pygame.K_LCTRL) and len(falcon_bullets) < max_bullet:
                        bullet = pygame.Rect((falcon9.x + falcon9.width),(falcon9.y + falcon9.height//2 - 2) , 10, 5)
                        BULLET_FIRE_SOUND.play()
                        falcon_bullets.append(bullet)
                         
                 if(event.key == pygame.K_RCTRL) and len(titan_bullets) < max_bullet:
                        bullet = pygame.Rect(Titan.x, (Titan.y + Titan.width//2 - 2) , 10, 5)
                        BULLET_FIRE_SOUND.play()
                        titan_bullets.append(bullet)
                        
             if(event.type == titan_hit):
                   r_health -= 1
                   BULLET_HIT_SOUND.play()

             if(event.type == falcon_hit):
                   p_health -= 1
                   BULLET_HIT_SOUND.play()
          
         winner_text = ""
         if r_health <= 0:
            winner_text = "Falcon9 Wins!!"

         if p_health <= 0:
            winner_text = "Titan  Wins!!"

         if winner_text != "":
            draw_winner(winner_text)
            break

         keys = pygame.key.get_pressed() 
         y_move(keys, falcon9)           
         r_move(keys, Titan)
         handle_movements(falcon_bullets, titan_bullets, falcon9, Titan)
         update_screen(falcon9, Titan, falcon_bullets, titan_bullets, r_health, p_health)                    
    game() # If we break loop it will run game() again 

if __name__ == "__main__":
      game()
