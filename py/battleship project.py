import pygame
import random
import psycopg2
import time

bgrandom = random.randint(0, 1)
bgrandommusic = random.randint(0,2)
quit_check = True
quit_checkmenu = False
game_quit = False
pygame.init()

x = True
y = True
z = True
u = True
v = True
w = True
t = True
s = True

victory_quit = True

lmao = 0
xD = 0

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
        global color, color1, color2, color3, color4, color5, color6, color7, green, YELLOW , bgrandommusic
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
        button2(1720, 16, 165, 50)


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
        global quit_checkmenu
        if bgrandommusic == 0:
            pygame.mixer.init()
            pygame.mixer.music.load("bgmusic1.ogg")
            pygame.mixer.music.play()

        if bgrandommusic == 1:
            pygame.mixer.init()
            pygame.mixer.music.load("bgmusic2.ogg")
            pygame.mixer.music.play()

        if bgrandommusic == 2:
            pygame.mixer.init()
            pygame.mixer.music.load("bgmusic3.ogg")
            pygame.mixer.music.play()

        #menu functionality loop
        while not process_events() or quit_checkmenu == True:
            global game_quit
            if quit_check == True:
                self.draw()
                self.update()
            if quit_check == False:
                self.update_rules1()
                self.draw_rules1()

    def quit_menu(self):
        # afsluiten van menu
        quit_check = True
        quit()

