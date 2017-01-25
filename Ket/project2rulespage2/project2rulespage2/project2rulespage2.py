import pygame
import time
 

class rules2:
    def __init__(self):
        self.run = True
        self.size = (1920, 1080)        
        self.clock = pygame.time.Clock()
        # Define some colors and BG images
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.bg = pygame.image.load("bgscherm2.jpg")
        self.ak = pygame.image.load("anker3.png")
        self.p1 = pygame.image.load("firstpagerulesgoed.png")
        
        #font text
        


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.scherm = pygame.display.set_caption("Battleport Game Rules")
        self.run = True
        
        
        

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
    
    def off_init(self):
        pygame.quit()

 # -------- Main Program Loop -----------
    def on_execute(self):
        if self.on_init() == False:
            self.run = False
        while self.run:
            # --- Main event loop
            for event in pygame.event.get():
                self.on_event(event)
 
            # --- Game logic should go here
 
            # --- Screen-clearing code goes here
 
            # Here, we clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
 
            # If you want a background image, replace this clear with blit'ing the
            # background image.
            self.font = pygame.font.SysFont('Goudy Stout', 50, True, False)
            self.text1 = self.font.render(" Battleport      Game Rules",True,self.BLACK)
            self.screen.blit(self.bg, [0,0])
            self.screen.blit(self.ak, [1920 / 2 - 55,30])
            self.screen.blit(self.p1, [365, 200])
            
            self.screen.blit(self.text1, [185,50])
 
            # --- Drawing code should go here
 
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
 
            # --- Limit to 60 frames per second
            self.clock.tick(60)
 
        # Close the window and quit.
        self.off_init()
def running():
    if __name__ == "__main__" :
        rulepage = rules2()
        rulepage.on_execute()
running()