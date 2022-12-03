import pygame
import os 

pygame.init()
pygame.font.init()
pygame.mixer.init()

width = 1400
height = 950

win = pygame.display.set_mode((width, height))
icon = pygame.image.load(os.path.join('res', 'images', 'saturnIV.png'))
pygame.display.set_caption('Vrectog')
pygame.display.set_icon(icon)

arnold = pygame.image.load(os.path.join('res'  ,  'images' , 'starship12.png'))
stallone = pygame.image.load(os.path.join('res' , 'images' , 'starship21.png'))
bulletr = pygame.image.load(os.path.join('res', 'images', 'bullet.png'))
winner_load = pygame.image.load(os.path.join('res', 'images', 'neverland.png'))

HIT_SOUND = pygame.mixer.Sound(os.path.join('res', 'sound', 'hit.mp3'))
FIRING_SOUND = pygame.mixer.Sound(os.path.join('res', 'sound', 'rifler.mp3'))

bullet_em = pygame.transform.rotate(pygame.transform.scale(bulletr, (15, 20)), 90 + 45)
bulletr = pygame.transform.rotate(pygame.transform.scale(bulletr, (15, 20)), 270 + 35 )

dummy_hero = pygame.image.load(os.path.join('res'  ,  'images' , 'starship12.png'))
dummy_villian = pygame.image.load(os.path.join('res' , 'images' , 'starship21.png'))
dummy_hero = pygame.transform.scale(arnold, (140, 125))
dummy_villian = pygame.transform.scale(stallone, (140, 125))

spaceship_width = 95
spaceship_height = 75
dimension = (spaceship_width, spaceship_height)

arnold = pygame.transform.rotate(pygame.transform.scale(arnold, dimension), 90+45 - 5)
stallone = pygame.transform.rotate(pygame.transform.scale(stallone, dimension), 270+45-10)
winner_load = pygame.transform.scale(winner_load, (width, height))

FPS = 140

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

# Sylvester 
clox1 = 1000
clox2 = 50
# Arnold 
clax1 = 100
clax2 = 750

bullet_velocity = 7
max_bullet = 4
motion_v = 3.5

