import pygame
import random
import psycopg2
import time

bgrandom = random.randint(0, 1)
quit_check = False
pygame.init()

white = (255,255,255)
black = (0,0,0)

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
        self.font = pygame.font.Font("DroidSans.ttf", 25)

        self.fontinstructions = pygame.font.Font("DroidSans.ttf", 30)

        self.fontsaus = pygame.font.Font("Capture_It.ttf", 30)

        self.fonttitle = pygame.font.Font("Capture_It.ttf", 30)

        self.titlefont = pygame.font.Font("Capture_it.ttf", 70)

        self.font1 = pygame.font.Font("Capture_it.ttf", 70)




    def draw(self):
        # background
        global bgrandom
        if bgrandom == 1:
            bg = pygame.image.load("background.jpg")
        else:
            bg = pygame.image.load("Background2.jpg")
        self.screen.blit(bg,(0,0))
        # title
        self.start_text = self.fontTitle.render("Battleport",
                                          1, (255, 255, 255))
        self.screen.blit(self.start_text, (260, 140))
        # start game tekst voor knop
        self.start_text = self.font1.render("Start Game",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (260, 440))
        # exit game tekst voor knop
        self.exit_text = self.font1.render("Exit Game",
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
        button(1720, 16, 165, 50, program_rules1)

    def update_termination(self):
        button(750, 500, 50, 50, pygame.QUIT)
        button(1000, 500, 50, 50, program)
        button(1187, 270, 51, 41, program)

    def draw_termination(self):
        global bgrandom
        if bgrandom == 1:
            bg = pygame.image.load("background.jpg")
        else:
            bg = pygame.image.load("Background2.jpg")
        self.screen.blit(bg, (0, 0))
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
        bg = pygame.image.load("termination_background.PNG")
        self.screen.blit(bg, (580, 270))

        self.exit_text = self.fontsaus.render("Yes",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (750, 500))

        self.exit_text = self.fontsaus.render("No",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (1000, 500))

        self.exit_text = self.fonttitle.render("Are you sure you want to quit?",
                                               1, (255, 255, 255))
        self.screen.blit(self.exit_text, (670, 350))

        pygame.display.flip()

    def update_rules1(self):
        button1(1720, 100, 50, 50)

    def draw_rules1(self):
        bg = pygame.image.load("rules_background.jpg")
        self.screen.blit(bg, (0, 0))

        self.start_text = self.font.render("Quit",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (1720, 100))

        self.start_text = self.titlefont.render("Rules",
                                                1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 100))

        self.start_text = self.font.render(
            "-Om te beginnen trekt elke speler om de beurt 1 kaart, totdat ze 2 kaarten hebben.",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 200))

        self.start_text = self.font.render(
            "-Daarna plaatst elke speler om de beurt zijn/haar schepen in het speelveld, met de achterkant van de schepen tegen de beginlijn aan.",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 250))

        self.start_text = self.font.render("-Wanneer je aan beurt bent mag je al je schepen verplaatsen",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 300))

        self.start_text = self.font.render(
            "-Ook kun je de positie van je schepen veranderen, wanneer je dit doet telt dat als 1 stap",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 350))

        self.start_text = self.font.render(
            "-Wanneer een schip in zijn aanvalspositie staat (verticaal) heeft het schip zijn standaard aanval bereik.",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 400))

        self.start_text = self.font.render(
            "-Wanneer een schip in zijn verdedigingspositite staat (horizontaal) mag deze niet verplaatst worden. ",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 430))

        self.start_text = self.font.render(
            "-Spelers mogen 2 keer per beurt aanvallen. aanvallen kan alleen wanneer een schip van de tegenstander in het bereik staat van een ",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 480))

        self.start_text = self.font.render("-een van jouw schepen. Maar per boot mag je maar 1 keer aanvallen.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 510))

        self.start_text = self.font.render("-Aan het begin van elke beurt trekt de speler aan beurt een kaart.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 560))

        self.start_text = self.font.render(
            "-Wanneer er een valstrik-kaart wordt getrokken moet deze kaart geplaatst worden op het speelveld in de bijbehorende trapveld.",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 610))

        self.start_text = self.font.render(
            "-Valstrik-kaarten mogen altijd geactiveerd worden, ook wanneer de tegenstander aan de beurt is.",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 640))

        self.start_text = self.font.render(
            "-Een speler mag maximaal 6 kaarten in z’n handen hebben, wanneer een speler z’n 7de kaart trekt moet hij deze in de “weggooistapel stoppen",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 690))

        self.start_text = self.font.render("-De spelers mogen per beurt maar 2 kaarten gebruiken ",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 740))

        self.start_text = self.font.render(
            "-Wanneer alle kaarten in de normale stapel zijn gebruikt wordt de weggooistapel geschud en dient deze te worden gebruikt als de nieuwe “normale” stapel ",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 790))

        self.start_text = self.font.render(
            "-Wanneer een speler de overkant haalt met een van z’n schepen mag hij een speciale kaart trekken",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 840))

        self.start_text = self.font.render(
            "-Wanneer het een perk-kaart is wordt de kaart toegewezen aan het schip die de overkant heeft gehaald. De effect van de kaart blijft de rest van het spel actief.",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 870))

        self.start_text = self.font.render(
            "-Wanneer een schip wordt vernietigd wordt dezelfde schip een obstakel. ander schepen kunnen niet door obstakels varen. ",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 920))

        self.start_text = self.font.render(
            "-een speler wint nadat hij/zij alle schepen van de tegenstander heeft vernietigd.",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 970))

        pygame.display.flip()

    def termination_loop(self):
        while not process_events():
            self.update_termination()
            self.draw_termination()

    def menu_loop(self):
        #menu functionality loop
        while not process_events():
            self.draw()
            self.update()
        quit()


    def rules_loop1(self):
        global quit_check
        quit_check = False
        while not process_events():
            self.update_rules1()
            self.draw_rules1()
            if quit_check == True:
                break

    def quit_menu(self):
        # afsluiten van menu
        quit()

