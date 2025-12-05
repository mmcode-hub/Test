import pygame,sys,random
pygame.init()
# window resolutions
size=[500,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("PADDLE GAME")
#Declaring colour variables
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
#Declaring paddle variables
paddle_1_size=[0,0,25,500]
paddle_2_size=[475,0,25,500]
paddle_rect_1=[0,250,25,75]
paddle_rect_2=[475,250,25,75]
# ball variables declaring
radious=10
circle_x=random.randint(25+radious,450-radious)
circle_y=random.randint(0+radious,500-radious)


#Declaring wanted variables
#Tesing Github Connection
FPS=60

direction='up'
movement='down'

clock=pygame.time.Clock()

a=random.randint(0,3)
print(a)
way=random.randint(0,3)
#Main Loop
while True:
    #img=pygame.image.load('flippyboard.png')
    #screen.blit(img,(0,0))
    # Draw the paddle
    pygame.draw.rect(screen,RED,(paddle_1_size))
    pygame.draw.rect(screen,RED,(paddle_2_size))
    pygame.draw.rect(screen,BLACK,(paddle_rect_1))
    pygame.draw.rect(screen,BLACK,(paddle_rect_2))
    
    # paddle_2_moveing properties
    if direction=='up':
        paddle_rect_1[1]-=5
        if paddle_rect_1[1]==0:
            direction='down'
    elif direction=='down':
        paddle_rect_1[1]+=5
        if paddle_rect_1[1]==425:
            direction='up'
    # paddle_2_moveing properties        
    if movement=='down':
        paddle_rect_2[1]+=5
        if paddle_rect_2[1]==425:
            movement='up'
    elif movement=='up':
        paddle_rect_2[1]-=5
        if paddle_rect_2[1]==0:
           movement='down'        

    #Ball properties
    pygame.draw.circle(screen,(WHITE),(circle_x,circle_y),radious,0)
    
    #Ball movemnt
    if  (a==0):
        root='right'
    elif a==1:
        root='left'
    elif a==2:
        root='up'
    elif a==3:
        root='down'

        
    if root=='right' and circle_x<=460:
          circle_x+=5
          # declaring the next root
          if way==0:
              root='up'
          elif way==1:
              root='right'
          elif way==2:
              root='down'
          elif way==3:
              root='left'

              
              
          
    if root=='left' and circle_x>=35:
          circle_x-=5
          # declaring the next root
          if way==0:
              root='up'
          elif way==1:
              root='right'
          elif way==2:
              root='down'
          elif way==3:
              root='left'
  
    
    if root=='up' and circle_y>=10:
          circle_y-=5
          # declaring the next root
          if way==0:
              root='up'
          elif way==1:
              root='right'
          elif way==2:
              root='down'
          elif way==3:
              root='left'
   
    if root=='down' and circle_y<=490:
          circle_y+=5
          # declaring the next root
          if way==0:
              root='up'
          elif way==1:
              root='right'
          elif way==2:
              root='down'
          elif way==3:
              root='left'
            
            
    #Quit event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Update & Pixes
    clock.tick(FPS)        
    pygame.display.update()  
