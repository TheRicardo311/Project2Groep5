import pygame
import sys
import time
import random

#kleuren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255,215,0)
bright_yew = (255,255,0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

#scherm lengte / breedte
SCREENWIDTH = 1920
SCREENHEIGHT = 1050
SIZE = [SCREENWIDTH, SCREENHEIGHT]
screen = pygame.display.set_mode(SIZE)

#plaatje laden "Game cards"
offensive = pygame.image.load("gamecard.png")




#initialize pygame
pygame.init()

#KAART LIST
cards = ['FMJ Upgrade', 'Reinforced Hull', 'Backup']
p1 = ("player 1 cards: ")
p2 = ("player 2 cards: ")
#random keuzes kaarten p1 (3 kaarten)
p1rand1 = random.choice(cards)
p1rand2 = random.choice(cards)
p1rand3 = random.choice(cards)
#random keuzes kaarten p2 (3 kaarten)
p2rand1 = random.choice(cards)
p2rand2 = random.choice(cards)
p2rand3 = random.choice(cards)
font2 = pygame.font.SysFont('Arial', 17, True, False)
#random kaarten printen p1
p1k1 = font2.render(p1rand1,True,WHITE)
p1k2 = font2.render(p1rand2,True,WHITE)
p1k3 = font2.render(p1rand3,True,WHITE)
#random kaarten printen p2
p2k1 = font2.render(p2rand1,True,WHITE)
p2k2 = font2.render(p2rand2,True,WHITE)
p2k3 = font2.render(p2rand3,True,WHITE)

card3 = font2.render("<+>",True,WHITE)    #om kaarten te onderscheiden

player_one_hp = 0
player_two_hp = 0

usecard = font2.render("USE CARD",True,WHITE)



#Cards menu in game 
def cardsdraw():
    screen.blit(offensive, [1200, 300])
    font = pygame.font.SysFont('Goudy Stout', 20, True, False)
    font2 = pygame.font.SysFont('Arial', 17, True, False)
    text2 = font.render(" ---------- Cards in hand ----------",True,WHITE)
    text3 = font.render(" P1:",True,GREEN)
    text4 = font.render(" P2:",True,YELLOW)
    text5 = font.render(" __________________________________________________",True,WHITE)
    text6 = font2.render(" P1 start cards",True,WHITE)
    text7 = font2.render(" P1 -- (1 CARD)",True,WHITE)
    text8 = font2.render(" P2 start cards",True,WHITE)#1
    text9 = font2.render(" P2 -- (1 CARD)",True,WHITE)#1


    screen.blit(text2, [1310,700])
    screen.blit(text3, [1300,800])
    screen.blit(text4, [1300,900])
    screen.blit(text5, [1300,1000])
    screen.blit(text6, [1317,600])
    screen.blit(text7, [1317,500])
    screen.blit(text8, [1788,600])
    screen.blit(text9, [1788,500])


#?------
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)

    return textSurface, textSurface.get_rect()


def text_objectss(text, font):
    textSurface2 = font.render(text, True, BLACK)
    return textSurface2, textSurface2.get_rect()




