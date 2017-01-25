import math
import pygame

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

clock = pygame.time.Clock()
boot = pygame.image.load('boot 3.png')               

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
    shipx = width * 0.4
    shipy = height * 0.4
    ammo = 0
    shipwidth = 50
    shipheight = 100
    enemyshipx = width*0.5
    enemyshipy = height * 0.7
    gunswidth = 0
    hp = 0
    fire_power = 0
    changeposition = 0
    gunposition = 0
    x = 0
    value = 0
    value1 = -5
    def ship(x,y,controlguns):
        x = int(x)
        y = int(y)
        
        positionguns = [(x-76,y-10),
                        (x-76,y+110), 
                        (x-109,y+50), 
                        (x-40,y+50)]
        positionguns2 = [(x-76,y-115),
                        (x-76,y+125), 
                        (x-104,y+50), 
                        (x+40,y+50)]

        #tekent bootje
        screen.blit(boot,(x-99,y))
        pygame.draw.line(screen, (255,255,255),positionguns[controlguns],positionguns2[controlguns] ,50) 
        
        return positionguns[controlguns]
    
    def range(x,y,controlguns):
        x = int(x)
        y = int(y)
        
        positionguns =[(x,y),
                       (x-50,y), 
                       (x-150,y), 
                       (x,y)]
        positionguns2 = [(x,y),
                        (x-50,y), 
                        (x-150,y+99), 
                        (x,y+99)]

        #tekent bootje
        
        pygame.draw.line(screen, (0,255,0),positionguns[controlguns],positionguns2[controlguns] ,100) 
        
        return positionguns[controlguns]
    def enemyship(x,y):
        x = int(x)
        y = int(y)
          
        enemy_health = (255,0,0)
        #tekent bootje

        pygame.draw.rect(screen, enemy_health, (x-shipheight, y, shipwidth , shipheight))
           
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
            pygame.draw.circle(screen, (200,0,0),(startschot[0],startschot[1]),10)  

            startschot[0] += value
            startschot[1] += value1
            #Range beperken
            

            if startschot[0] > (shipx + 60):
                fire = False
             
            if startschot[0] < (shipx - 210):
                fire = False
        
            if startschot[1] > (shipy + 210):
                fire = False
               
            if startschot[1] < (shipy - 110):
                fire = False
       
                
             
            #colission
            

            pygame.display.update()
                
            clock.tick(20)
           
    

    while not process_events():
        hallo = 0
        
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
        elif keys[pygame.K_r]:
            ammo = 1
            
           
        elif keys[pygame.K_SPACE]:
            if ammo == 1:
    
                shoot(gun,shipx,shipy,gunposition)
                
          
        screen.fill((255, 255, 255))

        
        ship(shipx,shipy,gunposition)


        gun = ship(shipx,shipy,gunposition)
            
        # Draw the cannons
        gunposition = int(changeposition)
             
        
        #move cannons
        
        # Flip the screen
        pygame.display.flip()

# Start the program

program()