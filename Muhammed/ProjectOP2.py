import pygame
 
# Kleuren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Lengte en breedte van grid
WIDTH = 20
HEIGHT = 20
MARGIN = 5
 
#Grid aanmaken
grid = []
for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)

## Scherm resolutie
SIZE = [505, 505]
screen = pygame.display.set_mode(SIZE)

#Grid tekenen
def drawgrid():
    for row in range(20):
            for column in range(20):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                if grid[row][column] == 2:
                    color = RED
                pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
                
def loop():

    check = False
    while not check:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                check = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
        
        screen.fill(BLACK)
        drawgrid()  
        pygame.display.flip()

pygame.init()
loop()
pygame.quit()

