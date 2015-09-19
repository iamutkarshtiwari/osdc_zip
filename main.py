


import pygame
import sys

from elements import *
from welcomescreen import *
from scorescreen import *



class game:
    
    
    def __init__(self):
        self.start=1
        
    def initialize(self):

        
        
        self.score=0
        self.left=True
        self.right=True
        
        self.leftclick=self.rightclick=0
       
        self.leftmove=0
        self.rightmove=0
        self.move=1
        
        
        self.left_angle = self.right_angle = 0
        
        
        
        self.leftcar_x=440
        #510
        
        
        #self.rightcar_x=760
        #600
        
        self.speed=15
        
        self.anglespeed=3
        self.anglelimit=30
        
        
        
        self.objectlist=[]
        
        
        self.i=0
        
        
        #self.objectlist.append(element())
        
        self.lastright=self.lastleft=0
        self.timer=0
        
        self.collision=0
        
        
        #self.start=1
        
        
        
        
        
        
        
        
        
        

        pygame.init()
        self.sound=True
        
        
        #self.gameDisplay=pygame.display.get_surface()
        
            
        self.gameDisplay = pygame.display.set_mode((1366,768))
 
        
        
        
        self.font_path = "fonts/sans.ttf"
        self.font_size = 55
        self.font1= pygame.font.Font(self.font_path,self.font_size)
        self.font2=pygame.font.Font("fonts/sans.ttf",30)
        self.font3=pygame.font.Font("fonts/gobold-light.ttf",40)
        self.font4=pygame.font.Font("fonts/sans.ttf",23)
        
        
        
        

        # Load the images for elements
        #load_elements_images()
        
        self.background =  pygame.image.load("assets/background.png").convert()
                                                 
        self.background = pygame.transform.scale(self.background, (491,768))                                   
                                             
                                             
        
        self.leftcar = pygame.image.load("assets/bluecar.png")
                                              
        
        self.leftcar = pygame.transform.scale(self.leftcar,(45+20,90+30))
        
        
        
        
        #Music load
        
        self.hit=pygame.mixer.Sound("assets/sounds/hit.ogg")
        self.miss=pygame.mixer.Sound("assets/sounds/miss.ogg")
        self.music=pygame.mixer.Sound("assets/sounds/music.ogg")
        self.scoresound=pygame.mixer.Sound("assets/sounds/score.ogg")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def make(self):

        self.initialize()
        
        # Variable Initialization
        black=(0,0,0)
        white=(255,255,255)
        clock=pygame.time.Clock()
            
        crashed=False   
        #self.music.play(-1)

        
        
        # GAME LOOP BEGINS !!!
        
        while not crashed:
            
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    crashed=True
                
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            
            
                
                
            
            
            #self.gameDisplay.fill(white)
            #self.gameDisplay.blit(self.background,(350,0))
            
            
            
            # Car Blitting
            
            
            
            
            
            
            
            
            # Obstacles placement
            
            
            
            
            
            
            # Elements display
            
              
                
                
                
                
            # Score blitting
            
            
            
                
            
            #Obtacle blinker
            '''
            if(self.move==0):
                self.timer+=1
                
                if(self.timer>=125):
                    self.collision=1
            '''    
            
            
            
                
            if(self.collision==1):
                
                sys.exit()
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # Car Movements
            
            
            
            
            
            
            #For left car updation
            
                        
            
                
                
                
            
            
            
            
            # Keyboard Input
            
            
            
            
            
            
            
            
          
            
            # BLACK RECTANGLES DISPLAY
                      
            
            
            
            
            
            
            
            
            
            pygame.display.update()
            clock.tick(60)
     
            if crashed:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
       
        # Just a window exception check condition

        event1=pygame.event.get()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed:
            pygame.quit()
            sys.exit()
            

if __name__ == "__main__":
    g = game()
    g.make()         

            
