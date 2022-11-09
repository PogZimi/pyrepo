import pygame
import os 

pygame.mixer.init()
pygame.init()

width = 1100
height = 900

win = pygame.display.set_mode((width, height))
icon = pygame.image.load(os.path.join('res', 'images', 'saturnIV.png'))
pygame.display.set_caption('CrazyWare')
pygame.display.set_icon(icon)

arnold = pygame.image.load(os.path.join('res'  ,  'images' , 'starship12.png'))
stallone = pygame.image.load(os.path.join('res' , 'images' , 'starship21.png'))

bg_vol = 0.3
JAP_THEME = pygame.mixer.Sound(os.path.join('res', 'sound', 'wr.mp3'))
JAP_THEME.set_volume(bg_vol)

spaceship_width = 95
spaceship_height = 75
dimension = (spaceship_width, spaceship_height)

arnold = pygame.transform.rotate(pygame.transform.scale(arnold, dimension), 90+45 - 5)
stallone = pygame.transform.rotate(pygame.transform.scale(stallone, dimension), 270+45-10)

FPS = 200

br = {

    "border_x" : width//2 ,
    "border_y" : height // 2,
    "border_width" : width // 2 ,
    "border_height" : height // 2,

}

border1 = pygame.Rect(br["border_x"], br["border_y"], br["border_width"], br["border_height"])
border2 = pygame.Rect(0,0,br["border_width"], br["border_height"])



dark_grey = (55,55,55)
black = (0,0,0)
blue = (0, 0, 255)
red = (255, 0,0)
yellow = (255,211,0)

stallone_crash = pygame.USEREVENT + 1
arnold_crash = pygame.USEREVENT + 2
green = (0,255,0)
red = (255, 0, 0)
blue = (0,0,255)


# Sylvester (x,y)
clox1 = 1000
clox2 = 50

# Arnold (x,y)
clax1 = 100
clax2 = 750

bullet_velocity = 6
max_bullet = 3
motion_v = 2

# Border Settings 
border_half_h = (height//2) // 2
border_half_w = (width//2) // 2

# Triangle Settings 
t_point1 = (width//2, br["border_height"] // 2 - 40)
t_point2 = (width//2, height//2)
t_point3 = ((width//2) // 2 - 40, height//2)

p_point1 = (width//2, br["border_height"] // 2 + (border_half_h*2) - 101)
p_point2 = (width//2, height//2)
p_point3 = ((width//2) - border_half_w + 101, height//2)

c_point1 = (width//2 , height//2)
c_point2 = ((width//2) + border_half_w + 40, height//2)
c_point3 = (width//2, (height//2) + border_half_h + 40)

j_point1 = (width//2, height//2)
j_point2 = (width//2, (height//2) - border_half_h + 101)
j_point3 = ((width//2) + border_half_w - 101, height//2)


square_dim = (50,60)
sq = pygame.Rect((width//2) - 27,br["border_y"] - 27, 55,65)

tr = (t_point1, t_point2, t_point3)
pr = (p_point1, p_point2, p_point3)
cr = (c_point1, c_point2, c_point3)
jr = (j_point1, j_point2, j_point3)


def update_screen(rec1, rec2):
    win.fill(dark_grey)

    pygame.draw.rect(win, black, border1)
    pygame.draw.rect(win, black, border2)
                                         
    pygame.draw.polygon(win, red, tr)
    pygame.draw.polygon(win, green, pr)
    pygame.draw.polygon(win, red, cr)
    pygame.draw.polygon(win, green, jr)
    pygame.draw.rect(win, blue , sq)
    
    # Play song 
    JAP_THEME.play()

    win.blit(arnold ,(rec1.x, rec1.y))
    win.blit(stallone, (rec2.x , rec2.y))


    pygame.display.update()
    

def player_keybind(key, player):
    
    if key[ord('w')]:
         player.y -= motion_v
    elif key[ord('s')]:
         player.y += motion_v
    elif key[ord('a')]:
         player.x -= motion_v
    elif key[ord('d')]:
         player.x += motion_v


def set_border(player, enemy):
     # Player1
     if(player.x < width//2 - 15 ):
          player.x = (width//2 - 15)
     elif(player.y > height//2 - spaceship_height - 28):
          player.y = height//2 - spaceship_height - 28
     elif(player.y < 0):
          player.y = 0.60
     elif(player.x > width - 100):
          player.x = width - 100

     # Player2
     if(enemy.x < 0-14): 
         enemy.x = -13
     elif(enemy.y > height - spaceship_height - 27):
         enemy.y = height - spaceship_height  - 28
     elif(enemy.x > width//2 - spaceship_width - 12.5):
         enemy.x = width//2 - spaceship_width - 12.5
     elif(enemy.y < height//2 - 15): 
         enemy.y = height//2 - 14

def enemy_keybind(key, enemy):
     
    if key[pygame.K_UP]:
         enemy.y -= motion_v
    elif key[pygame.K_DOWN]:
         enemy.y += motion_v
    elif key[pygame.K_LEFT]:
         enemy.x -= motion_v
    elif key[pygame.K_RIGHT]:
         enemy.x += motion_v

def handle_bullet(bul1):
    for bullet in bul1:
       bullet.x += bullet_velocity
       bullet.y -= bullet_velocity


def main():
  
  terminator = pygame.Rect(clax1, clax2,spaceship_width,spaceship_height)
  rocky = pygame.Rect(clox1, clox2, spaceship_width, spaceship_height)
  
  clock = pygame.time.Clock()

  run = True 
  while run:
      clock.tick(FPS)
      for event in pygame.event.get():
         if(event.type == pygame.QUIT):
              run = False  
         
         key = pygame.key.get_pressed() 
         
     
      enemy_keybind(key, rocky)
      player_keybind(key, terminator)
      set_border(rocky, terminator)
      update_screen(terminator, rocky)

  pygame.quit()

if __name__ == "__main__":
     main()


     