#game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    


        #player 1 klikken voor start cards
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            press = pygame.mouse.get_pressed()
            if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 620 and pos[1] <= 675:
                print ("start Card #1", p1, random.choice(cards))
                print ("start Card #2", p1, random.choice(cards))
                screen.blit(p1k1, [1380, 803])
                screen.blit(card3, [1515, 803])
                screen.blit(p1k2, [1560, 803])
            else:
                if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 510 and pos[1] <= 575:
                    print ("Normal Card #1", p1, random.choice(cards))
                    screen.blit(card3, [1685, 803])
                    screen.blit(p1k3, [1740, 803])

            if press[0] == 1 and pos[0] >= 1790 and pos[0] <= 1887 and pos[1] >= 620 and pos[1] <= 675:
                print ("start Card #1", p2, random.choice(cards))
                print ("start Card #2", p2, random.choice(cards))
                screen.blit(p2k1, [1380, 903])
                screen.blit(card3, [1515, 903])
                screen.blit(p2k2, [1560, 903])
                
            else:
                if press[0] == 1 and pos[0] >= 1790 and pos[0] <= 1887 and pos[1] >= 510 and pos[1] <= 575:
                    print ("Normal Card #1", p1, random.choice(cards))
                    screen.blit(card3, [1685, 903])
                    screen.blit(p2k3, [1740, 903])

            #voor de card use

            if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 850 and pos[1] <= 900:
                    player_one_hp = + 1
                    print (player_one_hp)
            else:
                if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 850 and pos[1] <= 900:
                    player_one_hp = + 1
                    print (player_one_hp)

            
            #player 2
            if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 850 and pos[1] <= 900:
                    player_two_hp = + 0
                    
            else:
                if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 850 and pos[1] <= 900:
                    player_two_hp = + 0
                    

            

        
               
            
        

    cardsdraw()
    press = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()


    #   select cards buttons
    #   normal cards
    #   player 1 - 2 start kaarten

    if 1320 + 100 > pos[0] > 1300 and 625 + 50 > pos[1] > 625:
        pygame.draw.rect(screen, bright_green, (1320, 625, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects("NORMAL", smallText)              #BUTTON TEXT
        textRect.center = ( (1320 + (100 / 2)), (625 + (50 / 2)) )          #TEXT BUTTON POSITIE
        screen.blit(textSurf, textRect)
   
    else:
        pygame.draw.rect(screen, GREEN, (1320, 625, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects("P1 CARDS", smallText)            #BUTTON TEXT
        textRect.center = ( (1320 + (100 / 2)), (625 + (50 / 2)) )          #TEXT BUTTON POSITIE
        screen.blit(textSurf, textRect)

        
    #   select cards button
    #   normal cards
    #   player 1 - 1 kaart kiezen

    if 1320 + 100 > pos[0] > 1300 and 530 + 50 > pos[1] > 530:
        pygame.draw.rect(screen, bright_green, (1320, 530, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects("NORMAL", smallText)              #BUTTON TEXT
        textRect.center = ( (1320 + (100 / 2)), (530 + (50 / 2)) )          #TEXT BUTTON POSITIE
        screen.blit(textSurf, textRect)
               
    else:
        pygame.draw.rect(screen, GREEN, (1320, 530, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects("P1 CARDS", smallText)               #BUTTON TEXT
        textRect.center = ( (1320 + (100 / 2)), (530 + (50 / 2)) )          #TEXT BUTTON POSITIE
        screen.blit(textSurf, textRect)




    #   select cards buttons
    #   normal cards
    #   player 2 - 2 start kaarten


    if 1790 + 100 > pos[0] > 1780 and 625 + 50 > pos[1] > 625:
        pygame.draw.rect(screen, bright_yew, (1790, 625, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf2, textRect = text_objectss("NORMAL", smallText)
        textRect.center = ( (1790 + (100 / 2)), (625 + (50 / 2)) )
        screen.blit(textSurf2, textRect)
       
    else:
        pygame.draw.rect(screen, YELLOW, (1790, 625, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf2, textRect = text_objectss("P2 CARDS", smallText)
        textRect.center = ( (1790 + (100 / 2)), (625 + (50 / 2)) )
        screen.blit(textSurf2, textRect)

    #   select cards button
    #   normal cards
    #   player 2 - 1 kaart kiezen

    if 1790 + 100 > pos[0] > 1780 and 530 + 50 > pos[1] > 530:
        pygame.draw.rect(screen, bright_yew, (1790, 530, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf2, textRect = text_objectss("NORMAL", smallText)
        textRect.center = ( (1790 + (100 / 2)), (530 + (50 / 2)) )
        screen.blit(textSurf2, textRect)
       
    else:
        pygame.draw.rect(screen, YELLOW, (1790, 530, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf2, textRect = text_objectss("P2 CARDs", smallText)
        textRect.center = ( (1790 + (100 / 2)), (530 + (50 / 2)) )
        screen.blit(textSurf2, textRect)

        #special cards
    if 1560 + 100 > pos[0] > 1560 and 530 + 50 > pos[1] > 530:
        pygame.draw.rect(screen, bright_red, (1560, 530, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("CARDS", smallText)
        textRect.center = ( (1560 + (100 / 2)), (530 + (50 / 2)) )
        screen.blit(textSurf, textRect)
       
    else:
        pygame.draw.rect(screen, RED, (1560, 530, 100, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Special", smallText)
        textRect.center = ( (1560 + (100 / 2)), (530 + (50 / 2)) )
        screen.blit(textSurf, textRect)

#use cards detection
    if 1320 + 100 > pos[0] > 1320 and 780 + 50 > pos[1] > 780:
        pygame.draw.rect(screen, bright_red, (1320, 780, 100, 50))
        screen.blit(usecard, [1330, 790])
        

    else:
        pygame.draw.rect(screen, RED, (1320, 780, 100, 50))
        screen.blit(usecard, [1330, 790])
    
    


        
            

                

                
 




            
                
          
    
    time.sleep(0.03)
    pygame.display.update()



