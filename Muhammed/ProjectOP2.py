import pygame
WIDTH = 1200
HEIGHT = 800
SIZE = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(SIZE)
white = (255,255,255)
black = (0,0,0)
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def program():
    pygame.init()


    while process_events():
        screen.fill(white)
        pygame.draw.lines(screen,black,True,[(0,0),(0,800)], 7)
        pygame.draw.lines(screen,black,True,[(0,0),(1200,0)], 7)
        pygame.draw.lines(screen,black,True,[(1200,0),(1200,800)], 8)
        pygame.draw.lines(screen,black,True,[(199,660),(951,660)], 4)
        pygame.draw.lines(screen,black,True,[(199,660),(199,800)], 4)
        pygame.draw.lines(screen,black,True,[(951,660),(951,800)], 4)
        pygame.draw.lines(screen,black,True,[(199,797),(951,797)], 4)
        hor()
        ver()
        pygame.display.update()
        pygame.display.flip()

def hor():
    for y in range(650,0,-50):
        pygame.draw.lines(screen,black,True,[(200,y),(950,y)], 4)
        
def ver():
    for x in range(200,1000,50):
        pygame.draw.lines(screen,black,True,[(x,50),(x,650)],4)

def checkcor():
    if x > (650,200) and x <(600,150):
        a = a[1]
#pie
            

program()
