

import pygame

import sys



from random import randint
#from scorescreen import scorescreen
    

redcircle=pygame.transform.scale(pygame.image.load("assets/redcircle.png"),(80,80))
bluecircle= pygame.transform.scale(pygame.image.load("assets/bluecircle.png"),(80,80))

    

redsquare= pygame.transform.scale(pygame.image.load("assets/redsquare.png"),(80,80))
bluesquare= pygame.transform.scale(pygame.image.load("assets/bluesquare.png"),(80,80))   
    
element_list=[redcircle,redsquare,bluecircle,bluesquare]

x_list=[430,680,430,680,430,680]
    
    
    
    
    
    
    
    
    

class element(object):
    
    def __init__(self):
      
        self.x=x_list[randint(0,5)]
        self.y=-10
        self.flag=0
        self.shape=0
        #self.move=1
        self.blink=0
        self.c=0
        self.playflag=0
      
        self.element=element_list[randint(0,3)]
        
        
        
        if(self.element==redcircle or self.element==bluecircle):
            self.shape=1
        else:
            self.shape=2
            
        
        
            
            
     
    def display(self,g):       
            
      
        
        element_rect=self.element.get_rect(center=(self.x+self.element.get_width()/2, \
                                             self.y+self.element.get_height()/2))
         
        car1_rect=g.leftcar.get_rect(center=(g.leftcar_x+g.leftcar.get_width()/2,\
                                          550+g.leftcar.get_height()/2))
         
         
        #Collision detection test 
         
        if(element_rect.colliderect(car1_rect)):
             
             
            # Square Collision test
            if(self.element==redsquare or self.element==redcircle):
                 
                g.collision=1
                g.hit.play(0)
                 
            #Circle collision test
            if(self.element==bluecircle or self.element==bluesquare):
                
                g.scoresound.play(0)
                g.score+=1
                g.objectlist.remove(self)
                 
        
        '''
        # Element Speed
        if(g.move==1):         
        '''
        
        self.y+=8        
        
         
        ''' 
         
        if(self.blink==1): 
             self.c+=1
             
             if(self.c>50):
                 self.c=0
             
             if(self.c<25):
                 g.gameDisplay.blit(self.element,(self.x,self.y))
         
        else:
            
            g.gameDisplay.blit(self.element,(self.x,self.y))
        '''
        
        
        
        
            
        
        #Element out of boundary
        if(self.y>=780):
            self.flag=1
            g.objectlist.remove(self)
            
        
        # INcase of miss
        if(self.element==bluecircle and self.y>=640 and self.playflag==0):
            #g.miss.play(0)
            self.playflag=1
            
            g.move=0
            #self.blink=1
            
           
         
                 
                 
                 
      
      
      
      
        

           