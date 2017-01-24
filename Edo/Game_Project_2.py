import math
import pygame

black = (0,0,0)
red = (255,100,100)
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

    shipwidth = 100
    shipheight = 50
    
    gunswidth = 0
    fire_power = 1
    changeposition = 0
    gunposition = 0

    value = 0
    value1 = -5
    def ship(x,y,controlguns):
        x = int(x)
        y = int(y)
        
        positionguns = [(x,y-25),
                        (x,y+75), 
                        (x-50,y+25), 
                        (x+50,y+25)]
        positionguns2 = [(x,y),
                        (x,y+50), 
                        (x-150,y+25), 
                        (x+150,y+25)]

        #tekent bootje
        pygame.draw.rect(screen, black, (x-shipheight, y, shipwidth , shipheight))
        pygame.draw.line(screen, (255,255,255),positionguns[controlguns],positionguns2[controlguns] ,gunswidth) 
        
        return positionguns[controlguns]
    def ship2(x,y,controlguns):
        x = int(x)
        y = int(y)
        
        positionguns = [(x-1,y-1),
                        (x-1,y+50), 
                        (x-50,y+24), 
                        (x+50,y+24)]
        positionguns2 = [(x-1,y-100),
                        (x-1,y+150), 
                        (x-150,y+24), 
                        (x+150,y+24)]

        #tekent bootje
        pygame.draw.rect(screen, black, (x-shipheight, y, shipwidth , shipheight))
        pygame.draw.line(screen, (0,255,0),positionguns[controlguns],positionguns2[controlguns] ,gunswidth) 
        
        return positionguns[controlguns]
    def enemyship(x,y):
        x = int(x)
        y = int(y)
          

        #tekent bootje

        pygame.draw.rect(screen, (255,0,0), (x-shipheight, y, shipwidth , shipheight))
           
    def shoot(xy,tankx,tanky,turPos,gun_power):
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
            pygame.draw.circle(screen, (255,0,0),(startschot[0],startschot[1]),gunswidth//3)  
            
            startschot[0] += value
            startschot[1] += value1
            #Range beperken
            if startschot[0] > (shipx + 130):
                fire = False 
            if startschot[0] < (shipx - 130):
                fire = False
            if startschot[1] > (shipy + 130):
                fire = False
            if startschot[1] < (shipy - 80):
                fire = False
            pygame.display.update()    
            clock.tick(20)
            
    

    while not process_events():
        screen.fill((255, 255, 255))
        gun = ship(shipx,shipy,gunposition)
        enemyship(height*0.5, width*0.7)
        #besturing kanon
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            changeposition = 1
            value = 0
            value1 = 5
            gunswidth = 100
        elif keys[pygame.K_UP]:
            changeposition = 0
            value = 0
            value1 = -5
            gunswidth = 100 
        elif keys[pygame.K_RIGHT]:
            changeposition = -1
            value = 5
            value1 = 0
            gunswidth = 50
        elif keys[pygame.K_LEFT]:
            changeposition = 2
            value = -5
            value1 = 0
            gunswidth = 50
        elif keys[pygame.K_SPACE]:
            shoot(gun,shipx,shipy,gunposition,fire_power)
            shoot = False
        # Draw the cannons
        gunposition = int(changeposition)
        ship(shipx,shipy,gunposition)        
        ship2(shipx,shipy,gunposition)
        #move cannons
        
        # Flip the screen
        pygame.display.flip()

# Start the program

program()