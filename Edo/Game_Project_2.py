import pygame

pygame.init()
width = 800
height = 600
white = (255,255,255)

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Battleport")
carImage = pygame.image.load("battleship.png")


def car(boatx,boaty):
    gameDisplay.blit(carImage,(boatx,boaty))
boatx = (height * 0.1)
boaty = (width * 0.1)   

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    gameDisplay.fill(white)
    car(boatx,boaty)
    pygame.display.update()
pygame.quit()
quit()