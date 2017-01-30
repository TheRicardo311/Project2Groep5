import pygame
import time

# Kleuren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
# Lengte en breedte van grid
WIDTH = 50
HEIGHT = 50
MARGIN = 5

## Scherm resolutie
SCREENWIDTH = 1920
SCREENHEIGHT = 1050
SIZE = [SCREENWIDTH, SCREENHEIGHT]
screen = pygame.display.set_mode(SIZE)

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
                pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column +200 + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
                

# Functions for text : Display Turn text
def text_objects(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',18)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREENWIDTH-x),(SCREENHEIGHT-y))
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

    playerchoose = int(input("Who wants to start, GREEN(1) or YELLOW(2)?"))
    if playerchoose == 1 or playerchoose == 2:
        turn = playerchoose
    else:
        playerchoose = int(input("Who wants to start, GREEN(1) or YELLOW(2)?"))

    check = False
    while not check:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                check = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = (pos[0] - 200) // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                
                
                if pos[0] < 199 and turn == 1:
                    print("Waiting to place boats from player 1(GREEN)")
                    if pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360:
                        boat = "DrieGroen"
                    elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180:
                        boat = "Vier1Groen"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190:
                        boat = "Vier2Groen"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450:
                        boat = "VijfGroen"

                if pos[0] < 199 and turn == 2:
                    print("Waiting to place boats from player 2(YELLOW)")
                    if pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760:
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
                            if row !=0:
                                print("Your ship is not placed correctly, Try again!")
                                break
                            if grid[row][column] == 1 or grid[row+1][column] == 1 or grid[row+2][column] == 1:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 1
                            grid[row+1][column] = 1
                            grid[row+2][column] = 1
                            boat = ""

                        elif boat == "Vier1Groen":
                            if row !=0:
                                print("Your ship is not placed correctly, Try again!")
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
                            if row != 0 :
                                print("Your ship is not placed correctly, Try again!")
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
                            if row !=0:
                                print("Your ship is not placed correctly, Try again!")
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
                            if row !=18:
                                print("Your ship is not placed correctly, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row-1][column] == 2 or grid[row-2][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row-1][column] = 2
                            grid[row-2][column] = 2
                            boat = ""

                        elif boat == "Vier1Geel":
                            if row !=18:
                                print("Your ship is not placed correctly, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row-1][column] == 2 or grid[row-2][column] == 2 or grid[row-3][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row-1][column] = 2
                            grid[row-2][column] = 2
                            grid[row-3][column] = 2
                            boat = ""

                        elif boat == "Vier2Geel":
                            if row !=18:
                                print("Your ship is not placed correctly, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row-1][column] == 2 or grid[row-2][column] == 2 or grid[row-3][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row-1][column] = 2
                            grid[row-2][column] = 2
                            grid[row-3][column] = 2
                            boat = ""

                        elif boat == "VijfGeel":
                            if row !=18:
                                print("Your ship is not placed correct, Try again!")
                                break
                            if grid[row][column] == 2 or grid[row-1][column] == 2 or grid[row-2][column] == 2 or grid[row-3][column] == 2 or grid[row-4][column] == 2:
                                print("Oops there is already a boat here, Try again!")
                                break
                            grid[row][column] = 2
                            grid[row-1][column] = 2
                            grid[row-2][column] = 2
                            grid[row-3][column] = 2
                            grid[row-4][column] = 2
                            boat = ""
                        break
                        
        
        screen.fill(BLACK)
        drawgrid()


        
        press = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        boat3 = pygame.draw.rect(screen,color,(130,250,40,110))

        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360 and turn == 1:
            color = BLACK
            block = pygame.draw.rect(screen,color,(130,250,40,110))
        boat4 = pygame.draw.rect(screen,color1,(130,50,40,140))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180 and turn == 1:
            color1 = BLACK
            block2 = pygame.draw.rect(screen,color,(130,50,40,140))
        boat4x = pygame.draw.rect(screen,color2,(50,50,40,140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190 and turn == 1:
            color2 = BLACK
            block3 = pygame.draw.rect(screen,color,(50,50,40,140))
        boat5 = pygame.draw.rect(screen,color3,(50,250,40,200));
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450 and turn == 1:
            color3 = BLACK
            block4 = pygame.draw.rect(screen,color,(50,250,40,200))
        boat33 = pygame.draw.rect(screen,color4,(130,650,40,110))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760 and turn == 2:
            color4 = BLACK
            block11 = pygame.draw.rect(screen,color4,(130,650,40,110))
        boat44 = pygame.draw.rect(screen,color5,(130,890,40,140));
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[1] <= 1030 and turn == 2:
            color5 = BLACK
            block22 = pygame.draw.rect(screen,color5,(130,890,40,140))
        boat44x = pygame.draw.rect(screen,color6,(50,890,40,140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[1] <= 1030 and turn == 2:
            color6 = BLACK
            block33 = pygame.draw.rect(screen,color6,(50,890,40,140))
        boat55 = pygame.draw.rect(screen,color7,(50,650,40,200))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[1] <= 850 and turn == 2:
            color7 = BLACK
            block44 = pygame.draw.rect(screen,color7,(50,650,40,200))

        endturn = pygame.draw.rect(screen,WHITE,(100,533,80,35))

        if press[0] == 1 and pos[0] >= 100 and pos[0] <= 180 and pos[1] >= 533 and pos[1] <= 568 and turn == 1:
            turn = 2
            print("GREEN turn is over")

        elif press[0] == 1 and pos[0] >= 100 and pos[0] <= 180 and pos[1] >= 533 and pos[1] <= 568 and turn == 2:
            turn = 1
            print("YELLOW turn is over")

        message_display("End Turn",1780,500)
        message_display("VS",1850,500)
        pygame.display.flip()


pygame.init()
loop()
pygame.quit()

