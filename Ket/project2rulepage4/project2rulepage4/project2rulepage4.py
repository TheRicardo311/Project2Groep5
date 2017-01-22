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
        self.s1 = pygame.image.load("shipmap1.png")
        self.s2 = pygame.image.load("shipmap2.png")
        self.s3 = pygame.image.load("shipmap3.png")
        self.s4 = pygame.image.load("shiptext.png")
        
        
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
            self.font = pygame.font.SysFont('Calibri', 30, True, False)
            self.text2 = self.font.render(" Range gevisualiseerd:",True,self.BLACK)
            self.screen.blit(self.bg, [0,0])
            self.screen.blit(self.ak, [1920 / 2 - 55,30])
            self.screen.blit(self.s1, [0, 200])
            self.screen.blit(self.s2, [550, 200])
            self.screen.blit(self.s3, [1170, 190])
            self.screen.blit(self.s4, [70, 600])
            
            self.screen.blit(self.text1, [185,50])
            self.screen.blit(self.text2, [230,700])
 
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