class Game:
    def __init__(self):
        #schermgrootte
        width = 1920
        height = 1080
        size = (width, height)
        #font
        self.font = pygame.font.Font("DroidSans.ttf", 25)

        self.titlefont = pygame.font.Font("Capture_it.ttf", 70)


        self.screen = pygame.display.set_mode(size)

    def update(self):
        global quit_check
        quit_check = False
        button(1720, 16, 150, 30, program_rules)
        button(1720, 50, 140, 30, pygame.QUIT)
        button(1720, 84, 200, 30, program)


    def draw(self):
        self.screen.fill((0,0,0))
        self.start_text = self.font.render("Instructions",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (1700, 16))

        self.exit_text = self.font.render("Back to main menu",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (1700, 84))

        self.exit_text = self.font.render("Exit Game",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (1700, 50))



        #flip
        pygame.display.flip()

    def update_rules(self):
        button1(1720, 100, 50, 50)


    def draw_rules(self):
        bg = pygame.image.load("rules_background.jpg")
        self.screen.blit(bg, (0,0))

        self.start_text = self.font.render("Quit",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (1720, 100))

        self.start_text = self.titlefont.render("Rules",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 100))

        self.start_text = self.font.render("-Om te beginnen trekt elke speler om de beurt 1 kaart, totdat ze 2 kaarten hebben.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 200))

        self.start_text = self.font.render("-Daarna plaatst elke speler om de beurt zijn/haar schepen in het speelveld, met de achterkant van de schepen tegen de beginlijn aan.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 250))

        self.start_text = self.font.render("-Wanneer je aan beurt bent mag je al je schepen verplaatsen",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 300))

        self.start_text = self.font.render("-Ook kun je de positie van je schepen veranderen, wanneer je dit doet telt dat als 1 stap",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 350))

        self.start_text = self.font.render("-Wanneer een schip in zijn aanvalspositie staat (verticaal) heeft het schip zijn standaard aanval bereik.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 400))

        self.start_text = self.font.render("-Wanneer een schip in zijn verdedigingspositite staat (horizontaal) mag deze niet verplaatst worden. ",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 430))

        self.start_text = self.font.render("-Spelers mogen 2 keer per beurt aanvallen. aanvallen kan alleen wanneer een schip van de tegenstander in het bereik staat van een ",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 480))

        self.start_text = self.font.render("-een van jouw schepen. Maar per boot mag je maar 1 keer aanvallen.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 510))

        self.start_text = self.font.render("-Aan het begin van elke beurt trekt de speler aan beurt een kaart..",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 560))

        self.start_text = self.font.render("-Wanneer er een valstrik-kaart wordt getrokken moet deze kaart geplaatst worden op het speelveld in de bijbehorende trapveld.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 610))

        self.start_text = self.font.render("-Valstrik-kaarten mogen altijd geactiveerd worden, ook wanneer de tegenstander aan de beurt is.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (150, 640))

        self.start_text = self.font.render("-Een speler mag maximaal 6 kaarten in z’n handen hebben, wanneer een speler z’n 7de kaart trekt moet hij deze in de “weggooistapel stoppen",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 690))

        self.start_text = self.font.render("-De spelers mogen per beurt maar 2 kaarten gebruiken ",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 740))

        self.start_text = self.font.render("-Wanneer alle kaarten in de normale stapel zijn gebruikt wordt de weggooistapel geschud en dient deze te worden gebruikt als de nieuwe “normale” stapel ",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 790))

        self.start_text = self.font.render("-Wanneer een speler de overkant haalt met een van z’n schepen mag hij een speciale kaart trekken",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 840))

        self.start_text = self.font.render("-Wanneer het een perk-kaart is wordt de kaart toegewezen aan het schip die de overkant heeft gehaald. De effect van de kaart blijft de rest van het spel actief.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 870))

        self.start_text = self.font.render("-Wanneer een schip wordt vernietigd wordt dezelfde schip een obstakel. ander schepen kunnen niet door obstakels varen. ",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 920))

        self.start_text = self.font.render("-een speler wint nadat hij/zij alle schepen van de tegenstander heeft vernietigd.",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (100, 970))






        pygame.display.flip()


    def game_loop(self):
        #game functionality loop
        while not process_events():
            self.update()
            self.draw()

    def rules_loop(self):
        while not process_events():
            self.update_rules()
            self.draw_rules()
            if quit_check == True:
                break

class VictoryScreen:
    def __init__(self):
        width = 1220
        height = 900
        size = (width, height)

        self.screen = pygame.display.set_mode(size)
        self.bg = pygame.image.load("VictoryImage.PNG")
        self.bg = self.bg.convert()
        self.i = 0


    def draw(self):
        if not self.i == 255:
            self.screen.fill((0, 0, 0))
            self.bg.set_alpha(self.i)
            self.screen.blit(self.bg, (0,0))
            self.i += 1
            pygame.time.delay(5)

            pygame.display.flip()

    def update(self):
        button(10,10,10,10)

    def victory_loop(self):
        while not process_events():
            self.update()
            self.draw()


#button functie
def button(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(mouse)
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()

def button1(x, y, w, h):
    global quit_check
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(mouse)
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1:
            quit_check = True
    return quit_check

def mouse_down():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
    return False
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
    menu = Menu()
    menu.termination_loop()

def program_rules():
    game = Game()
    game.rules_loop()

def program_rules1():
    menu = Menu()
    menu.rules_loop1()

def program_victory():
    victory = VictoryScreen()
    victory.victory_loop()

#aanroepen van startup functie
program()