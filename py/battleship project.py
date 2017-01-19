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

        self.fontinstructions = pygame.font.Font("DroidSans.ttf", 30)



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

        self.start_text = self.fontinstructions.render("Instructions",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (1720, 16))
        # flip
        pygame.display.flip()

    def update(self):
        #buttons aanmaken met button functie
        button(260, 600, 450, 50, program_quit)
        button(260, 440, 500, 50, program2)
        button(1820, 16, 100, 50, program_instructions)

    def menu_loop(self):
        #menu functionality loop
        while not process_events():
            self.draw()
            self.update()
        quit()
    def quit_menu(self):
        # afsluiten van menu
        quit()

class Game:
    def __init__(self):
        #schermgrootte
        width = 1920
        heigth = 1080
        size = (width, heigth)
        #font
        self.font = pygame.font.Font("DroidSans.ttf", 30)


        self.screen = pygame.display.set_mode(size)

    def update(self):
        button (1720, 16, 150, 50, program_instructions)
        button(1720, 50, 140, 50, pygame.QUIT)

    def draw(self):
        self.start_text = self.font.render("Instructions",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (1720, 16))

        self.exit_text = self.font.render("Exit Game",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (1720, 50))
        #flip
        pygame.display.flip()

    def game_loop(self):
        #game functionality loop
        while not process_events():
            self.update()
            self.draw()

class Termination:
        def __init__(self):
            width = 500
            heigth = 300
            size = (width, heigth)

            self.font = pygame.font.Font("Capture_It.ttf", 30)

            self.fonttitle = pygame.font.Font("Capture_It.ttf", 30)

            self.screen = pygame.display.set_mode(size)

        def update(self):
            button(150, 150, 50, 50, pygame.QUIT)
            button(300, 150, 50, 50, program)


        def draw(self):
            bg = pygame.image.load("termination_background.PNG")
            self.screen.blit(bg, (0, 0))

            self.exit_text = self.font.render("Yes",
                                              1, (255, 255, 255))
            self.screen.blit(self.exit_text, (150, 150))

            self.exit_text = self.font.render("No",
                                              1, (255, 255, 255))
            self.screen.blit(self.exit_text, (300, 150))

            self.exit_text = self.fonttitle.render("Are you sure you want to quit?",
                                              1, (255, 255, 255))
            self.screen.blit(self.exit_text, (11, 70))

            pygame.display.flip()


        def termination_loop(self):
            while not process_events():
                self.update()
                self.draw()

        def termination_quit(self):
            quit()



#button functie
def button(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(mouse)
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
#startup termination screen
def program_quit():
    termination = Termination()
    termination.termination_loop()
    menu = Menu()
    menu.quit_menu()



def program_instructions():
    return 0


#aanroepen van startup functie
program()