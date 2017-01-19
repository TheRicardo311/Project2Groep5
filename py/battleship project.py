import pygame
import psycopg2


pygame.init()

class Menu:
    def __init__(self):
        #schermgrootte
        width = 1920
        heigth = 1080
        size = (width, heigth)


        self.screen = pygame.display.set_mode(size)
        #title font
        self.fontTitle = pygame.font.Font("Capture_it_2.ttf", 150)
        #start en exit font
        self.font = pygame.font.Font("Capture_it_2.ttf", 70)



    def draw(self):
        # background
        bg = pygame.image.load("background.jpg")
        self.screen.blit(bg,(0,0))
        # title
        self.start_text = self.fontTitle.render("Battleport",
                                          1, (255, 255, 255))
        self.screen.blit(self.start_text, (260, 140))
        # start game tekst voor knop
        self.start_text = self.font.render("Start Game",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (260, 440))
        # exit game tekst voor knop
        self.exit_text = self.font.render("Exit Game",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (260, 600))
        # flip
        pygame.display.flip()

    def update(self):
        #buttons aanmaken met button functie
        button(260, 600, 450, 50, pygame.QUIT)
        button(260, 440, 500, 50, program2)

    def menu_loop(self):
        #menu functionality loop
        while not process_events():
            self.draw()
            self.update()
    def quit_menu(self):
        # afsluiten van menu
        quit()

class Game:
    def __init__(self):
        #schermgrootte
        width = 1920
        heigth = 1080
        size = (width, heigth)


        self.screen = pygame.display.set_mode(size)

    def draw(self):
        #flip
        pygame.display.flip()

    def game_loop(self):
        #game functionality loop
        while not process_events():
            self.draw()
#button functie
def button(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()

#check voor quit
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False
#STARTUP VAN MENU
def program():
    menu = Menu()
    menu.menu_loop()
#startup van game
def program2():
    game = Game()
    game.game_loop()
    menu = Menu()
    menu.quit_menu()


#aanroepen van startup functie
program()