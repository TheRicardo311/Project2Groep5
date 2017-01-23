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

    height = 640

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
    width1 = 100
    height1 = 100
    value = 0
    value1 = 0
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
        pygame.image.load('boat.png'),
        pygame.draw.line(screen, black,positionguns2[controlguns], positionguns[controlguns],gunswidth) 
        
        return positionguns[controlguns]
   
    def shoot(xy,tankx,tanky,turPos):
        fire = True
        hallo = (pygame.key.get_pressed()[pygame.K_RIGHT])
        hallo1 = (pygame.key.get_pressed()[pygame.K_LEFT])
        doei =  (pygame.key.get_pressed()[pygame.K_UP])
        doei1 = (pygame.key.get_pressed()[pygame.K_DOWN])
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
            
            startschot[0] += value
            startschot[1] += value1
            
            if startschot[0] > 640:
                fire = False 
            if startschot[0] < 0:
                fire = False
            if startschot[1] > 640:
                fire = False
            if startschot[1] < 0:
                fire = False
            pygame.display.update()    
    while not process_events():
        screen.fill((255, 255, 255))
        gun = ship(shipx,shipy,gunposition)
     
        #besturing kanon
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            changeposition = 1
            value = 0
            value1 = 5

        elif keys[pygame.K_UP]:
            changeposition = 0
            value = 0
            value1 = -5
   
        elif keys[pygame.K_RIGHT]:
            changeposition = -1
            value = 5
            value1 = 0
      
        elif keys[pygame.K_LEFT]:
            changeposition = 2
            value = -5
            value1 = 0
  
        elif keys[pygame.K_SPACE]:
            shoot(gun,shipx,shipy,gunposition)
        
        # Draw the cannons
        gunposition = int(changeposition)
        ship(shipx,shipy,gunposition)        
        
        #move cannons
        clock.tick(10)
        # Flip the screen
        pygame.display.flip()

# Start the program

program()