class Game:
    def __init__(self):
        self.WIDTH = 50
        self.HEIGHT = 50
        self.MARGIN = 5

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)


        turn_player = "player1"
        turn = 1

        #schermgrootte
        width = 1920
        height = 1050
        size = (width, height)

        self.Player1 = Player("Henk" , "Groen")
        self.Player2 = Player("Joost", "Geel")

        #font
        self.font = pygame.font.Font("DroidSans.ttf", 25)

        self.titlefont = pygame.font.Font("Capture_it.ttf", 70)

        self.game_quit = False

        self.screen = pygame.display.set_mode(size)

        self.grid = []
        for self.row in range(20):
            self.grid.append([])
            for self.column in range(20):
                self.grid[self.row].append(0)


    def turn(self):
        self.turn_player = "player1"
        self.turn = 1

    def turnend_player1(self):
        self.turn_player = "player2"
        self.Player1.Furgo.moves = 3
        self.Player1.Intensity.moves = 2
        self.Player1.Silver.moves = 2
        self.Player1.Merapi.moves = 1
        time.sleep(1)

    def turnend_player2(self):
        self.turn_player = "player1"
        self.turn += 1
        self.Player2.Furgo.moves = 3
        self.Player2.Intensity.moves = 2
        self.Player2.Silver.moves = 2
        self.Player2.Merapi.moves = 1
        print(self.Player2.Furgo.moves)
        time.sleep(1)


    def player1_turn(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 1550 + 300 > mouse[0] > 1550 and 100 + 50 > mouse[1] > 100:
            if click[0] == 1:
                self.turnend_player1()
    def player2_turn(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 1550 + 300 > mouse[0] > 1550 and 100 + 50 > mouse[1] > 100:
            if click[0] == 1:
                self.turnend_player2()
    def boat(self):
        self.boat = ""

    def update(self):
        global x, y, z, u, v, w, t, s, lmao, xD
        self.screen.fill((0,0,0))
        button(1720, 16, 150, 30, program_rules)
        button(1720, 50, 140, 30, pygame.QUIT)
        button(1720, 84, 200, 30, program)
        if self.turn == 3:
            program_victory()


        pos = pygame.mouse.get_pos()
        print(pos)
        press = pygame.mouse.get_pressed()
        if press[0] == 1:
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360 or self.column == self.Player1.Furgo.pos_column and self.row == self.Player1.Furgo.pos_row +2 and x == False and y == False and z == False and u == False:
                    self.boat = "DrieGroen"
                    self.Player1.Furgo.boat = "DrieGroen"
                elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180 or self.column == self.Player1.Intensity.pos_column and self.row == self.Player1.Intensity.pos_row +3 and x == False and y == False and z == False and u == False:
                    self.boat = "Vier1Groen"
                    self.Player1.Intensity.boat = "Vier1Groen"
                elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190 or self.column == self.Player1.Silver.pos_column and self.row == self.Player1.Silver.pos_row + 3 and x == False and y == False and z == False and u == False:
                    self.boat = "Vier2Groen"
                    self.Player1.Silver.boat = "Vier2Groen"
                elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450 or self.column == self.Player1.Merapi.pos_column and self.row == self.Player1.Merapi.pos_row + 4 and x == False and y == False and z == False and u == False:
                    self.boat = "VijfGroen"
                    self.Player1.Merapi.boat = "VijfGroen"
                elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760 or self.column == self.Player2.Furgo.pos_column and self.row == self.Player2.Furgo.pos_row and v == False and w == False and t == False and s == False:
                    self.boat = "DrieGeel"
                    self.Player2.Furgo.boat = "DrieGeel"
                elif pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[1] <= 1030 or self.column == self.Player2.Intensity.pos_column and self.row == self.Player2.Intensity.pos_row and v == False and w == False and t == False and s == False:
                    self.boat = "Vier1Geel"
                    self.Player2.Intensity.boat = "Vier1Geel"
                elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[1] <= 1030 or self.column == self.Player2.Silver.pos_column and self.row == self.Player2.Silver.pos_row and v == False and w == False and t == False and s == False:
                    self.boat = "Vier2Geel"
                    self.Player2.Silver.boat = "Vier2Geel"
                elif pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[1] <= 850 or self.column == self.Player2.Merapi.pos_column and self.row == self.Player2.Merapi.pos_row and v == False and w == False and t == False and s == False:
                    self.boat = "VijfGeel"
                    self.Player2.Merapi.boat = "VijfGeel"


                if self.column == self.Player1.Furgo.pos_column and self.row == self.Player1.Furgo.pos_row and x == False and y == False and z == False and u == False and self.Player1.Furgo.moves !=0 and self.Player1.Furgo.pos_off == True:
                    self.Player1.Furgo.pos_off = False
                    self.boat = "DrieGroenDef"
                    self.Player1.Furgo.moves -= 1
                    time.sleep(1)

                elif self.column == self.Player1.Furgo.pos_column and self.row == self.Player1.Furgo.pos_row and x == False and y == False and z == False and u == False and self.Player1.Furgo.moves !=0 and self.Player1.Furgo.pos_off == False:
                    self.boat = "DrieGroenOff"
                    self.Player1.Furgo.pos_off = True
                    self.Player1.Furgo.moves -= 1
                    time.sleep(1)

                elif self.column == self.Player1.Intensity.pos_column and self.row == self.Player1.Intensity.pos_row and x == False and y == False and z == False and u == False and self.Player1.Intensity.moves !=0 and self.Player1.Intensity.pos_off == True:
                    self.Player1.Intensity.pos_off = False
                    self.boat = "Vier1GroenDef"
                    self.Player1.Intensity.moves -= 1
                    time.sleep(1)

                elif self.column == self.Player1.Intensity.pos_column and self.row == self.Player1.Intensity.pos_row and x == False and y == False and z == False and u == False and self.Player1.Intensity.moves !=0 and self.Player1.Intensity.pos_off == False:
                    self.Player1.Intensity.pos_off = True
                    self.boat = "Vier1GroenOff"
                    self.Player1.Intensity.moves -= 1
                    time.sleep(1)

                elif self.column == self.Player1.Silver.pos_column and self.row == self.Player1.Silver.pos_row and x == False and y == False and z == False and u == False and self.Player1.Silver.moves !=0:
                    self.Player1.Silver.pos_off = False

                elif self.column == self.Player1.Merapi.pos_column and self.row == self.Player1.Merapi.pos_row and x == False and y == False and z == False and u == False and self.Player1.Merapi.moves !=0:
                    self.Player1.Merapi.pos_off = False




                if pos[0] > 199 and pos[0] < 1300:
                    print("Click ", pos, "self.grid coordinates: ", self.row, self.column)
                    if self.boat == "DrieGroen" and x == True and self.turn_player == "player1":
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
                            self.boat = ""
                            x = False
                            time.sleep(1)

                    elif self.boat == "Vier1Groen" and y == True and self.turn_player == "player1":
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
                            self.boat = ""
                            y = False
                            time.sleep(1)


                    elif self.boat == "Vier2Groen" and z == True and self.turn_player == "player1":
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
                            self.Player1.Silver.pos_row = self.row
                            self.Player1.Silver.pos_column = self.column
                            self.boat = ""
                            z = False

                    elif self.boat == "VijfGroen" and u == True and self.turn_player == "player1":
                        if self.row >= 15:
                            print("Oops you went out the playfield, Try again!")
                        elif self.grid[self.row][self.column] == 1 or self.grid[self.row + 1][self.column] == 1 or self.grid[self.row + 2][self.column] == 1 or \
                                        self.grid[self.row + 3][self.column] == 1 or self.grid[self.row + 4][self.column] == 1:
                            print("Oops there is already a boat here, Try again!")
                        elif self.row == 0:
                            self.grid[self.row][self.column] = 1
                            self.grid[self.row + 1][self.column] = 1
                            self.grid[self.row + 2][self.column] = 1
                            self.grid[self.row + 3][self.column] = 1
                            self.grid[self.row + 4][self.column] = 1
                            self.Player1.Merapi.pos_row = self.row
                            self.Player1.Merapi.pos_column = self.column
                            self.boat = ""
                            u = False

                    elif self.boat == "DrieGeel" and v == True and self.turn_player == "player2":
                        if self.row == 20:
                            print("Oops you went out the playfield, Try again!")
                        elif self.row ==18:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.Player2.Furgo.pos_row = self.row -2
                            self.Player2.Furgo.pos_column = self.column
                            self.boat = ""
                            v = False

                    elif self.boat == "Vier1Geel" and w == True and self.turn_player == "player2":
                        if self.row == 20:
                            print("Oops you went out the playfield, Try again!")
                        elif self.row == 18:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.grid[self.row - 3][self.column] = 2
                            self.Player2.Intensity.pos_row = self.row -3
                            self.Player2.Intensity.pos_column = self.column
                            self.boat = ""
                            w = False


                    elif self.boat == "Vier2Geel" and t == True and self.turn_player == "player2":
                        if self.row == 20:
                            print("Oops you went out the playfield, Try again!")
                        elif self.row == 18:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.grid[self.row - 3][self.column] = 2
                            self.Player2.Silver.pos_row = self.row -3
                            self.Player2.Silver.pos_column = self.column
                            self.boat = ""
                            t = False

                    elif self.boat == "VijfGeel" and s == True and self.turn_player == "player2":
                        if self.row == 20:
                            print("Oops you went out the playfield, Try again!")
                        elif self.row == 18:
                            self.grid[self.row][self.column] = 2
                            self.grid[self.row - 1][self.column] = 2
                            self.grid[self.row - 2][self.column] = 2
                            self.grid[self.row - 3][self.column] = 2
                            self.grid[self.row - 4][self.column] = 2
                            self.Player2.Merapi.pos_row = self.row - 4
                            self.Player2.Merapi.pos_column = self.column
                            self.boat = ""
                            s = False
        keys = pygame.key.get_pressed()
        print(keys)
        if keys[pygame.K_DOWN] and self.boat == "DrieGroen" and not self.Player1.Furgo.pos_row == 16 and self.Player1.Furgo.moves != 0 and self.Player1.Furgo.pos_off == True and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Furgo.pos_row + 3][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.Player1.Furgo.pos_row += 1
            self.Player1.Furgo.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "DrieGroen" and not self.Player1.Furgo.pos_row == 0 and self.Player1.Furgo.moves != 0 and self.Player1.Furgo.pos_off == True and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row - 0][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row - 1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] = 3
            self.Player1.Furgo.pos_row -= 1
            self.Player1.Furgo.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "DrieGroen" and not self.Player1.Furgo.pos_column == 19 and self.Player1.Furgo.moves != 0 and self.Player1.Furgo.pos_off == True and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +1] = 1
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column+1] = 1
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column+1] = 1
            self.Player1.Furgo.pos_column += 1
            self.Player1.Furgo.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "DrieGroen" and not self.Player1.Furgo.pos_column == 0 and self.Player1.Furgo.moves != 0 and self.Player1.Furgo.pos_off == True and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row ][self.Player1.Furgo.pos_column -1] = 1
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column-1] = 1
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column-1] = 1
            self.Player1.Furgo.pos_column -= 1
            self.Player1.Furgo.moves -= 1
            time.sleep(1)
        elif self.Player1.Furgo.pos_off == False and self.boat == "DrieGroenDef" and self.Player1.Furgo.moves != 0 and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +1] = 1
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +2] = 1
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
        elif self.Player1.Furgo.pos_off == True and self.boat == "DrieGroenOff" and self.Player1.Furgo.moves != 0 and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +1] = 3
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +2] = 3
            self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 1
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 1
        elif self.Player1.Furgo.hp == 0:
            self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row + 1][self.Player1.Furgo.pos_column] = 3
            self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] = 3






        if keys[pygame.K_DOWN] and self.boat == "Vier1Groen" and not self.Player1.Intensity.pos_row == 16 and self.Player1.Intensity.moves != 0 and self.Player1.Intensity.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Intensity.pos_row + 4][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row + 1][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row + 2][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 3
            self.Player1.Intensity.pos_row += 1
            self.Player1.Intensity.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "Vier1Groen" and not self.Player1.Intensity.pos_row == 0 and self.Player1.Intensity.moves != 0 and self.Player1.Intensity.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row ][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row - 1][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] = 3
            self.Player1.Intensity.pos_row -= 1
            self.Player1.Intensity.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "Vier1Groen" and not self.Player1.Intensity.pos_column == 19 and self.Player1.Intensity.moves != 0 and self.Player1.Intensity.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +1] = 1
            self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column+1] = 1
            self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column+1] = 1
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column +1] = 1
            self.Player1.Intensity.pos_column += 1
            self.Player1.Intensity.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "Vier1Groen" and not self.Player1.Intensity.pos_column == 0 and self.Player1.Intensity.moves != 0 and self.Player1.Intensity.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row ][self.Player1.Intensity.pos_column -1] = 1
            self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column-1] = 1
            self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column-1] = 1
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column - 1] = 1
            self.Player1.Intensity.pos_column -= 1
            self.Player1.Intensity.moves -= 1
            time.sleep(1)
        elif self.Player1.Intensity.pos_off == False and self.boat == "Vier1GroenDef" and self.Player1.Intensity.moves != 0 and self.Player1.Intensity.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +1] = 1
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +2] = 1
            self.grid[self.Player1.Intensity.pos_row ][self.Player1.Intensity.pos_column +3] = 1
            self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] = 3
        elif self.Player1.Intensity.pos_off == True and self.boat == "Vier1GroenOff" and self.Player1.Intensity.moves != 0 and self.Player1.Intensity.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +1] = 3
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +2] = 3
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column + 3] = 3
            self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row +3][self.Player1.Intensity.pos_column] = 1
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 1
        elif self.Player1.Intensity.hp == 0:
            self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row + 1][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row + 2][self.Player1.Intensity.pos_column] = 3
            self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] = 3
            

        if keys[pygame.K_DOWN] and self.boat == "Vier2Groen" and not self.Player1.Silver.pos_row == 16 and self.Player1.Silver.moves != 0 and self.Player1.Silver.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Silver.pos_row + 4][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row + 1][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row + 2][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 3
            self.Player1.Silver.pos_row += 1
            self.Player1.Silver.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "Vier2Groen" and not self.Player1.Silver.pos_row == 0 and self.Player1.Silver.moves != 0 and self.Player1.Silver.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Silver.pos_row + 2][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row + 1][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row - 1][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] = 3
            self.Player1.Silver.pos_row -= 1
            self.Player1.Silver.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "Vier2Groen" and not self.Player1.Silver.pos_column == 19 and self.Player1.Silver.moves != 0 and self.Player1.Silver.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 1][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 2][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column + 1] = 1
            self.grid[self.Player1.Silver.pos_row + 1][self.Player1.Silver.pos_column + 1] = 1
            self.grid[self.Player1.Silver.pos_row + 2][self.Player1.Silver.pos_column + 1] = 1
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column + 1] = 1
            self.Player1.Silver.pos_column += 1
            self.Player1.Silver.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "Vier2Groen" and not self.Player1.Silver.pos_column == 0 and self.Player1.Silver.moves != 0 and self.Player1.Silver.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 1][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 2][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column - 1] = 1
            self.grid[self.Player1.Silver.pos_row + 1][self.Player1.Silver.pos_column - 1] = 1
            self.grid[self.Player1.Silver.pos_row + 2][self.Player1.Silver.pos_column - 1] = 1
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column - 1] = 1
            self.Player1.Silver.pos_column -= 1
            self.Player1.Silver.moves -= 1
            time.sleep(1)
        elif self.Player1.Silver.pos_off == False and self.boat == "Vier2GroenDef" and self.Player1.Silver.moves != 0 and self.Player1.Silver.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +1] = 1
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +2] = 1
            self.grid[self.Player1.Silver.pos_row ][self.Player1.Silver.pos_column +3] = 1
            self.grid[self.Player1.Silver.pos_row +1][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row +2][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] = 3
        elif self.Player1.Silver.pos_off == True and self.boat == "Vier2GroenOff" and self.Player1.Silver.moves != 0 and self.Player1.Silver.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +1] = 3
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +2] = 3
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column + 3] = 3
            self.grid[self.Player1.Silver.pos_row +1][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row +2][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row +3][self.Player1.Silver.pos_column] = 1
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 1
        elif self.Player1.Silver.hp == 0:
            self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 1][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 2][self.Player1.Silver.pos_column] = 3
            self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] = 3


        if keys[pygame.K_DOWN] and self.boat == "VijfGroen" and not self.Player1.Merapi.pos_row == 16 and self.Player1.Merapi.moves != 0 and self.Player1.Merapi.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Merapi.pos_row + 5][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 3
            self.Player1.Merapi.pos_row += 1
            self.Player1.Merapi.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "VijfGroen" and not self.Player1.Merapi.pos_row == 0 and self.Player1.Merapi.moves != 0 and self.Player1.Merapi.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row - 1][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] = 3
            self.Player1.Merapi.pos_row -= 1
            self.Player1.Merapi.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "VijfGroen" and not self.Player1.Merapi.pos_column == 19 and self.Player1.Merapi.moves != 0 and self.Player1.Merapi.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column + 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column + 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column + 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column + 1] = 1
            self.Player1.Merapi.pos_column += 1
            self.Player1.Merapi.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "VijfGroen" and not self.Player1.Merapi.pos_column == 0 and self.Player1.Merapi.moves != 0 and self.Player1.Merapi.pos_off == True and self.turn_player == "player1":
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column - 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column - 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column - 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column - 1] = 1
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column - 1] = 1
            self.Player1.Merapi.pos_column -= 1
            self.Player1.Merapi.moves -= 1
            time.sleep(1)
        elif self.Player1.Merapi.pos_off == False and self.boat == "VijfGroenDef" and self.Player1.Merapi.moves != 0 and self.Player1.Merapi.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 1] = 1
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 2] = 1
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 3] = 1
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 4] = 1
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row+ 4][self.Player1.Merapi.pos_column ] = 3
        elif self.Player1.Merapi.pos_off == True and self.boat == "VijfGroenOff" and self.Player1.Merapi.moves != 0 and self.Player1.Merapi.hp != 0 and self.turn_player == "player1":
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 1] = 3
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 2] = 3
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 3] = 3
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 4] = 3
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] = 1
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 1
        elif self.Player1.Merapi.hp == 0:
            self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 3
            self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] = 3
            
            
        if keys[pygame.K_DOWN] and self.boat == "DrieGeel" and not self.Player2.Furgo.pos_row == 16 and self.Player2.Furgo.moves != 0 and self.Player2.Furgo.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Furgo.pos_row + 3][self.Player2.Furgo.pos_column] = 2
            self.grid[self.Player2.Furgo.pos_row + 1][self.Player2.Furgo.pos_column] = 2
            self.grid[self.Player2.Furgo.pos_row + 2][self.Player2.Furgo.pos_column] = 2
            self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column] = 3
            self.Player2.Furgo.pos_row += 1
            self.Player2.Furgo.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "DrieGeel" and not self.Player2.Furgo.pos_row == 0 and self.Player2.Furgo.moves != 0 and self.Player2.Furgo.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Furgo.pos_row +1][self.Player2.Furgo.pos_column] = 2
            self.grid[self.Player2.Furgo.pos_row - 0][self.Player2.Furgo.pos_column] = 2
            self.grid[self.Player2.Furgo.pos_row - 1][self.Player2.Furgo.pos_column] = 2
            self.grid[self.Player2.Furgo.pos_row + 2][self.Player2.Furgo.pos_column] = 3
            self.Player2.Furgo.pos_row -= 1
            self.Player2.Furgo.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "DrieGeel" and not self.Player2.Furgo.pos_column == 19 and self.Player2.Furgo.moves != 0 and self.Player2.Furgo.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row +1][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row +2][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column +1] = 2
            self.grid[self.Player2.Furgo.pos_row +1][self.Player2.Furgo.pos_column+1] = 2
            self.grid[self.Player2.Furgo.pos_row +2][self.Player2.Furgo.pos_column+1] = 2
            self.Player2.Furgo.pos_column += 1
            self.Player2.Furgo.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "DrieGeel" and not self.Player2.Furgo.pos_column == 0 and self.Player2.Furgo.moves != 0 and self.Player2.Furgo.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row +1][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row +2][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row ][self.Player2.Furgo.pos_column -1] = 2
            self.grid[self.Player2.Furgo.pos_row +1][self.Player2.Furgo.pos_column-1] = 2
            self.grid[self.Player2.Furgo.pos_row +2][self.Player2.Furgo.pos_column-1] = 2
            self.Player2.Furgo.pos_column -= 1
            self.Player2.Furgo.moves -= 1
            time.sleep(1)
        elif self.Player2.Furgo.hp == 0:
            self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row + 1][self.Player2.Furgo.pos_column] = 3
            self.grid[self.Player2.Furgo.pos_row + 2][self.Player2.Furgo.pos_column] = 3
        


        if keys[pygame.K_DOWN] and self.boat == "Vier1Geel" and not self.Player2.Intensity.pos_row == 16 and self.Player2.Intensity.moves != 0 and self.Player2.Intensity.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Intensity.pos_row + 4][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row + 1][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row + 2][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row][self.Player2.Intensity.pos_column] = 3
            self.Player2.Intensity.pos_row += 1
            self.Player2.Intensity.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "Vier1Geel" and not self.Player2.Intensity.pos_row == 0 and self.Player2.Intensity.moves != 0 and self.Player2.Intensity.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Intensity.pos_row +2][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row +1][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row ][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row - 1][self.Player2.Intensity.pos_column] = 2
            self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column] = 3
            self.Player2.Intensity.pos_row -= 1
            self.Player2.Intensity.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "Vier1Geel" and not self.Player2.Intensity.pos_column == 19 and self.Player2.Intensity.moves != 0 and self.Player2.Intensity.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Intensity.pos_row][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row +1][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row +2][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row][self.Player2.Intensity.pos_column +1] = 2
            self.grid[self.Player2.Intensity.pos_row +1][self.Player2.Intensity.pos_column+1] = 2
            self.grid[self.Player2.Intensity.pos_row +2][self.Player2.Intensity.pos_column+1] = 2
            self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column +1] = 2
            self.Player2.Intensity.pos_column += 1
            self.Player2.Intensity.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "Vier1Geel" and not self.Player2.Intensity.pos_column == 0 and self.Player2.Intensity.moves != 0 and self.Player2.Intensity.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Intensity.pos_row][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row +1][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row +2][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row ][self.Player2.Intensity.pos_column -1] = 2
            self.grid[self.Player2.Intensity.pos_row +1][self.Player2.Intensity.pos_column-1] = 2
            self.grid[self.Player2.Intensity.pos_row +2][self.Player2.Intensity.pos_column-1] = 2
            self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column - 1] = 2
            self.Player2.Intensity.pos_column -= 1
            self.Player2.Intensity.moves -= 1
            time.sleep(1)
        elif self.Player2.Intensity.hp == 0:
            self.grid[self.Player2.Intensity.pos_row][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row + 1][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row + 2][self.Player2.Intensity.pos_column] = 3
            self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column] = 3

        if keys[pygame.K_DOWN] and self.boat == "Vier2Geel" and not self.Player2.Silver.pos_row == 16 and self.Player2.Silver.moves != 0 and self.Player2.Silver.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Silver.pos_row + 4][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column] = 3
            self.Player2.Silver.pos_row += 1
            self.Player2.Silver.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "Vier2Geel" and not self.Player2.Silver.pos_row == 0 and self.Player2.Silver.moves != 0 and self.Player2.Silver.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row - 1][self.Player2.Silver.pos_column] = 2
            self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] = 3
            self.Player2.Silver.pos_row -= 1
            self.Player2.Silver.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "Vier2Geel" and not self.Player2.Silver.pos_column == 19 and self.Player2.Silver.moves != 0 and self.Player2.Silver.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column + 1] = 2
            self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column + 1] = 2
            self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column + 1] = 2
            self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column + 1] = 2
            self.Player2.Silver.pos_column += 1
            self.Player2.Silver.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "Vier2Geel" and not self.Player2.Silver.pos_column == 0 and self.Player2.Silver.moves != 0 and self.Player2.Silver.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column - 1] = 2
            self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column - 1] = 2
            self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column - 1] = 2
            self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column - 1] = 2
            self.Player2.Silver.pos_column -= 1
            self.Player2.Silver.moves -= 1
            time.sleep(1)
        elif self.Player2.Silver.hp == 0:
            self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column] = 3
            self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] = 3


        if keys[pygame.K_DOWN] and self.boat == "VijfGeel" and not self.Player2.Merapi.pos_row == 16 and self.Player2.Merapi.moves != 0 and self.Player2.Merapi.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Merapi.pos_row + 5][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 3
            self.Player2.Merapi.pos_row += 1
            self.Player2.Merapi.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_UP] and self.boat == "VijfGeel" and not self.Player2.Merapi.pos_row == 0 and self.Player2.Merapi.moves != 0 and self.Player2.Merapi.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row - 1][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 2
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 3
            self.Player2.Merapi.pos_row -= 1
            self.Player2.Merapi.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_RIGHT] and self.boat == "VijfGeel" and not self.Player2.Merapi.pos_column == 19 and self.Player2.Merapi.moves != 0 and self.Player2.Merapi.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column + 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column + 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column + 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column + 1] = 2
            self.Player2.Merapi.pos_column += 1
            self.Player2.Merapi.moves -= 1
            time.sleep(1)
        elif keys[pygame.K_LEFT] and self.boat == "VijfGeel" and not self.Player2.Merapi.pos_column == 0 and self.Player2.Merapi.moves != 0 and self.Player2.Merapi.pos_off == True and self.turn_player == "player2":
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column - 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column - 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column - 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column - 1] = 2
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column - 1] = 2
            self.Player2.Merapi.pos_column -= 1
            self.Player2.Merapi.moves -= 1
            time.sleep(1)
        elif self.Player2.Merapi.pos_off == False and self.boat == "VijfGeelDef" and self.Player2.Merapi.moves != 0 and self.Player2.Merapi.hp != 0 and self.turn_player == "Player2":
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 1
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 1] = 1
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 2] = 1
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 3] = 1
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 4] = 1
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 3
        elif self.Player2.Merapi.pos_off == True and self.boat == "VijfGeelOff" and self.Player2.Merapi.moves != 0 and self.Player2.Merapi.hp != 0 and self.turn_player == "Player2":
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 1] = 3
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 2] = 3
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 3] = 3
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column + 4] = 3
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 1
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 1
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 1
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 1
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 1
        elif self.Player2.Merapi.hp == 0:
            self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 3
            self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 3


        for self.row in range(20):
            for self.column in range(20):
                color0 = self.WHITE
                if self.grid[self.row][self.column] == 1:
                    color0 = self.GREEN
                elif self.grid[self.row][self.column] == 2:
                    color0 = self.YELLOW
                pygame.draw.rect(self.screen, color0,
                                 [(self.MARGIN + self.WIDTH) * self.column + 200 + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * self.row + self.MARGIN, self.WIDTH,
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

        self.start_text = self.font.render("End turn",
                                                       1, (255, 255, 255))
        self.screen.blit(self.start_text, (1550, 100))

        self.start_text = self.font.render(str(self.turn_player) + " Turn: "   + str(self.turn),
                                                       1, (255, 255, 255))
        self.screen.blit(self.start_text, (1550, 150))


        press = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        boat3 = pygame.draw.rect(self.screen, color, (130, 250, 40, 110))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[1] <= 360 and self.turn_player == "player1":
            color = self.BLACK
            block1 = pygame.draw.rect(self.screen, color, (130, 250, 40, 110))
        boat4 = pygame.draw.rect(self.screen, color1, (130, 50, 40, 140))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[1] <= 180 and self.turn_player == "player1":
            color1 = self.BLACK
            block2 = pygame.draw.rect(self.screen, color1, (130, 50, 40, 140))
        boat4x = pygame.draw.rect(self.screen, color2, (50, 50, 40, 140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[1] <= 190 and self.turn_player == "player1":
            color2 = self.BLACK
            block3 = pygame.draw.rect(self.screen, color2, (50, 50, 40, 140))
        boat5 = pygame.draw.rect(self.screen, color3, (50, 250, 40, 200));
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[1] <= 450 and self.turn_player == "player1":
            color3 = self.BLACK
            block4 = pygame.draw.rect(self.screen, color3, (50, 250, 40, 200))

        boat33 = pygame.draw.rect(self.screen, color4, (130, 650, 40, 110))
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[1] <= 760 and self.turn_player == "player2":
            color4 = self.BLACK
            block11 = pygame.draw.rect(self.screen, color4, (130, 650, 40, 110))
        boat44 = pygame.draw.rect(self.screen, color5, (130, 890, 40, 140));
        if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[1] <= 1030 and self.turn_player == "player2":
            color5 = self.BLACK
            block22 = pygame.draw.rect(self.screen, color5, (130, 890, 40, 140))
        boat44x = pygame.draw.rect(self.screen, color6, (50, 890, 40, 140))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[1] <= 1030 and self.turn_player == "player2":
            color6 = self.BLACK
            block33 = pygame.draw.rect(self.screen, color6, (50, 890, 40, 140))
        boat55 = pygame.draw.rect(self.screen, color7, (50, 650, 40, 200))
        if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[1] <= 850 and self.turn_player == "player2":
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
            if self.turn_player == "player1":
                self.player1_turn()
            else:
                self.player2_turn()
            if self.Player1.Furgo.hp == 0 and self.Player1.Intensity.hp == 0 and self.Player1.Silver.hp == 0 and self.Player1.Merapi.hp == 0 or self.Player2.Furgo.hp == 0 and self.Player2.Intensity.hp == 0 and self.Player2.Silver.hp == 0 and self.Player2.Merapi.hp == 0:
                program_victory()

            if self.game_quit == True:
                break

            if game_quit == True:
                break

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
        self.x = -400
        self.y = -800
        self.z = -400
        self.a = 5
        self.font = pygame.font.Font("Capture_It.ttf", 50)

        self.victory_quit = True


    def draw(self):
        if self.i < 255:
            self.screen.fill((0, 0, 0))
            self.bg.set_alpha(self.i)
            self.screen.blit(self.bg, (0,0))
            self.i += 1
            pygame.time.delay(5)


        self.screen.blit(self.bg, (0, 0))

        if self.x != 480 and self.i == 255:
            self.start_text = self.font.render(
                "Play again",
                1, (255, 255, 255))
            self.screen.blit(self.start_text, (self.x, 800))
            self.x +=2

        if self.y != 150 and self.i == 255:
            self.start_text = self.font.render(
                "Main Menu",
                1, (255, 255, 255))
            self.screen.blit(self.start_text, (self.y, 700))
            self.y += 2

        if self.z != 800 and self.i == 255:
            self.start_text = self.font.render(
                "High Score",
                1, (255, 255, 255))
            self.screen.blit(self.start_text, (self.z, 700))
            self.z += 2


        self.start_text = self.font.render(
            "Main Menu",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (self.y, 700))

        self.start_text = self.font.render(
            "Play again",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (self.x, 800))

        self.start_text = self.font.render(
            "High Score",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (self.z, 700))

        pygame.display.flip()

    def update(self):
        button(800 ,700, 300 ,50, program2)
        button(150, 700, 300, 50,)
        button(480, 800, 300, 50, game_reset)

    def victory_loop(self):
        global victory_quit
        while process_events() == False:
            self.update()
            self.draw()
            if self.victory_quit == False:
                break


class Player:
    def __init__(self, name, kleur):
        self.name = name
        self.score = 0
        self.kleur = kleur

        self.Furgo = Boat(2, 3, 2, 1)
        self.Intensity = Boat(3, 2, 3, 1)
        self.Silver = Boat(3, 2, 3, 1,)
        self.Merapi = Boat(4, 1, 4, 1,)

class Boat:
    def __init__(self, hp, moves, atk_range, atk_damage):
        self.hp = hp
        self.moves = moves
        self.atk_range = atk_range
        self.atk_damage = atk_damage
        self.pos_off = True
        self.boat = ""
        self.pos_row = 0
        self.pos_column = 0



#button functie
def button(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            pygame.mixer.init()
            pygame.mixer.music.load("MenuBlip.ogg")
            pygame.mixer.music.play()
            time.sleep(0.3)
            action()

def button1(x, y, w, h):
    global quit_check
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1:
            quit_check = True
    return quit_check

def button2(x, y, w, h):
    global quit_check
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1:
            quit_check = False
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
    global x, quit_check, game_quit
    x = True
    game = Game()
    game_quit = True
    menu = Menu()
    menu.menu_loop()
    quit_check = True
#startup van game
def program2():
    global game_quit
    game = Game()
    game_quit = False
    game.turn()
    game.boat()
    game.game_loop()
    menu = Menu()
    menu.quit_menu()
    quit_checkmenu = True
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
    game = Game()
    game.game_quit = True
    victory = VictoryScreen()
    victory.victory = True
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

def game_reset():
    global color, color1, color2, color3, color4, color5, color6, color7, green, YELLOW, x, y, z, u, w, v, w, t, s, victory_quit
    victory = VictoryScreen()

    victory.victory_quit = False
    x = True
    y = True
    z = True
    u = True
    v = True
    w = True
    t = True
    s = True
    color = green
    color1 = green
    color2 = green
    color3 = green

    color4 = YELLOW
    color5 = YELLOW
    color6 = YELLOW
    color7 = YELLOW



    game = Game()

    game.Player1.Furgo = Boat(2, 3, 2, 1)
    game.Player1.Intensity = Boat(3, 2, 3, 1)
    game.Player1.Silver = Boat(3, 2, 3, 1, )
    game.Player1.Merapi = Boat(4, 1, 4, 1, )

    game.Player2.Furgo = Boat(2, 3, 2, 1)
    game.Player2.Intensity = Boat(3, 2, 3, 1)
    game.Player2.Silver = Boat(3, 2, 3, 1, )
    game.Player2.Merapi = Boat(4, 1, 4, 1, )

    game.Player1.score = 0

    game.Player2.score = 0

    game.turn = 1

    game.turn_player = "player1"

    game.game_quit = False

    game.game_loop()








#aanroepen van startup functie
program()

