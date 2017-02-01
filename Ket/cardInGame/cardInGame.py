import pygame
import time
import random


# Kleuren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255,255,0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# Lengte en breedte van grid
WIDTH = 50
HEIGHT = 50
MARGIN = 5

## Scherm resolutie
SCREENWIDTH = 1920
SCREENHEIGHT = 1050
SIZE = [SCREENWIDTH, SCREENHEIGHT]
screen = pygame.display.set_mode(SIZE)

#kaarten
offensive = pygame.image.load("gamecard.png")



#Grid aanmaken
grid = []
for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)


#Grid tekenen
def drawgrid():
    for row in range(20):
            for column in range(20):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                elif grid[row][column] == 2:
                    color = YELLOW
                pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column+200 + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
 



#kaart menu
def cardsdraw():
    screen.blit(offensive, [1200, 300])
    font = pygame.font.SysFont('Goudy Stout', 20, True, False)
    text1 = font.render(" Pick Up A Card",True,WHITE)
    text2 = font.render(" ---------- Cards in hand ----------",True,WHITE)
    text3 = font.render(" P1:",True,GREEN)
    text4 = font.render(" P2:",True,YELLOW)
    text5 = font.render(" __________________________________________________",True,WHITE)

    screen.blit(text1, [1428,450])
    screen.blit(text2, [1310,700])
    screen.blit(text3, [1300,800])
    screen.blit(text4, [1300,900])
    screen.blit(text5, [1300,1000])

#normalcard
normalCard = ['FMJ Upgrade', 'Riffling', 'Advanced Riffling', 'Naval Mine', 'EMP Upgrade', 'Reinforced Hull', 'Sonar', 'Smoke Screen', 'Sabotage', 'Backup', 'Extra Fuel', 'Rally', 'Adrenaline Rush']
def normalcard():
    global normalCard
    p1 = random.choice(normalCard)
    font = pygame.font.SysFont('Calibri', 20, True, False)
    card1 = font.render(p1,True,WHITE)

    screen.blit(card1, [1380, 805])

    print (p1)



# Functions for text : Display Turn text
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREENWIDTH-1810),(SCREENHEIGHT-500))
    screen.blit(TextSurf, TextRect)


                    
