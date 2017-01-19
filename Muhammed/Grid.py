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
        pygame.draw.lines(screen,black,True,[(1000,660),(1000,800)], 4)
        pygame.draw.lines(screen,black,True,[(199,797),(1000,797)], 4)

        hor()
        ver()
        pygame.display.update()
        pygame.display.flip()

def hor():
    for y in range(660,0,-33):
        pygame.draw.lines(screen,black,True,[(200,y),(1000,y)], 4)
        
def ver():
    for x in range(200,1010,40):
        pygame.draw.lines(screen,black,True,[(x,0),(x,660)],4)


program()
