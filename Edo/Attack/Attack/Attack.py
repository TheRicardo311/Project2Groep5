import math
import pygame

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
lightred = (255,103,246)
clock = pygame.time.Clock()
           

def process_events():
    
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            # Give the signal to quit

            return True

    

    return False
# Main program logic

def program():

    width = 800

    height = 900

    size = (width, height)

    

    # Start PyGame

    pygame.init()

    # Set the resolution
    
    screen = pygame.display.set_mode(size)
    # Set up the default font
    font = pygame.font.Font(None, 30)
    # Create the ship
    shipx = width * 0.5
    shipy = height * 0.35
    ammo = 0
    shipwidth = 50
    shipheight = 150
    ship2width = 50
    ship2height = 200
    ship3width = 50
    ship3height = 250
    enemyshipx = width*0.7
    enemyshipy = height * 0.35
    gunswidth = 0
    bootje = pygame.image.load("boot 3.png")
    changeposition = 0
    gunposition = 0
    value = 0
    value1 = -5
    ammo = True
    def ship(x,y,controlguns):
        x = int(x)
        y = int(y)
        #Positie startshoten
        positionguns = [(x-27,y-60),
                        (x-27,y+110), 
                        (x-55,y+25), 
                        (x+5,y+25)]
        positionguns2 = [(x-27,y-225),
                        (x-27,y+275), 
                        (x-225,y+25), 
                        (x+175,y+25)]

        #tekent bootje / kogel
        pygame.draw.rect(screen, green, (x-50, y-50, shipwidth , shipheight))
        pygame.draw.line(screen, (0,0,0),positionguns[controlguns],positionguns2[controlguns] ,shipwidth) 
        
        return positionguns[controlguns]
    
    def ship2(x,y,controlguns):
        x = int(x)
        y = int(y)
        #Positie startshoten
        positionguns = [(x-27,y-60),
                        (x-27,y+160), 
                        (x-55,y+50), 
                        (x+5,y+50)]
        positionguns2 = [(x-27,y-275),
                        (x-27,y+375), 
                        (x-275,y+50), 
                        (x+225,y+50)]

        #tekent bootje / kogel
        pygame.draw.rect(screen, green, (x-50, y-50, ship2width , ship2height))
        pygame.draw.line(screen, (0,0,0),positionguns[controlguns],positionguns2[controlguns] ,shipwidth) 
        
        return positionguns[controlguns]
    def ship3(x,y,controlguns):
        x = int(x)
        y = int(y)
        #Positie startshoten
        positionguns = [(x-27,y-60),
                        (x-27,y+210), 
                        (x-55,y+75), 
                        (x+5,y+75)]
        positionguns2 = [(x-27,y-325),
                        (x-27,y+425), 
                        (x-300,y+75), 
                        (x+250,y+75)]

        #tekent bootje / kogel
        pygame.draw.rect(screen, green, (x-50, y-50, ship3width , ship3height))
        pygame.draw.line(screen, (0,0,0),positionguns[controlguns],positionguns2[controlguns] ,shipwidth) 
        
        return positionguns[controlguns]    

    def enemyship(x,y):
        x = int(x)
        y = int(y)
          
    
        #tekent bootje

        pygame.draw.rect(screen, red, (x, y-50, ship2width , ship2height))
           
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
            if startschot[0] > (enemyshipx):
                print("HIT",enemyshipx)
                fire = False

            if startschot[0] > (shipx + 155):
                fire = False
             
            if startschot[0] < (shipx - 205):
                fire = False
        
            if startschot[1] > (shipy + 260):
                fire = False
               
            if startschot[1] < (shipy - 210):
                fire = False
       
                
             
            #colission
            

            pygame.display.update()
                
            clock.tick(20)
               
    def shoot2(xy,tankx,tanky,turPos):
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
            
            if startschot[0] > (enemyshipx):
                print("HIT",enemyshipx)
                fire = False
            if startschot[0] > (shipx + 205):
                print("Missed")
                fire = False
                 
            if startschot[0] < (shipx - 255):
                print("Missed")
                fire = False
        
            if startschot[1] > (shipy + 360):
                print("Missed")
                fire = False
               
            if startschot[1] < (shipy - 260):
                print("Missed")
                fire = False
                      
            # tekent cirkels op elkaar
            pygame.display.update()
                
            clock.tick(20)

    def shoot3(xy,tankx,tanky,turPos):
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
            pygame.draw.circle(screen, (0,0,255),(startschot[0],startschot[1]),10)  
            if ammo == True:
                startschot[0] += value
                startschot[1] += value1
                #Range beperken
            
                if startschot[0] > (enemyshipx):
                    print("HIT",enemyshipx)
                    fire = False
                if startschot[0] > (shipx + 255):
                    fire = False
                    ammo = False
                if startschot[0] < (shipx - 305):
                    fire = False
                    ammo = False
                if startschot[1] > (shipy + 410):
                    fire = False
                    ammo = False
                if startschot[1] < (shipy - 310):
                    fire = False
                    ammo = False  
            # tekent cirkels op elkaar
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
        
           
        elif keys[pygame.K_SPACE]:
            shoot2(gun,shipx,shipy,gunposition)
            
                
        screen.fill((255, 255, 255))
        
   
        ship2(shipx,shipy,gunposition)
        
        gun = ship2(shipx,shipy,gunposition)
        enemyship(enemyshipx,enemyshipy)    
        # Draw the cannons
        gunposition = int(changeposition)
             
        
        #move cannons
        
        # Flip the screen
        pygame.display.flip()

# Start the program

program()



##defense ranges (x,y-25),
#                        (x,y+75), 
#                        (x-50,y+25), 
#                        (x+50,y+25)]
#        positionguns2 = [(x,y),
#                        (x,y+50), 
#                        (x-150,y+25), 
#                        (x+150,y+25)]
#positionguns = [(x-1,y-1),
#                        (x-1,y+50), 
#                        (x-50,y+24), 
#                        (x+50,y+24)]
#        positionguns2 = [(x-1,y-100),
#                        (x-1,y+150), 
#                        (x-150,y+24), 
#                        (x+150,y+24)]