def loop():
    color = GREEN
    color1 = GREEN
    color2 = GREEN
    color3 = GREEN
    color4 = YELLOW
    color5 = YELLOW
    color6 = YELLOW
    color7 = YELLOW
    boat = ""
    check = False
    pause = False
    
    #card test 1.0
    font = pygame.font.SysFont('Goudy Stout', 20, True, False)
    card1 = font.render("card test p1",True,WHITE)
    card2 = font.render("card test p2",True,WHITE)

    cards = ['FMJ Upgrade', 'Reinforced Hull', 'Backup']
    p1 = ("player 1 cards: ")
    p2 = ("player 2 cards: ")

    
    while not check:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                check = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = (pos[0] - 200) // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)



            

            
                



                if pos[0] < 199:
                    if pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360:
                        boat = "DrieGroen"
                    elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180:
                        boat = "Vier1Groen"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190:
                        boat = "Vier2Groen"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450:
                        boat = "VijfGroen"
                    elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760:
                        boat = "DrieGeel"
                    elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[1] <= 1030:
                        boat = "Vier1Geel"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[1] <= 1030:
                        boat = "Vier2Geel"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[1] <= 850:
                        boat = "VijfGeel"

                if pos[0] > 199  and pos[0] < 1300:
                        print("Click ", pos, "Grid coordinates: ", row, column)
                        if boat == "DrieGroen":
                            if row >=17:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 1 or grid[row+1][column] == 1 or grid[row+2][column] == 1:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 1
                            grid[row+1][column] = 1
                            grid[row+2][column] = 1
                            boat = ""

                        elif boat == "Vier1Groen":
                            if row >=16:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 1 or grid[row+1][column] == 1 or grid[row+2][column] == 1 or grid[row+3][column] == 1:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 1
                            grid[row+1][column] = 1
                            grid[row+2][column] = 1
                            grid[row+3][column] = 1
                            boat = ""

                        elif boat == "Vier2Groen":
                            if row >=16:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 1 or grid[row+1][column] == 1 or grid[row+2][column] == 1 or grid[row+3][column] == 1:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 1
                            grid[row+1][column] = 1
                            grid[row+2][column] = 1
                            grid[row+3][column] = 1
                            boat = ""

                        elif boat == "VijfGroen":
                            if row >=15:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 1 or grid[row+1][column] == 1 or grid[row+2][column] == 1 or grid[row+3][column] == 1 or grid[row+4][column] == 1:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 1
                            grid[row+1][column] = 1
                            grid[row+2][column] = 1
                            grid[row+3][column] = 1
                            grid[row+4][column] = 1
                            boat = ""

                        elif boat == "DrieGeel":
                            if row >=17:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row+1][column] == 2 or grid[row+2][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row+1][column] = 2
                            grid[row+2][column] = 2
                            boat = ""

                        elif boat == "Vier1Geel":
                            if row >=16:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row+1][column] == 2 or grid[row+2][column] == 2 or grid[row+3][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row+1][column] = 2
                            grid[row+2][column] = 2
                            grid[row+3][column] = 2
                            boat = ""

                        elif boat == "Vier2Geel":
                            if row >=16:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row+1][column] == 2 or grid[row+2][column] == 2 or grid[row+3][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row+1][column] = 2
                            grid[row+2][column] = 2
                            grid[row+3][column] = 2
                            boat = ""

                        elif boat == "VijfGeel":
                            if row >=15:
                                print("Oops you went out the playfield, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row+1][column] == 2 or grid[row+2][column] == 2 or grid[row+3][column] == 2 or grid[row+4][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row+1][column] = 2
                            grid[row+2][column] = 2
                            grid[row+3][column] = 2
                            grid[row+4][column] = 2
                            boat = ""
                        break
                        
        
        screen.fill(BLACK)
        drawgrid()
        
        
        
        
        

        press = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()


        #select cards buttons

        #normal cards
        if 1320 + 100 > pos[0] > 1300 and 625 + 50 > pos[1] > 625:
            pygame.draw.rect(screen, bright_green, (1320, 625, 100, 50))
            
            
       
        else:
            pygame.draw.rect(screen, GREEN, (1320, 625, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Normal", smallText)
        textRect.center = ( (1320 + (100 / 2)), (625 + (50 / 2)) )
        screen.blit(textSurf, textRect)

        #special cards
        if 1790 + 100 > pos[0] > 1780 and 625 + 50 > pos[1] > 625:
            pygame.draw.rect(screen, bright_red, (1790, 625, 100, 50))
       
        else:
            pygame.draw.rect(screen, RED, (1790, 625, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Special", smallText)
        textRect.center = ( (1790 + (100 / 2)), (625 + (50 / 2)) )
        screen.blit(textSurf, textRect)
        #print (pos)

        if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 620 and pos[1] <= 675:
            if pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 620 and pos[1] <= 675:
                print ("start Card #1", p1, random.choice(cards))
                print ("start Card #2", p1, random.choice(cards))
                screen.blit(card1, [150, 100])

        def choosenormal():
            if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 620 and pos[1] <= 675:
                mouseclick()



        def chooseSpec():
            if press[0] == 1 and pos[0] >= 1790 and pos[0] <= 1880 and pos[1] >= 620 and pos[1] <= 675:
                font = pygame.font.SysFont('Arial', 20, True, False)
                K2 = font.render("Special Choice",True,WHITE)
                screen.blit(K2, [1300, 150])
                
                specialCard = ['Repair', 'Flak Armor', 'Far Sight', 'Aluminium Bull', 'Jack Sparrow']
                from random import randrange
                random_index = randrange(0,len(specialCard))
                print (specialCard[random_index])
        

                
                
            
                
        


        boat3 = pygame.draw.rect(screen,color,(130,250,40,110))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360:
            color = BLACK
            block = pygame.draw.rect(screen,color,(130,250,40,110))
        boat4 = pygame.draw.rect(screen,color1,(130,50,40,140))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180:
            color1 = BLACK
            block2 = pygame.draw.rect(screen,color,(130,50,40,140))
        boat4x = pygame.draw.rect(screen,color2,(50,50,40,140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190:
            color2 = BLACK
            block3 = pygame.draw.rect(screen,color,(50,50,40,140))
        boat5 = pygame.draw.rect(screen,color3,(50,250,40,200));
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450:
            color3 = BLACK
            block4 = pygame.draw.rect(screen,color,(50,250,40,200))
        
        
        boat33 = pygame.draw.rect(screen,color4,(130,650,40,110))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760:
            color4 = BLACK
            block11 = pygame.draw.rect(screen,color4,(130,650,40,110))
        boat44 = pygame.draw.rect(screen,color5,(130,890,40,140));
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[1] <= 1030:
            color5 = BLACK
            block22 = pygame.draw.rect(screen,color5,(130,890,40,140))
        boat44x = pygame.draw.rect(screen,color6,(50,890,40,140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[1] <= 1030:
            color6 = BLACK
            block33 = pygame.draw.rect(screen,color6,(50,890,40,140))
        boat55 = pygame.draw.rect(screen,color7,(50,650,40,200))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[1] <= 850:
            color7 = BLACK
            block44 = pygame.draw.rect(screen,color7,(50,650,40,200))



        

            

        
        message_display("VS")
        cardsdraw()

        
        

        pygame.display.flip()
        
        


pygame.init()
loop()
pygame.quit()





