import pygame
pygame.init()

def VictoryScreen():
    width = 1920
    height = 1080
    size = (width, height)

    pygame.display.set_mode(size)





def update_termination(self):
    button(750, 500, 50, 50, pygame.QUIT)
    button(1000, 500, 50, 50, program)
    button(1187, 270, 51, 41, program)

def victory_loop():
    while process_events == False:
        update_termination()


def button(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(mouse)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()

def button1(x, y, w, h):
    global quit_check
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(mouse)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1:
            quit_check = True
    return quit_check

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def program():
    VictoryScreen()
    victory_loop()

program()