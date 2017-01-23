import math
import pygame

black = (0,0,0)
clock = pygame.time.Clock()
                    

def process_events():
    
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            # Give the signal to quit

            return True

    

    return False

   


    



# Main program logic

def program():

    width = 640

    height = 480

    size = (width, height)

    

    # Start PyGame

    pygame.init()

    # Set the resolution

    screen = pygame.display.set_mode(size)
    # Set up the default font
    font = pygame.font.Font(None, 30)
    # Create the ship
    shipx = width * 0.5
    shipy = height * 0.5
    shipwidth = 80
    shipheight= 40
    gunswidth = 10
    weels = 30
    changeposition = 0
    gunposition = 0
    
    def ship(x,y,controlguns):
        x = int(x)
        y = int(y)
        
        positionguns = [(x,y-30),
                        (x,y), 
                        (x-70,y+20), 
                        (x+70,y+20)]
        positionguns2 = [(x,y),
                        (x,y+70), 
                        (x,y+20), 
                        (x,y+20)]

        #tekent bootje
        pygame.draw.rect(screen, black, (x-shipheight, y, shipwidth , shipheight))
        pygame.draw.line(screen, black,positionguns2[controlguns], positionguns[controlguns],gunswidth) 
        
        return positionguns[controlguns]
   
    def shoot(xy,tankx,tanky,turPos):
        fire = True
        
        startschot = list(xy)
        print("fire",xy)
        
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #print de kogels
            print(startschot[0],startschot[1])
            pygame.draw.circle(screen, (0,0,255),(startschot[0],startschot[1]),5)  
        
            startschot[0] -= 5
            
            if startschot[1] > height:
                fire = False
            pygame.display.update()    
    while not process_events():
        screen.fill((255, 255, 255))
        gun = ship(shipx,shipy,gunposition)
        
        #besturing kanon
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            changeposition = 1
            
        elif keys[pygame.K_UP]:
            changeposition = 0
        elif keys[pygame.K_RIGHT]:
            changeposition = -1
            
        elif keys[pygame.K_LEFT]:
            changeposition = 2
        
        elif keys[pygame.K_SPACE]:
            shoot(gun,shipx,shipy,gunposition)
        


       
        # Draw the cannons
        gunposition = int(changeposition)
        ship(shipx,shipy,gunposition)
    
 
        # draw cannons
        
       
        
        #move cannons

        # Flip the screen
        pygame.display.flip()

# Start the program

program()