border_half_h = (height//2) // 2
border_half_w = (width//2) // 2

brominer =  {
     
     # Upper Rect1 (big) 
     "width" : (width//2) // 2 - 40,
     "height" : br["border_height"],
     "x" : 0,
     "y" : 0,
     # Upper Rect2 (small)
     "width2" : (width//2) // 2 + 40,
     "height2" : br["border_height"] // 2 - 40,
     "x2" : (width//2) // 2 - 40,
     "y2" : 0,

     # LOWER RECTS 
     "widther" : width//2,
     "heighter" : height - (height//2) + border_half_h + 40,
     "xr" : width//2,
     "xy" : (height//2) + border_half_h + 40,
   
     "bruh_w" : (width//2) // 2 - 40,
     "bruh_h" : (height//2) - (height//2) + border_half_h + 40,
     "bruh_x" : (width//2) + border_half_w + 40,
     "bruh_y" : (height//2)

}

recterer = pygame.Rect(brominer["x2"], brominer["y2"], brominer["width2"], brominer["height2"])


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

white = (255,255,255)

bull_bound = pygame.Rect(brominer["x"], brominer["y"], brominer["width"] + 3, brominer["height"])
squid1 = pygame.Rect(brominer["xr"], brominer["xy"], brominer["widther"], brominer["heighter"])
squid2 = pygame.Rect(brominer["bruh_x"], brominer["bruh_y"], brominer["bruh_w"], brominer["bruh_h"])

square_dim = (50,60)
sq = pygame.Rect((width//2) - 27,br["border_y"] - 27, 55,65)

tr = (t_point1, t_point2, t_point3)
pr = (p_point1, p_point2, p_point3)
cr = (c_point1, c_point2, c_point3)
jr = (j_point1, j_point2, j_point3)

bullet_x = 110
bullet_y = 780

bullet_limit = 3

HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 70)
yellow = (255,255,0)

def update_screen(rec1, rec2, arnolder, stalloner, r_health, p_health):
    win.fill(dark_grey)

    pygame.draw.rect(win, black, border1)
    pygame.draw.rect(win, black, border2)

    # Upper RECTANGLES 
    pygame.draw.rect(win, black, bull_bound)
    pygame.draw.rect(win, black, recterer)
    # Lower RECTANGLE
    pygame.draw.rect(win, black, squid1)
    pygame.draw.rect(win, black, squid2)

    pygame.draw.polygon(win, red, tr)
    pygame.draw.polygon(win, green, pr)
    pygame.draw.polygon(win, red, cr)
    pygame.draw.polygon(win, green, jr)
#     pygame.draw.polygon(win, green, xr)
    red_text = HEALTH_FONT.render("Health : " + str(r_health), 1, white)
    blue_text = HEALTH_FONT.render("Health : " + str(p_health), 1, white)  
     
    win.blit(red_text, (width - red_text.get_width() - 5, height - 50))
    win.blit(blue_text, (10, 10))

    pygame.draw.rect(win, blue , sq)

    win.blit(arnold ,(rec1.x, rec1.y))
    win.blit(stallone, (rec2.x , rec2.y))
    
    for bullet in arnolder:
        pygame.draw.rect(win, (0, 255, 0), bullet)
        win.blit(bulletr, (bullet.x - 8, bullet.y - 8.5))
        
    
    for bullet in stalloner:
        pygame.draw.rect(win, (255,0,0), bullet)
        win.blit(bullet_em, (bullet.x - (bullet.width//2 ) - 3, bullet.y - (spaceship_width//2)//2 + (bullet.height*2) + 2))
        
       
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

def bullet_movement(arnolder, stalloner, rec1, rec2):

    for bullet in arnolder:
        bullet.x += motion_v
        bullet.y -= motion_v 
        if(bullet.colliderect(rec2)):
           pygame.event.post(pygame.event.Event(stallone_crash))
           arnolder.remove(bullet)
        elif(bullet.colliderect(bull_bound) or bullet.colliderect(recterer) or bullet.colliderect(squid1) or bullet.colliderect(squid2)):
           arnolder.remove(bullet)
        elif(bullet.x > 1050):
           arnolder.remove(bullet)
        elif(bullet.y < 10):
           arnolder.remove(bullet)
     
    for bullet in stalloner:
        bullet.x -= motion_v - 1
        bullet.y += motion_v - 1
        if(bullet.colliderect(rec1)):
           pygame.event.post(pygame.event.Event(arnold_crash))
           stalloner.remove(bullet)
        elif(bullet.colliderect(bull_bound) or bullet.colliderect(recterer) or bullet.colliderect(squid1) or bullet.colliderect(squid2)):
           stalloner.remove(bullet)
        elif(bullet.x < 0):
           stalloner.remove(bullet)
        elif(bullet.y > 850):
           stalloner.remove(bullet)
        
def draw_txt(text, post):
     texter = WINNER_FONT.render(text, 1, yellow)
     origin = (0,0)
     win.blit(winner_load, origin)
     if(post == 0):
          win.blit(dummy_villian, (width//2 - spaceship_width//2, height//2 + spaceship_height))
     elif(post == 1):
          win.blit(dummy_hero, (width//2 - spaceship_width//2, height//2 + spaceship_height))

     win.blit(texter, (width // 2 - texter.get_width() / 2, height // 2 - texter.get_height()))
     pygame.display.update()
     pygame.time.delay(7000)

           
def main():
  
  terminator = pygame.Rect(clax1, clax2,spaceship_width - 12,spaceship_height - 12)
  rocky = pygame.Rect(clox1, clox2+5, spaceship_width - 4, spaceship_height - 4)
  
  player_health = 10
  enemy_health = 10

  arnold_l = []
  stallone_l = []

  clock = pygame.time.Clock()
  run = True 
  while run:
      clock.tick(FPS)
      for event in pygame.event.get():
         if(event.type == pygame.QUIT):
              run = False  

         key = pygame.key.get_pressed() 

         if(event.type == pygame.KEYDOWN):

            if key[pygame.K_LCTRL]  and len(arnold_l) < bullet_limit:
              bullet = pygame.Rect(terminator.x + spaceship_width - 6, terminator.y + spaceship_height//2, 9, 5)
              FIRING_SOUND.play()
              arnold_l.append(bullet)

            elif key[pygame.K_RCTRL] and len(stallone_l) < bullet_limit:
              bullet = pygame.Rect(rocky.x + (spaceship_width//2) - 17 , rocky.y + spaceship_height, 9,5)
              FIRING_SOUND.play()
              stallone_l.append(bullet)

         elif(event.type == stallone_crash):
              HIT_SOUND.play()
              enemy_health -= 1
         elif(event.type == arnold_crash):
              HIT_SOUND.play()
              player_health -= 1

         post = 5
         winner_text = ""
         if player_health <= 0:
            winner_text = "Lockheed MartinF-35 Wins!!"
            post = 0
            enemy_health = 10
            player_health = 10           

         if enemy_health <= 0:
            winner_text = "F-15EX EagleII Wins!!"
            post = 1
            enemy_health = 10
            player_health = 10

         if winner_text != "":
            draw_txt(winner_text, post)
            break         

      enemy_keybind(key, rocky)
      player_keybind(key, terminator)
      bullet_movement(arnold_l, stallone_l, terminator, rocky)
      set_border(rocky, terminator)
      update_screen(terminator, rocky, arnold_l, stallone_l, enemy_health, player_health)

  pygame.quit()

if __name__ == "__main__":
     main()

