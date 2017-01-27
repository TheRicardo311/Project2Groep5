import pygame
import random

import time

bgrandom = random.randint(0, 1)
quit_check = False
pygame.init()

x = True

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
YELLOW = (255, 255, 0)

color = green
color1 = green
color2 = green
color3 = green

color4 = YELLOW
color5 = YELLOW
color6 = YELLOW
color7 = YELLOW

class Menu:
    def __init__(self):
        global color, color1, color2, color3, color4, color5, color6, color7, green, YELLOW
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

        color = green
        color1 = green
        color2 = green
        color3 = green

        color4 = YELLOW
        color5 = YELLOW
        color6 = YELLOW
        color7 = YELLOW

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
        self.WIDTH = 50
        self.HEIGHT = 50
        self.MARGIN = 5
        #images
        self.blank = pygame.image.load('blank.png')
        self.bootje = pygame.image.load('boot 3.png')
        self.bootje2 = pygame.image.load('Boot4Groen.png')
        self.bootje3 = pygame.image.load('Boot4Groen.png')
        self.bootje4 = pygame.image.load('Boot5Groen.png')
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        #schermgrootte
        width = 1920
        height = 1050
        size = (width, height)

        self.Player1 = Player("Henk" , "Groen")

        #font
        self.font = pygame.font.Font("DroidSans.ttf", 25)

        self.titlefont = pygame.font.Font("Capture_it.ttf", 70)

        self.bootje = pygame.image.load('boot 3.png')
        self.screen = pygame.display.set_mode(size)

        self.grid = []
        for self.row in range(20):
            self.grid.append([])
            for self.column in range(20):
                self.grid[self.row].append(0)

    def boot(self):
        self.boat = ""

    def update(self):
        global x
        self.screen.fill((0,0,0))
        global quit_check
        quit_check = False
        button(1720, 16, 150, 30, program_rules)
        button(1720, 50, 140, 30, pygame.QUIT)
        button(1720, 84, 200, 30, program)
        

        pos = pygame.mouse.get_pos()
        print(pos)
        press = pygame.mouse.get_pressed()
        if press[0] == 1:
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if pos[0] < 199:
                    if pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360:
                        self.boat = "DrieGroen"
                        self.Player1.Furgo.boat = "DrieGroen"
                    elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180:
                        self.boat = "Vier1Groen"
                        self.Player1.Intensity.boat = "Vier1Groen"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190:
                        self.boat = "Vier2Groen"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450:
                        self.boat = "VijfGroen"
                    elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760:
                        self.boat = "DrieGeel"
                    elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[1] <= 1030:
                        self.boat = "Vier1Geel"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[1] <= 1030:
                        self.boat = "Vier2Geel"
                    elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[1] <= 850:
                        self.boat = "VijfGeel"

                if pos[0] > 199 and pos[0] < 1300:
                    print("Click ", pos, "self.grid coordinates: ", self.row, self.column)
                    if self.boat == "DrieGroen" and x == True:
                        if self.row >= 17:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 1 or self.grid[self.row + 1][self.column] == 1 or self.grid[self.row + 2][self.column] == 1:
                            print("Oops there is already a boat here, Try again!")
                        elif self.row == 0:
                            self.grid[self.row][self.column] = 1
                            self.grid[self.row + 1][self.column] = 1
                            self.grid[self.row + 2][self.column] = 1
                            self.Player1.Furgo.pos_row = self.row
                            self.Player1.Furgo.pos_column = self.column
                            self.boat = "DrieGroen"
                            x = False

                    elif self.boat == "Vier1Groen":
                        if self.row >= 16:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 1 or self.grid[self.row + 1][self.column] == 1 or self.grid[self.row + 2][self.column] == 1 or \
                                        self.grid[self.row + 3][self.column] == 1:
                            print("Oops there is already a boat here, Try again!")
                        elif self.row == 0:
                            self.grid[self.row][self.column] = 1
                            self.grid[self.row + 1][self.column] = 1
                            self.grid[self.row + 2][self.column] = 1
                            self.grid[self.row + 3][self.column] = 1
                            self.Player1.Intensity.pos_row = self.row
                            self.Player1.Intensity.pos_column = self.column
                            self.boat = "Vier1Groen"


                    elif self.boat == "Vier2Groen":
                        if self.row >= 16:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 1 or self.grid[self.row + 1][self.column] == 1 or self.grid[self.row + 2][self.column] == 1 or \
                                        self.grid[self.row + 3][self.column] == 1:
                            print("Oops there is already a boat here, Try again!")
                        else:
                            self.grid[self.row][self.column] = 1
                            self.grid[self.row + 1][self.column] = 1
                            self.grid[self.row + 2][self.column] = 1
                            self.grid[self.row + 3][self.column] = 1
                            self.boat = ""

                    elif self.boat == "VijfGroen":
                        if self.row >= 15:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 1 or self.grid[self.row + 1][self.column] == 1 or self.grid[self.row + 2][self.column] == 1 or \
                                        self.grid[self.row + 3][self.column] == 1 or self.grid[self.row + 4][self.column] == 1:
                            print("Oops there is already a boat here, Try again!")
                        else:
                            self.grid[self.row][self.column] = 1
                            self.grid[self.row + 1][self.column] = 1
                            self.grid[self.row + 2][self.column] = 1
                            self.grid[self.row + 3][self.column] = 1
                            self.grid[self.row + 4][self.column] = 1
                            self.boat = ""

                    elif self.boat == "DrieGeel":
                        if self.row >= 17:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 2 or self.grid[self.row + 1][self.column] == 2 or self.grid[self.row + 2][self.column] == 2:
                            print("Oops there is already a boat here, Try again!")
                        else:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.boat = ""

                    elif self.boat == "Vier1Geel":
                        if self.row >= 16:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 2 or self.grid[self.row + 1][self.column] == 2 or self.grid[self.row + 2][self.column] == 2 or \
                                        self.grid[self.row + 3][self.column] == 2:
                            print("Oops there is already a boat here, Try again!")
                        else:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.grid[self.row - 3][self.column] = 2
                            self.boat = ""

                    elif self.boat == "Vier2Geel":
                        if self.row >= 16:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 2 or self.grid[self.row + 1][self.column] == 2 or self.grid[self.row + 2][self.column] == 2 or \
                                        self.grid[self.row + 3][self.column] == 2:
                            print("Oops there is already a boat here, Try again!")
                        else:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.grid[self.row - 3][self.column] = 2
                            self.boat = ""

                    elif self.boat == "VijfGeel":
                        if self.row >= 15:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 2 or self.grid[self.row + 1][self.column] == 2 or self.grid[self.row + 2][self.column] == 2 or \
                                        self.grid[self.row + 3][self.column] == 2 or self.grid[self.row + 4][self.column] == 2:
                            print("Oops there is already a boat here, Try again!")
                        else:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.grid[self.row - 3][self.column] = 2
                            self.grid[self.row - 4][self.column] = 2
                            self.boat = ""
        keys = pygame.key.get_pressed()
        print(keys)
        if keys[pygame.K_DOWN] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_row == 16:
            self.grid[self.Player1.Furgo.pos_row + 3][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.Player1.Furgo.pos_row += 1
        elif keys[pygame.K_UP] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_row == 0:
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row - 0][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row - 1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] = 3
            self.Player1.Furgo.pos_row -= 1
        elif keys[pygame.K_RIGHT] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_column == 19:
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +1] = 1
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column+1] = 1
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column+1] = 1
            self.Player1.Furgo.pos_column += 1
        elif keys[pygame.K_LEFT] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_column == 0:
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row ][self.Player1.Furgo.pos_column -1] = 1
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column-1] = 1
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column-1] = 1
            self.Player1.Furgo.pos_column -= 1


        if keys[pygame.K_DOWN] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_row == 16:
            self.grid[self.Player1.Furgo.pos_row + 3][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.Player1.Furgo.pos_row += 1
        elif keys[pygame.K_UP] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_row == 0:
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row - 0][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row - 1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] = 3
            self.Player1.Furgo.pos_row -= 1
        elif keys[pygame.K_RIGHT] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_column == 19:
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +1] = 1
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column+1] = 1
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column+1] = 1
            self.Player1.Furgo.pos_column += 1
        elif keys[pygame.K_LEFT] and self.Player1.Furgo.boat == "DrieGroen" and not self.Player1.Furgo.pos_column == 0:
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row ][self.Player1.Furgo.pos_column -1] = 1
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column-1] = 1
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column-1] = 1
            self.Player1.Furgo.pos_column -= 1




        for self.row in range(20):
            for self.column in range(20):
                color0 = self.WHITE
                if self.grid[self.row][self.column] == 1:
                    color0 = self.GREEN
                elif self.grid[self.row][self.column] == 2:
                    color0 = self.YELLOW
                pygame.draw.rect(self.screen, color0,
                            [(self.MARGIN + self.WIDTH) * self.column + 200 + self.MARGIN, (self.MARGIN + self.HEIGHT) * self.row + self.MARGIN, self.WIDTH,
                                    self.HEIGHT])


    def draw(self):
        global color, color1, color2, color3, color4, color5, color6, color7
        self.start_text = self.font.render("Instructions",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (1700, 16))

        self.exit_text = self.font.render("Back to main menu",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (1700, 84))
        
        self.exit_text = self.font.render("Exit Game",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (1700, 50))
        
        press = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        boat3 = self.screen.blit(self.bootje,(130, 250, 40, 110))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360:
            self.bootje = self.blank
            block1 = pygame.draw.rect(self.screen, black, (130, 250, 40, 110))
            
        boat4 = self.screen.blit(self.bootje2,(130, 50, 40, 140))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180:
            self.bootje2 = self.blank
            block2 = pygame.draw.rect(self.screen, black, (130, 50, 40, 140))
        boat4x = self.screen.blit(self.bootje3, (50, 50, 40, 140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190:
            self.bootje3 = self.blank
            block3 = pygame.draw.rect(self.screen, black, (50, 50, 40, 140))
        boat5 = self.screen.blit(self.bootje4, (50, 250, 40, 200));
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450:
            self.bootje4 = self.blank
            block4 = pygame.draw.rect(self.screen, black, (50, 250, 40, 200))

        boat33 = pygame.draw.rect(self.screen, color4, (130, 650, 40, 110))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760:
            color4 = self.BLACK
            block11 = pygame.draw.rect(self.screen, color4, (130, 650, 40, 110))
        boat44 = pygame.draw.rect(self.screen, color5, (130, 890, 40, 140));
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[1] <= 1030:
            color5 = self.BLACK
            block22 = pygame.draw.rect(self.screen, color5, (130, 890, 40, 140))
        boat44x = pygame.draw.rect(self.screen, color6, (50, 890, 40, 140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[1] <= 1030:
            color6 = self.BLACK
            block33 = pygame.draw.rect(self.screen, color6, (50, 890, 40, 140))
        boat55 = pygame.draw.rect(self.screen, color7, (50, 650, 40, 200))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[1] <= 850:
            color7 = self.BLACK
            block44 = pygame.draw.rect(self.screen, color7, (50, 650, 40, 200))

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

class Player:
    def __init__(self, name, kleur):
        self.name = name
        self.score = 0
        self.kleur = kleur

        self.Furgo = Boat(2, 3, 2, 1)
        self.Intensity = Boat(3, 2, 3, 1)
        self.silver = Boat(3, 2, 3, 1,)
        self.Merapi = Boat(4, 1, 4, 1,)

class Boat:
    def __init__(self, hp, moves, atk_range, atk_damage):
        self.hp = hp
        self.moves = moves
        self.atk_range = atk_range
        self.atk_damage = atk_damage
        self.Offensive = True
        self.boat = ""
        self.pos_row = 0
        self.pos_column = 0

        keys = pygame.key.get_pressed()
        print(keys)
        #if keys[K_LEFT]:
            #self.pos.row += 1


#button functie
def button(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()

def button1(x, y, w, h):
    global quit_check
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
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
    global color, color1, color2, color3, color4, color5, color6, color7, green, YELLOW
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
    game.boot
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

def program_kleur():
    global color, color1, color2, color3, color4, color5, color6, color7, green, YELLOW
    color = green
    color1 = green
    color2 = green
    color3 = green

    color4 = YELLOW
    color5 = YELLOW
    color6 = YELLOW
    color7 = YELLOW

#aanroepen van startup functie
program()
