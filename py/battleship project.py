import pygame
import random
import psycopg2
import time

bgrandom = random.randint(0, 1)
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

highscore_quit = True

color8 = bright_green = (0, 255, 0)
color9 = bright_yew = (255,255,0)
#kaart lijst en teksten --------------------------------------------------------------
cards = ['FMJ Upgrade', 'Reinforced Hull', 'Backup']
p1 = ("player 1 cards: ")
p2 = ("player 2 cards: ")

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
green2 = (0,200,0) #------------------kleur voor kaart
YELLOW = (255, 255, 0)
YELLOW2 = (255, 255, 0) #------ kleur voor kaart
red = (255, 0, 0)
bright_yew = (255,255,0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

Pause = True

victory_quit = True

lmao = 0
xD = 0

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
YELLOW = (255, 255, 0)
red = (255, 0, 0)

color = green
color1 = green
color2 = green
color3 = green

color4 = YELLOW
color5 = YELLOW
color6 = YELLOW
color7 = YELLOW


def init_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Project user=postgres password='1234'")
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

    # Save results
    result = None
    try:
        result = cursor.fetchall()
    except psycopg2.ProgrammingError:
        pass

    # Close connection
    cursor.close()
    connection.close()
    return result


# Updates a score in the database
def update_db(score, naam):
    init_database("UPDATE users SET score = " + str(score) + " WHERE name = '" + naam + "' ")


def update_dbx(nummer):
    init_database("UPDATE nummers SET id = " + str(nummer) + "")


# Insert data in db
def insert_db(score, naam):
    init_database("INSERT INTO users VALUES (" + str(score) + " ,'" + naam + "')")


# Delete data from db

def delete_db(player1, player2):
    init_database("DELETE FROM users WHERE name = '" + player1 + "' or name = '" + player2 + "'")


# Read data from database

def read_db():
    return init_database("SELECT * FROM users ORDER BY score LIMIT 10")


scoree = read_db()


def read_dbid():
    return init_database("SELECT * FROM nummers LIMIT 10")


nummeruit = read_dbid()


def haalnummereruit():
    for i in nummeruit:
        a = "{}".format(i[0])
    return a


def show_scores():
    lijst = []
    for i in scoree:
        x = "{} finished in {} turn(s)".format(i[1], i[0])
        lijst.append(x)
    return lijst


class Menu:
    def __init__(self):
        global color, color1, color2, color3, color4, color5, color6, color7, green, YELLOW , bgrandommusic
        #schermgrootte
        width = 1920
        heigth = 1080
        size = (width, heigth)

        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        #title font
        self.fontTitle = pygame.font.Font("Capture_it_2.ttf", 150)
        #start en exit font
        self.font = pygame.font.Font("DroidSans.ttf", 25)

        self.fontinstructions = pygame.font.Font("DroidSans.ttf", 30)

        self.fontsaus = pygame.font.Font("Capture_It.ttf", 30)

        self.fonttitle = pygame.font.Font("Capture_It.ttf", 30)

        self.titlefont = pygame.font.Font("Capture_it.ttf", 70)

        self.font1 = pygame.font.Font("Capture_it.ttf", 70)

        self.Music = True
        self.abc = 1

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
        if self.Music == True:
            musicOnOff = pygame.image.load("VolumeOff.png")
        else:
            musicOnOff = pygame.image.load("VolumeOn.png")

        self.screen.blit(musicOnOff, (0, 0))
        # exit game tekst voor knop
        self.exit_text = self.font1.render("Exit Game",
                                          1, (255, 255, 255))
        self.screen.blit(self.exit_text, (260, 600))

        self.start_text = self.fontinstructions.render("Instructions",
                                           1, (255, 255, 255))
        self.screen.blit(self.start_text, (1720, 16))

        self.start_text = self.font1.render("AI",
                                            1, (255, 255, 255))
        self.screen.blit(self.start_text, (260, 800))
        # flip
        pygame.display.flip()


    def update(self):
        #buttons aanmaken met button functie
        button(260, 600, 450, 50, program_quit)
        button(260, 440, 500, 50, program2)
        button2(1720, 16, 165, 50)
        button(260, 800, 60, 50, programAI)

        buttonposition = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        if clicked[0] == 1:
            if buttonposition[0] >= 0 and buttonposition[0] <= 75 and buttonposition[1] >= 0 and buttonposition[1] <= 75:
                if self.Music == True:
                    if self.abc == 1:
                        self.abc -= 1
                    else:
                        self.Music = False
                        pygame.mixer.music.pause()
                        time.sleep(1)
                else:
                    self.Music = True
                    pygame.mixer.music.unpause()
                    time.sleep(1)


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

        self.start_text = self.font1.render("AI",
                                            1, (255, 255, 255))
        self.screen.blit(self.start_text, (260, 800))

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

    def AI_troll(self):
        pygame.mixer.init()
        pygame.mixer.music.load("AImusic.ogg")
        pygame.mixer.music.play()

    def termination_loop(self):
        while not process_events():
            self.update_termination()
            self.draw_termination()

    def BgMusic(self):
        bgMusic = ['Castlevania2-BloodyTears.ogg', 'Castlevania-SymphonyoftheNight-Dracula.ogg', 'FinalFantasyII-NFC--DeadMusic.ogg', 'FinalFantasyII-NFC--PandemoniumCastle.ogg', 'LeagueOfLegendsMusic-BitRush.ogg', 'LegendOfZeldaIntro.ogg', 'LegendOfZeldaTheme.ogg', 'MarioTheme.ogg', 'PokemonTheme.ogg', 'SkyrimTheme.ogg', 'Undertale-Megalovania.ogg', 'Undertale-SpiderDanceExtended.ogg', 'Zelda2-TheAdventureOfLink-Palace.ogg', 'bgmusic1.ogg', 'bgmusic2.ogg', 'bgmusic3.ogg']

        Random_bgMusic = random.choice(bgMusic)
        pygame.mixer.init()
        pygame.mixer.music.load(Random_bgMusic)
        pygame.mixer.music.play()

    def AI_screen(self):
        bgAI = pygame.image.load("maxresdefault.jpg")
        self.screen.blit(bgAI, (0, 0))

        pygame.display.flip()


    def AI_loop(self):
        while  not process_events():
            self.AI_screen()


    def menu_loop(self):
        global quit_checkmenu


        Menu.BgMusic(self)

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
        self.pause = False
        pygame.mixer.init()
        pygame.mixer.music.load('mortal_kombat_fatality.ogg')
        pygame.mixer.music.play()

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.bright_yew = (255, 255, 0)
        self.bright_red = (255, 0, 0)
        self.bright_green = (0, 255, 0)
        self.w = 0
        self.scorep1 = 1
        self.scorep2 = 1


        ###1/8
        self.hehe = 2
        self.exdee = 0
        self.x_y = -1

        ###2/8
        self.hehe2 = 2
        self.exdee2 = 0
        self.x_y2 = -1

        ###3/8
        self.hehe3 = 2
        self.exdee3 = 0
        self.x_y3 = -1

        ###4/8
        self.hehe4 = 2
        self.exdee4 = 0
        self.x_y4 = -1

        ###5/8
        self.hehe5 = 2
        self.exdee5 = 0
        self.x_y5 = -1

        ###6/8
        self.hehe6 = 2
        self.exdee6 = 0
        self.x_y6 = -1

        ###7/8
        self.hehe7 = 2
        self.exdee7 = 0
        self.x_y7 = -1

        ###8/8
        self.hehe8 = 2
        self.exdee8 = 0
        self.x_y8 = -1

        pygame.mixer.music.stop()

        turn_player = "player1"
        turn = 1

        #schermgrootte
        width = 1920
        height = 1050
        size = (width, height)

        self.ship1 = pygame.image.load('boot 3.png')
        self.blank = pygame.image.load('blank.png')
        self.ship2 = pygame.image.load('Boot4Groen.png')
        self.ship3 = pygame.image.load('Boot4Groen.png')
        self.ship5 = pygame.image.load('Boot5Groen.png')
        self.ship6 = pygame.image.load('Boot3Geel.png')
        self.ship7 = pygame.image.load('Boot4Geel.png')
        self.ship8 = pygame.image.load('Boot4Geel.png')
        self.ship9 = pygame.image.load('Boot5Geel.png')


        self.Player1 = Player("Henk" , "Groen")
        self.Player2 = Player("Joost", "Geel")

        #font
        self.font = pygame.font.Font("DroidSans.ttf", 25)

        self.titlefont = pygame.font.Font("Capture_it.ttf", 70)
        self.fontTitle = pygame.font.Font("Capture_it_2.ttf", 150)
        # start en exit font
        self.font = pygame.font.Font("DroidSans.ttf", 25)
        self.fontTitle2 = pygame.font.Font("Capture_it_2.ttf", 300)
        self.fontinstructions = pygame.font.Font("DroidSans.ttf", 30)

        self.fontsaus = pygame.font.Font("Capture_It.ttf", 30)

        self.fonttitle = pygame.font.Font("Capture_It.ttf", 30)

        self.titlefont = pygame.font.Font("Capture_it.ttf", 70)

        self.font1 = pygame.font.Font("Capture_it.ttf", 70)
        self.game_quit = False
        self.lexD = 0

        self.lexD1 = 0

        self.lexD2 = 0

        self.lexD3 = 0

        # kaarten text set up--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.font2 = pygame.font.SysFont('Goudy Stout', 20, True, False)
        self.font3 = pygame.font.SysFont('Arial', 17, True, False)
        self.textcard1 = self.font2.render(" ---------- Cards in hand ----------", True, self.WHITE)
        self.textcard3 = self.font2.render(" P1:", True, self.GREEN)
        self.textcard4 = self.font2.render(" P2:", True, self.YELLOW)

        self.cards = ['FMJ Upgrade', 'Reinforced Hull', 'Backup']
        self.p1 = ("player 1 cards: ")
        self.p2 = ("player 2 cards: ")
        self.card3 = self.font2.render("<+>", 1, self.WHITE)  # om kaarten te onderscheiden

        self.p1rand1 = random.choice(cards)
        self.p1rand2 = random.choice(cards)
        self.p1rand3 = random.choice(cards)

        self.p1k1 = self.font3.render(self.p1rand1, 1, self.WHITE)
        self.p1k2 = self.font3.render(self.p1rand2, 1, self.WHITE)
        self.p1k3 = self.font3.render(self.p1rand3, 1, self.WHITE)

        self.usecard = self.font3.render("USE CARD", 1, (255, 255, 255))

        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

        self.grid = []
        for self.row in range(20):
            self.grid.append([])
            for self.column in range(20):
                self.grid[self.row].append(0)

        def text_objects(self, text, font):
            self.textSurface = self.font.render(text, True, WHITE)

            return self.textSurface, self.textSurface.get_rect()


    def turn(self):
        self.turn_player = "player1"
        self.turn = 1

    def turnend_player1(self):
        self.turn_player = "player2"
        self.Player1.Furgo.moves = 3
        self.Player1.Intensity.moves = 2
        self.Player1.Silver.moves = 2
        self.Player1.Merapi.moves = 1
        self.hehe5 = 2
        self.exdee5 = 0
        self.hehe6 = 2
        self.exdee6 = 0
        self.hehe7 = 2
        self.exdee7 = 0
        self.hehe8 = 2
        self.exdee8 = 0
        time.sleep(1)

    def turnend_player2(self):
        self.turn_player = "player1"
        self.turn += 1
        self.Player2.Furgo.moves = 3
        self.Player2.Intensity.moves = 2
        self.Player2.Silver.moves = 2
        self.Player2.Merapi.moves = 1
        self.hehe = 2
        self.exdee = 0
        time.sleep(1)


    def player1_turn(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 1350 + 300 > mouse[0] > 1350 and 16 + 50 > mouse[1] > 16:
            if click[0] == 1:
                self.turnend_player1()
    def player2_turn(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 1350 + 300 > mouse[0] > 1350 and 16 + 50 > mouse[1] > 16:
            if click[0] == 1:
                self.turnend_player2()
    def boat(self):
        self.boat = ""

    def update(self):
        global x, y, z, u, v, w, t, s, lmao, xD, Pause
        global cards, p1, p2  # voor de kaarten lijst en p1 / p2

        # random kaarten van lijst
        self.p1rand1 = random.choice(cards)
        self.p1rand2 = random.choice(cards)
        self.p1rand3 = random.choice(cards)
        if Pause == True or self.pause == False:
            self.screen.fill((0,0,0))
            button(1720, 16, 150, 30, program_rules)
            button(1720, 50, 140, 30, pygame.QUIT)
            button(1720, 84, 200, 30, program)
            if self.turn == 6:
                program_victory()



            pos = pygame.mouse.get_pos()
            press = pygame.mouse.get_pressed()
            if press[0] == 1 and self.pause == False:
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
                        self.boat = "Vier1GroenOff"
                        self.Player1.Intensity.pos_off = True
                        self.Player1.Intensity.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player1.Silver.pos_column and self.row == self.Player1.Silver.pos_row and x == False and y == False and z == False and u == False and self.Player1.Silver.moves !=0 and self.Player1.Silver.pos_off == True:
                        self.Player1.Silver.pos_off = False
                        self.boat = "Vier2GroenDef"
                        self.Player1.Silver.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player1.Silver.pos_column and self.row == self.Player1.Silver.pos_row and x == False and y == False and z == False and u == False and self.Player1.Silver.moves != 0 and self.Player1.Silver.pos_off == False:
                        self.boat = "Vier2GroenOff"
                        self.Player1.Silver.pos_off = True
                        self.Player1.Silver.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player1.Merapi.pos_column and self.row == self.Player1.Merapi.pos_row and x == False and y == False and z == False and u == False and self.Player1.Merapi.moves !=0 and self.Player1.Merapi.pos_off == True :
                        self.Player1.Merapi.pos_off = False
                        self.boat = "VijfGroenDef"
                        self.Player1.Merapi.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player1.Merapi.pos_column and self.row == self.Player1.Merapi.pos_row and x == False and y == False and z == False and u == False and self.Player1.Merapi.moves != 0 and self.Player1.Merapi.pos_off == False:
                        self.boat = "VijfGroenOff"
                        self.Player1.Merapi.pos_off = True
                        self.Player1.Merapi.moves -= 1
                        time.sleep(1)



                    elif self.column == self.Player2.Furgo.pos_column and self.row == self.Player2.Furgo.pos_row +2 and w == False and v == False and t == False and s == False and self.Player2.Furgo.moves !=0 and self.Player2.Furgo.pos_off == True:
                        self.Player2.Furgo.pos_off = False
                        self.boat = "DrieGeelDef"
                        self.Player2.Furgo.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player2.Furgo.pos_column and self.row == self.Player2.Furgo.pos_row  +2and w == False and v == False and t == False and s == False and self.Player2.Furgo.moves !=0 and self.Player2.Furgo.pos_off == False:
                        self.boat = "DrieGeelOff"
                        self.Player2.Furgo.pos_off = True
                        self.Player2.Furgo.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player2.Intensity.pos_column and self.row == self.Player2.Intensity.pos_row +3 and w == False and v == False and t == False and s == False and self.Player2.Intensity.moves !=0 and self.Player2.Intensity.pos_off == True:
                        self.Player2.Intensity.pos_off = False
                        self.boat = "Vier1GeelDef"
                        self.Player2.Intensity.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player2.Intensity.pos_column and self.row == self.Player2.Intensity.pos_row + 3 and w == False and v == False and t == False and s == False and self.Player2.Intensity.moves !=0 and self.Player2.Intensity.pos_off == False:
                        self.boat = "Vier1GeelOff"
                        self.Player2.Intensity.pos_off = True
                        self.Player2.Intensity.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player2.Silver.pos_column and self.row == self.Player2.Silver.pos_row +3and w == False and v == False and t == False and s == False and self.Player2.Silver.moves !=0 and self.Player2.Silver.pos_off == True:
                        self.Player2.Silver.pos_off = False
                        self.boat = "Vier2GeelDef"
                        self.Player2.Silver.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player2.Silver.pos_column and self.row == self.Player2.Silver.pos_row +3and w == False and v == False and t == False and s == False and self.Player2.Silver.moves != 0 and self.Player2.Silver.pos_off == False:
                        self.boat = "Vier2GeelOff"
                        self.Player2.Silver.pos_off = True
                        self.Player2.Silver.moves -= 1
                        time.sleep(1)

                    elif self.column == self.Player2.Merapi.pos_column and self.row == self.Player2.Merapi.pos_row +4 and w == False and v == False and t == False and s == False and self.Player2.Merapi.moves !=0 and self.Player2.Merapi.pos_off == True :
                        self.Player2.Merapi.pos_off = False
                        self.boat = "VijfGeelDef"
                        self.Player2.Merapi.moves -= 1
                        print(self.boat)
                        time.sleep(1)

                    elif self.column == self.Player2.Merapi.pos_column and self.row == self.Player2.Merapi.pos_row +4 and w == False and v == False and t == False and s == False and self.Player2.Merapi.moves != 0 and self.Player2.Merapi.pos_off == False:
                        self.boat = "VijfGeelOff"
                        self.Player2.Merapi.pos_off = True
                        self.Player2.Merapi.moves -= 1
                        time.sleep(1)

                    if pos[0] > 199 and pos[0] < 1300:
                        if self.boat == "DrieGroen" and x == True and self.turn_player == "player1":
                            if self.row >= 17:
                                print("Oops you went out the playfield, Try again!")
                            elif self.grid[self.row][self.column] == 1 or self.grid[self.row + 1][self.column] == 1 or self.grid[self.row + 2][self.column] == 1:
                                print("Oops there is already a boat here, Try again!")
                            else:
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
                                time.sleep(1)

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
                                time.sleep(1)

                        elif self.boat == "DrieGeel" and v == True and self.turn_player == "player2":
                            if self.row == 20:
                                print("Oops you went out the playfield, Try again!")
                            else:
                                self.grid[self.row][self.column] = 2
                                self.grid[self.row - 1][self.column] = 2
                                self.grid[self.row - 2][self.column] = 2
                                self.Player2.Furgo.pos_row = self.row -2
                                self.Player2.Furgo.pos_column = self.column
                                self.boat = ""
                                v = False
                                time.sleep(1)

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
                                time.sleep(1)


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
                                time.sleep(1)

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
                                time.sleep(1)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                self.pause = False
            if keys[pygame.K_p]:
                self.pause = True
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
            elif self.Player1.Furgo.pos_off == False and self.boat == "DrieGroenDef" and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
                self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 1
                self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +1] = 1
                self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +2] = 1
                self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 3
                self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 3
            elif self.Player1.Furgo.pos_off == True and self.boat == "DrieGroenOff" and self.Player1.Furgo.hp != 0 and self.turn_player == "player1":
                self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +1] = 3
                self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column +2] = 3
                self.grid[self.Player1.Furgo.pos_row +1][self.Player1.Furgo.pos_column] = 1
                self.grid[self.Player1.Furgo.pos_row +2][self.Player1.Furgo.pos_column] = 1
                self.grid[self.Player1.Furgo.pos_row][self.Player1.Furgo.pos_column] = 1
                self.Player1.Furgo.moves -= 1
                time.sleep(1)
            elif self.Player1.Furgo.hp == 0 and self.grid[self.Player1.Furgo.pos_row + 2][self.Player1.Furgo.pos_column] != 3:
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
            elif self.Player1.Intensity.pos_off == False and self.boat == "Vier1GroenDef" and self.Player1.Intensity.hp != 0 and self.turn_player == "player1":
                self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 1
                self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +1] = 1
                self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +2] = 1
                self.grid[self.Player1.Intensity.pos_row ][self.Player1.Intensity.pos_column +3] = 1
                self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column] = 3
                self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column] = 3
                self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] = 3
            elif self.Player1.Intensity.pos_off == True and self.boat == "Vier1GroenOff" and self.Player1.Intensity.hp != 0 and self.turn_player == "player1":
                self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +1] = 3
                self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column +2] = 3
                self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column + 3] = 3
                self.grid[self.Player1.Intensity.pos_row +1][self.Player1.Intensity.pos_column] = 1
                self.grid[self.Player1.Intensity.pos_row +2][self.Player1.Intensity.pos_column] = 1
                self.grid[self.Player1.Intensity.pos_row +3][self.Player1.Intensity.pos_column] = 1
                self.grid[self.Player1.Intensity.pos_row][self.Player1.Intensity.pos_column] = 1
            elif self.Player1.Intensity.hp == 0 and self.grid[self.Player1.Intensity.pos_row + 3][self.Player1.Intensity.pos_column] != 3:
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
            elif keys[pygame.K_RIGHT] and self.boat == "Vier2Groen" and not self.Player1.Silver.pos_column == 19 and self.Player1.Silver.pos_off == True and self.turn_player == "player1":
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
            elif keys[pygame.K_LEFT] and self.boat == "Vier2Groen" and not self.Player1.Silver.pos_column == 0 and self.Player1.Silver.pos_off == True and self.turn_player == "player1":
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
            elif self.Player1.Silver.pos_off == False and self.boat == "Vier2GroenDef" and self.turn_player == "player1":
                self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 1
                self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +1] = 1
                self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +2] = 1
                self.grid[self.Player1.Silver.pos_row ][self.Player1.Silver.pos_column +3] = 1
                self.grid[self.Player1.Silver.pos_row +1][self.Player1.Silver.pos_column] = 3
                self.grid[self.Player1.Silver.pos_row +2][self.Player1.Silver.pos_column] = 3
                self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] = 3
            elif self.Player1.Silver.pos_off == True and self.boat == "Vier2GroenOff" and self.turn_player == "player1":
                self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +1] = 3
                self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column +2] = 3
                self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column + 3] = 3
                self.grid[self.Player1.Silver.pos_row +1][self.Player1.Silver.pos_column] = 1
                self.grid[self.Player1.Silver.pos_row +2][self.Player1.Silver.pos_column] = 1
                self.grid[self.Player1.Silver.pos_row +3][self.Player1.Silver.pos_column] = 1
                self.grid[self.Player1.Silver.pos_row][self.Player1.Silver.pos_column] = 1
            elif self.Player1.Silver.hp == 0 and self.grid[self.Player1.Silver.pos_row + 3][self.Player1.Silver.pos_column] != 3:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
            elif self.Player1.Merapi.pos_off == False and self.boat == "VijfGroenDef" and self.turn_player == "player1":
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 1
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 1] = 1
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 2] = 1
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 3] = 1
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 4] = 1
                self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 3
                self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 3
                self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 3
                self.grid[self.Player1.Merapi.pos_row+ 4][self.Player1.Merapi.pos_column ] = 3
            elif self.Player1.Merapi.pos_off == True and self.boat == "VijfGroenOff" and self.turn_player == "player1":
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 1] = 3
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 2] = 3
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 3] = 3
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column + 4] = 3
                self.grid[self.Player1.Merapi.pos_row + 1][self.Player1.Merapi.pos_column] = 1
                self.grid[self.Player1.Merapi.pos_row + 2][self.Player1.Merapi.pos_column] = 1
                self.grid[self.Player1.Merapi.pos_row + 3][self.Player1.Merapi.pos_column] = 1
                self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] = 1
                self.grid[self.Player1.Merapi.pos_row][self.Player1.Merapi.pos_column] = 1
            elif self.Player1.Merapi.hp == 0 and self.grid[self.Player1.Merapi.pos_row + 4][self.Player1.Merapi.pos_column] != 3:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
            elif self.Player2.Furgo.pos_off == False and self.boat == "DrieGeelDef" and self.Player2.Furgo.hp != 0 and self.turn_player == "player2":
                self.grid[self.Player2.Furgo.pos_row+2][self.Player2.Furgo.pos_column] = 2
                self.grid[self.Player2.Furgo.pos_row+2][self.Player2.Furgo.pos_column + 1] = 2
                self.grid[self.Player2.Furgo.pos_row+2][self.Player2.Furgo.pos_column + 2] = 2
                self.grid[self.Player2.Furgo.pos_row + 1][self.Player2.Furgo.pos_column] = 3
                self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column] = 3
            elif self.Player2.Furgo.pos_off == True and self.boat == "DrieGeelOff" and self.Player2.Furgo.hp != 0 and self.turn_player == "player2":
                self.grid[self.Player2.Furgo.pos_row +2][self.Player2.Furgo.pos_column + 1] = 3
                self.grid[self.Player2.Furgo.pos_row+2][self.Player2.Furgo.pos_column + 2] = 3
                self.grid[self.Player2.Furgo.pos_row + 1][self.Player2.Furgo.pos_column] = 2
                self.grid[self.Player2.Furgo.pos_row + 2][self.Player2.Furgo.pos_column] = 2
                self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column] = 2
            elif self.Player2.Furgo.hp == 0 and self.grid[self.Player2.Furgo.pos_row][self.Player2.Furgo.pos_column] != 3:
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
            elif self.Player2.Intensity.pos_off == False and self.boat == "Vier1GeelDef" and self.Player2.Intensity.hp != 0 and self.turn_player == "player2":
                self.grid[self.Player2.Intensity.pos_row +3][self.Player2.Intensity.pos_column] = 2
                self.grid[self.Player2.Intensity.pos_row+3][self.Player2.Intensity.pos_column + 1] = 2
                self.grid[self.Player2.Intensity.pos_row+3][self.Player2.Intensity.pos_column + 2] = 2
                self.grid[self.Player2.Intensity.pos_row+3][self.Player2.Intensity.pos_column + 3] = 2
                self.grid[self.Player2.Intensity.pos_row + 1][self.Player2.Intensity.pos_column] = 3
                self.grid[self.Player2.Intensity.pos_row + 2][self.Player2.Intensity.pos_column] = 3
                self.grid[self.Player2.Intensity.pos_row][self.Player2.Intensity.pos_column] = 3
            elif self.Player2.Intensity.pos_off == True and self.boat == "Vier1GeelOff" and self.Player2.Intensity.hp != 0 and self.turn_player == "player2":
                self.grid[self.Player2.Intensity.pos_row +3][self.Player2.Intensity.pos_column + 1] = 3
                self.grid[self.Player2.Intensity.pos_row+3][self.Player2.Intensity.pos_column + 2] = 3
                self.grid[self.Player2.Intensity.pos_row+3][self.Player2.Intensity.pos_column + 3] = 3
                self.grid[self.Player2.Intensity.pos_row + 1][self.Player2.Intensity.pos_column] = 2
                self.grid[self.Player2.Intensity.pos_row + 2][self.Player2.Intensity.pos_column] = 2
                self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column] = 2
                self.grid[self.Player2.Intensity.pos_row][self.Player2.Intensity.pos_column] = 2
            elif self.Player2.Intensity.hp == 0 and self.grid[self.Player2.Intensity.pos_row + 3][self.Player2.Intensity.pos_column] != 3:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
            elif self.Player2.Silver.pos_off == False and self.boat == "Vier2GeelDef" and self.Player2.Silver.hp != 0 and self.turn_player == "player2":
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] = 2
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column + 1] = 2
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column + 2] = 2
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column + 3] = 2
                self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column] = 3
                self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column] = 3
                self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column] = 3
            elif self.Player2.Silver.pos_off == True and self.boat == "Vier2GeelOff" and self.Player2.Silver.hp != 0 and self.turn_player == "player2":
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column + 1] = 3
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column + 2] = 3
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column + 3] = 3
                self.grid[self.Player2.Silver.pos_row + 1][self.Player2.Silver.pos_column] = 2
                self.grid[self.Player2.Silver.pos_row + 2][self.Player2.Silver.pos_column] = 2
                self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] = 2
                self.grid[self.Player2.Silver.pos_row][self.Player2.Silver.pos_column] = 2
            elif self.Player2.Silver.hp == 0 and self.grid[self.Player2.Silver.pos_row + 3][self.Player2.Silver.pos_column] != 3:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
            elif self.Player2.Merapi.pos_off == False and self.boat == "VijfGeelDef" and self.turn_player == "player2":
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column] = 2
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 1] = 2
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 2] = 2
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 3] = 2
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 4] = 2
                self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 3
                self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 3
                self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 3
                self.grid[self.Player2.Merapi.pos_row ][self.Player2.Merapi.pos_column] = 3
            elif self.Player2.Merapi.pos_off == True and self.boat == "VijfGeelOff" and self.turn_player == "player2":
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 1] = 3
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 2] = 3
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 3] = 3
                self.grid[self.Player2.Merapi.pos_row+4][self.Player2.Merapi.pos_column + 4] = 3
                self.grid[self.Player2.Merapi.pos_row + 1][self.Player2.Merapi.pos_column] = 2
                self.grid[self.Player2.Merapi.pos_row + 2][self.Player2.Merapi.pos_column] = 2
                self.grid[self.Player2.Merapi.pos_row + 3][self.Player2.Merapi.pos_column] = 2
                self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] = 2
                self.grid[self.Player2.Merapi.pos_row][self.Player2.Merapi.pos_column] = 2
            elif self.Player2.Merapi.hp == 0 and self.grid[self.Player2.Merapi.pos_row + 4][self.Player2.Merapi.pos_column] != 3:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('mortal_kombat_fatality.ogg')
                pygame.mixer.music.play()
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
                    if self.grid[self.row][self.column] == 2:
                        color0 = self.YELLOW
                    if self.grid[self.row][self.column] == 4:
                        color0 = self.RED
                    pygame.draw.rect(self.screen, color0,
                                     [(self.MARGIN + self.WIDTH) * self.column + 200 + self.MARGIN,
                                      (self.MARGIN + self.HEIGHT) * self.row + self.MARGIN, self.WIDTH,
                                      self.HEIGHT])
            if self.turn_player == "player1":
            ###1/8
                if self.hehe == 2:
                    self.FireFurgoY = self.Player1.Furgo.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireFurgoX = self.Player1.Furgo.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x = self.FireFurgoX
                if self.boat == "DrieGroen" and keys[pygame.K_a] and self.hehe == 2:
                    self.hehe = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "DrieGroen" and keys[pygame.K_d] and self.hehe == 2:
                    self.hehe = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                    (self.x_x, self.FireFurgoY, 50, (55 * self.Player1.Furgo.length)), 0)

                    self.exdee += 1
                    self.x_x -= 1
                    if self.Player1.Furgo.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2 or self.Player1.Furgo.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Furgo.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    if self.exdee == (self.Player1.Furgo.atk_range * 55):
                        self.hehe = 3
                if self.hehe == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x, self.FireFurgoY, 50, (55 * self.Player1.Furgo.length)), 0)
                    self.exdee += 1
                    self.x_x += 1
                    if self.Player1.Furgo.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2 or self.Player1.Furgo.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Furgo.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    if self.exdee == (self.Player1.Furgo.atk_range * 55):
                        self.hehe = 3

                ###2/8
                if self.hehe2 == 2:
                    self.FireIntensityY = self.Player1.Intensity.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireIntensityX = self.Player1.Intensity.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x1 = self.FireIntensityX
                if self.boat == "Vier1Groen" and keys[pygame.K_a] and self.hehe2 == 2:
                    self.hehe2 = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "Vier1Groen" and keys[pygame.K_d] and self.hehe2 == 2:
                    self.hehe2 = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe2 == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x1, self.FireIntensityY, 50, (55 * self.Player1.Intensity.length)), 0)

                    self.exdee2 += 1
                    self.x_x1 -= 1
                    if self.Player1.Intensity.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3 or self.Player1.Intensity.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Intensity.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    if self.exdee2 == (self.Player1.Intensity.atk_range * 55):
                        self.hehe2 = 3
                if self.hehe2 == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x1, self.FireIntensityY, 50, (55 * self.Player1.Intensity.length)), 0)
                    self.exdee2 += 1
                    self.x_x1 += 1
                    if self.Player1.Intensity.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3 or self.Player1.Intensity.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Intensity.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    if self.exdee2 == (self.Player1.Intensity.atk_range * 55):
                        self.hehe2 = 3

                ###3/8
                if self.hehe3 == 2:
                    self.FireSilverY = self.Player1.Silver.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireSilverX = self.Player1.Silver.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x2 = self.FireSilverX
                if self.boat == "Vier2Groen" and keys[pygame.K_a] and self.hehe3 == 2:
                    self.hehe3 = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "Vier2Groen" and keys[pygame.K_d] and self.hehe3 == 2:
                    self.hehe3 = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe3 == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x2, self.FireSilverY, 50, (55 * self.Player1.Silver.length)), 0)

                    self.exdee3 += 1
                    self.x_x2 -= 1
                    if self.Player1.Silver.pos_column - 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 3 or self.Player1.Silver.pos_column - 1 == self.Player2.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Silver.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    if self.exdee3 == (self.Player1.Silver.atk_range * 55):
                        self.hehe3 = 3
                if self.hehe3 == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x2, self.FireSilverY, 50, (55 * self.Player1.Silver.length)), 0)
                    self.exdee3 += 1
                    self.x_x2 += 1
                    if self.Player1.Silver.pos_column + 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 3 or self.Player1.Silver.pos_column + 1 == self.Player2.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Silver.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    if self.exdee3 == (self.Player1.Silver.atk_range * 55):
                        self.hehe3 = 3
            else:
                ###4/8
                if self.hehe4 == 2:
                    self.FireMerapiY = self.Player1.Merapi.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireMerapiX = self.Player1.Merapi.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x3 = self.FireMerapiX
                if self.boat == "VijfGroen" and keys[pygame.K_a] and self.hehe4 == 2:
                    self.hehe4 = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "VijfGroen" and keys[pygame.K_d] and self.hehe4 == 2:
                    self.hehe4 = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe4 == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x3, self.FireMerapiY, 50, (55 * self.Player1.Merapi.length)), 0)

                    self.exdee4 += 1
                    self.x_x3 -= 1
                    if self.Player1.Merapi.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4 or self.Player1.Merapi.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Merapi.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    if self.exdee4 == (self.Player1.Merapi.atk_range * 55):
                        self.hehe4 = 3
                if self.hehe4 == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x3, self.FireMerapiY, 50, (55 * self.Player1.Merapi.length)), 0)
                    self.exdee4 += 1
                    self.x_x3 += 1
                    if self.Player1.Merapi.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4 or self.Player1.Merapi.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Merapi.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    if self.exdee4 == (self.Player1.Merapi.atk_range * 55):
                        self.hehe4 = 3

            ###5/8
            if self.hehe5 == 2:
                self.FireFurgoYGeel = self.Player2.Furgo.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireFurgoX = self.Player2.Furgo.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x4 = self.FireFurgoX
            if self.boat == "DrieGeel" and keys[pygame.K_a] and self.hehe5 == 2:
                self.hehe5 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "DrieGeel" and keys[pygame.K_d] and self.hehe5 == 2:
                self.hehe5 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe5 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x4, self.FireFurgoYGeel, 50, (55 * self.Player2.Furgo.length)), 0)

                self.exdee5 += 1
                self.x_x4 -= 1
                if self.Player2.Furgo.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2 or self.Player2.Furgo.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Furgo.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                if self.exdee5 == (self.Player2.Furgo.atk_range * 55):
                    self.hehe5 = 3
            if self.hehe5 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x4, self.FireFurgoYGeel, 50, (55 * self.Player2.Furgo.length)), 0)
                self.exdee5 += 1
                self.x_x4 += 1
                if self.Player2.Furgo.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2 or self.Player2.Furgo.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Furgo.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                if self.exdee5 == (self.Player2.Furgo.atk_range * 55):
                    self.hehe5 = 3

            ###6/8
            if self.hehe6 == 2:
                self.FireIntensityYGeel = self.Player2.Intensity.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireIntensityX = self.Player2.Intensity.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x5 = self.FireIntensityX
            if self.boat == "Vier1Geel" and keys[pygame.K_a] and self.hehe6 == 2:
                self.hehe6 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "Vier1Geel" and keys[pygame.K_d] and self.hehe6 == 2:
                self.hehe6 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe6 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x5, self.FireIntensityYGeel, 50, (55 * self.Player2.Intensity.length)), 0)

                self.exdee6 += 1
                self.x_x5 -= 1
                if self.Player2.Intensity.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3 or self.Player2.Intensity.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Intensity.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                if self.exdee6 == (self.Player2.Intensity.atk_range * 55):
                    self.hehe6 = 3
            if self.hehe6 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x5, self.FireIntensityYGeel, 50, (55 * self.Player1.Intensity.length)), 0)
                self.exdee6 += 1
                self.x_x5 += 1
                if self.Player2.Intensity.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3 or self.Player2.Intensity.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Intensity.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                if self.exdee6 == (self.Player1.Intensity.atk_range * 55):
                    self.hehe6 = 3

            ###7/8
            if self.hehe7 == 2:
                self.FireSilverYGeel = self.Player2.Silver.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireSilverX = self.Player2.Silver.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x6 = self.FireSilverX
            if self.boat == "Vier2Geel" and keys[pygame.K_a] and self.hehe7 == 2:
                self.hehe7 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "Vier2Geel" and keys[pygame.K_d] and self.hehe7 == 2:
                self.hehe7 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe7 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x6, self.FireSilverYGeel, 50, (55 * self.Player2.Silver.length)), 0)

                self.exdee7 += 1
                self.x_x6 -= 1
                if self.Player2.Silver.pos_column - 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3 or self.Player2.Silver.pos_column - 1 == self.Player1.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Silver.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                if self.exdee7 == (self.Player2.Silver.atk_range * 55):
                    self.hehe7 = 3
            if self.hehe7 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x6, self.FireSilverYGeel, 50, (55 * self.Player2.Silver.length)), 0)
                self.exdee7 += 1
                self.x_x6 += 1
                if self.Player2.Silver.pos_column + 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3 or self.Player2.Silver.pos_column + 1 == self.Player1.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 3:
                    self.Player1.Silver.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                if self.exdee7 == (self.Player2.Silver.atk_range * 55):
                    self.hehe7 = 3

            ###8/8
            if self.hehe8 == 2:
                self.FireMerapiYGeel = self.Player2.Merapi.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireMerapiX = self.Player2.Merapi.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x7 = self.FireMerapiX
            if self.boat == "VijfGeel" and keys[pygame.K_a] and self.hehe8 == 2:
                self.hehe8 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "VijfGeel" and keys[pygame.K_d] and self.hehe8 == 2:
                self.hehe8 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe8 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x7, self.FireMerapiYGeel, 50, (55 * self.Player2.Merapi.length)), 0)

                self.exdee8 += 1
                self.x_x7 -= 1
                if self.Player2.Merapi.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4 or self.Player2.Merapi.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Merapi.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                if self.exdee8 == (self.Player2.Merapi.atk_range * 55):
                    self.hehe8 = 3
            if self.hehe8 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x7, self.FireMerapiYGeel, 50, (55 * self.Player2.Merapi.length)), 0)
                self.exdee8 += 1
                self.x_x7 += 1
                if self.Player2.Merapi.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4 or self.Player2.Merapi.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Merapi.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                if self.exdee8 == (self.Player2.Merapi.atk_range * 55):
                    self.hehe8 = 3

            gameplaybg = pygame.image.load(
                "gamecard.png")  # game card loaden en printen -------------------------------------------------------------------------------------------------------------------------
            self.screen.blit(gameplaybg, [1210, 400])

            pos = pygame.mouse.get_pos()
            press = pygame.mouse.get_pressed()
            if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 620 and pos[1] <= 675:
                print("start Card #1", p1, random.choice(cards))
                print("start Card #2", p1, random.choice(cards))
                self.lexD = 2
            if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1417 and pos[1] >= 710 and pos[1] <= 775:
                print("Normal Card #1", p1, random.choice(cards))
                self.lexD1 = 1

            if press[0] == 1 and pos[0] >= 1790 and pos[0] <= 1887 and pos[1] >= 620 and pos[1] <= 675:
                print("start Card #1", p2, random.choice(cards))
                print("start Card #2", p2, random.choice(cards))
                self.lexD2 = 1

            if press[0] == 1 and pos[0] >= 1790 and pos[0] <= 1887 and pos[1] >= 510 and pos[1] <= 575:
                print("Normal Card #1", p1, random.choice(cards))
                self.lexD3 = 1

            if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1420 and pos[1] >= 780 and pos[1] <= 780 + 50:
                self.Player1.Furgo.hp += 1
                time.sleep(0.5)

            else:
                if press[0] == 1 and pos[0] >= 1320 and pos[0] <= 1420 and pos[1] >= 780 and pos[1] <= 780 + 50:
                    self.Player1.Furgo.hp += 1
                    time.sleep(0.5)

            if 1320 + 100 > pos[0] > 1320 and 780 + 50 > pos[1] > 780:
                pygame.draw.rect(self.screen, self.bright_red, (1320, 780, 100, 50))
                self.screen.blit(self.usecard, [1330, 790])


            else:
                pygame.draw.rect(self.screen, (255,0,255), (1320, 780, 100, 50))
                self.screen.blit(self.usecard, [1330, 790])

            print(self.Player1.Furgo.hp)

        else:
            button(1720, 100, 50, 50, back_game)












    def draw(self):
        global color, color1, color2, color3, color4, color5, color6, color7, pause, bright_green, color9, green2, YELLOW2
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.bright_yew = (255, 255, 0)
        self.bright_red = (255, 0, 0)
        self.bright_green = (0, 255, 0)

        if Pause == True:
            self.start_text = self.font.render("Instructions",
                                               1, (255, 255, 255))
            self.screen.blit(self.start_text, (1700, 16))

            self.exit_text = self.font.render("Back to main menu",
                                              1, (255, 255, 255))
            self.screen.blit(self.exit_text, (1700, 84))

            self.exit_text = self.font.render("Exit Game",
                                              1, (255, 255, 255))
            self.screen.blit(self.exit_text, (1700, 50))
            self.exit_text = self.font.render("Pause",
                                              1, (255, 255, 255))
            self.screen.blit(self.exit_text, (1700, 118))
            self.start1_text = self.font.render("End turn",
                                                           1, (255, 255, 255))
            self.screen.blit(self.start1_text, (1350, 16))

            self.start2_text = self.font.render(str(self.turn_player) + " Turn: "   + str(self.turn),
                                                           1, (255, 255, 255))
            self.screen.blit(self.start2_text, (1350, 50))

            if not self.turn > 2:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (1310, 190, 580, 310), 5)

            pygame.draw.rect(self.screen, (200, 10, 0),
                             (1310, 190, 580, 60), 0)


            pygame.draw.rect(self.screen, (125, 0, 0),
                             (1310, 250, 580, 250), 0)

            pygame.draw.line(self.screen, self.WHITE,
                             (1310, 250 ), (1890, 250), 4)

            self.start_text = self.titlefont.render("Hints!!",
                                               1, (255, 255, 255))
            self.screen.blit(self.start_text, (1500, 180))

            if self.turn == 1 and x == True and self.turn_player == "player1" or self.turn == 1 and y == True and self.turn_player == "player1" or self.turn == 1 and z == True and self.turn_player == "player1" or self.turn == 1 and u == True and self.turn_player == "player1":
                self.start_text = self.font.render("Place your boats now Player 1!",
                                                   1, (255, 255, 255))
                self.screen.blit(self.start_text, (1400, 300))
            elif self.turn == 1 and x == False and y == False and z == False and u == False and self.turn_player == "player1":
                self.start_text = self.font.render("Press end turn if you have finished your turn!",
                                                   1, (255, 255, 255))
                self.screen.blit(self.start_text, (1350, 300))
            elif self.turn == 1 and w == True or self.turn == 1 and v == True and self.turn_player == "player2" or self.turn == 1 and t == True and self.turn_player == "player2" or self.turn == 1 and s == True and self.turn_player == "player2":
                self.start_text = self.font.render("Place your boats now Player 2!",
                                                   1, (255, 255, 255))
                self.screen.blit(self.start_text, (1400, 300))
            elif self.turn == 1 and w == False and v == False and t == False and s == False and self.turn_player == "player2":
                self.start_text = self.font.render("Press end turn if you have finished your turn!",
                                                   1, (255, 255, 255))
                self.screen.blit(self.start_text, (1350, 300))
            elif self.turn == 2 and self.turn_player == "player1" or self.turn == 2 and self.turn_player == "player2":
                self.start_text = self.font.render("Press A to attack to the left of your selected boat",
                                                   1, (255, 255, 255))
                self.screen.blit(self.start_text, (1320, 300))
                self.start_text = self.font.render("Press D to attack to the right of your selected boat",
                                                   1, (255, 255, 255))
                self.screen.blit(self.start_text, (1320, 400))
            if self.turn > 2:
                if self.w < 255:
                    self.square = pygame.image.load("Black.PNG")
                    self.square.set_alpha(self.w)
                    self.screen.blit(self.square, (1310, 190))
                    self.w += 1
                else:
                    self.screen.blit(self.square, (1310, 190))

            # kaart button text
            self.textcard5 = self.font3.render("P1 CARDS",
                                               1, (255, 255, 255))
            self.textcard6 = self.font3.render(" P1 start cards", 1, (255, 255, 255))
            self.textcard7 = self.font3.render("NORMAL", 1, (255, 255, 255))
            self.textcard8 = self.font3.render(" P1 -- (1 CARD)", 1, (255, 255, 255))

            self.textcard9 = self.font3.render(" P2 START CARD", 1, (255, 255, 255))
            self.textcard10 = self.font3.render(" P2 -- (1 CARD)", 1, (255, 255, 255))

            self.textcard11 = self.font3.render("P2 CARDS",
                                               1, (255, 255, 255))

            # kaart text menu tekenen ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            self.screen.blit(self.textcard1, [1310, 780])
            self.screen.blit(self.textcard3, [1300, 850])
            self.screen.blit(self.textcard4, [1300, 950])

            self.screen.blit(self.textcard9, [1790, 710])
            self.screen.blit(self.textcard10, [1790, 600])
            # self.screen.blit(self.textcard5, [1320,725])


            press = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            boat3 = self.screen.blit(self.ship1, (130,250))
            if press[0] == 1 and pos[0] >= 1700 and pos[0] <= 1800 and pos[1] >= 118 and pos[1] <= 155:
                self.pause = True
            if self.pause == True:
                if press[0] == 1 and pos[0] >= 400 and pos[0] <= 1400 and pos[1] >= 800 and pos[1] <= 950:
                    self.pause = False
            if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 250 and pos[
                1] <= 360 and self.turn_player == "player1":
                self.ship1 = self.blank

            boat4 = self.screen.blit(self.ship2, (130, 50))
            if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 40 and pos[
                1] <= 180 and self.turn_player == "player1":
                self.ship2 = self.blank

            boat4x = self.screen.blit(self.ship3, (50, 50))
            if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 50 and pos[
                1] <= 190 and self.turn_player == "player1":
                self.ship3 = self.blank

            boat5 = self.screen.blit(self.ship5, (50, 250))
            if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 250 and pos[
                1] <= 450 and self.turn_player == "player1":
                self.ship5 = self.blank

            boat33 = self.screen.blit(self.ship6, (130, 650))
            if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 650 and pos[
                1] <= 760 and self.turn_player == "player2":
                self.ship6 = self.blank

            boat44 = self.screen.blit(self.ship7, (130, 890))
            if press[0] == 1 and pos[0] >= 130 and pos[0] <= 170 and pos[1] >= 890 and pos[
                1] <= 1030 and self.turn_player == "player2":
                self.ship7 = self.blank

            boat44x = self.screen.blit(self.ship8, (50, 890))
            if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 890 and pos[
                1] <= 1030 and self.turn_player == "player2":
                self.ship8 = self.blank

            boat55 = self.screen.blit(self.ship9, (50, 650))
            if press[0] == 1 and pos[0] >= 50 and pos[0] <= 90 and pos[1] >= 650 and pos[
                1] <= 850 and self.turn_player == "player2":
                self.ship9 = self.blank

            if 1320 + 100 > pos[0] > 1300 and 725 + 50 > pos[1] > 725:

                pygame.draw.rect(self.screen, bright_green, (1320, 725, 100, 50))
                self.screen.blit(self.textcard7, [1335, 740])
                self.screen.blit(self.textcard6, [1318, 700])
            else:
                pygame.draw.rect(self.screen, green2, (1320, 725, 100, 50))
                self.screen.blit(self.textcard5, [1335, 740])
                self.screen.blit(self.textcard6, [1318, 700])

                #   select cards button   normal cards    player 1 - 1 kaart kiezen

            if 1320 + 100 > pos[0] > 1300 and 630 + 50 > pos[1] > 630:
                pygame.draw.rect(self.screen, bright_green, (1320, 630, 100, 50))
                self.screen.blit(self.textcard7, [1335, 640])
                self.screen.blit(self.textcard8, [1318, 605])


            else:
                pygame.draw.rect(self.screen, green2, (1320, 630, 100, 50))
                self.screen.blit(self.textcard5, [1335, 640])
                self.screen.blit(self.textcard8, [1318, 605])


            if 1790 + 100 > pos[0] > 1790 and 740 + 50 > pos[1] > 700:

                pygame.draw.rect(self.screen, bright_green, (1790, 730, 100, 50))
                self.screen.blit(self.textcard7, [1790, 740])
            else:
                pygame.draw.rect(self.screen, green2, (1790, 730, 100, 50))
                self.screen.blit(self.textcard11, [1790, 740])

                #   select cards button   normal cards    player 1 - 1 kaart kiezen

            if 1790 + 100 > pos[0] > 1780 and 630 + 50 > pos[1] > 630:
                pygame.draw.rect(self.screen, bright_green, (1790, 630, 100, 50))
                self.screen.blit(self.textcard7, [1790, 640])


            else:
                pygame.draw.rect(self.screen, green2, (1790, 630, 100, 50))
                self.screen.blit(self.textcard11, [1790, 640])

            if self.lexD == 2:
                self.screen.blit(self.p1k3, [1685, 803])
            if self.lexD1 == 1:
                self.screen.blit(self.p1k1, [1400, 803])
                self.screen.blit(self.p1k2, [1560, 803])
            if self.lexD2 == 1:
                screen.blit(p2k1, [1380, 903])
                screen.blit(p2k2, [1560, 903])
            if self.lexD3 == 1:
                screen.blit(p2k3, [1740, 903])


                # kaart klikken voor kaart ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        elif Pause == False:
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

            self.start_text = self.font.render("-Aan het begin van elke beurt trekt de speler aan beurt een kaart..",
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


        if self.pause == True:

            # background
            global bgrandom

            if bgrandom == 1:
                bg = pygame.image.load("background3.jpg")
            else:
                bg = pygame.image.load("background3.jpg")
            self.screen.blit(bg, (0, 0))
            # title
            self.start_text = self.fontTitle2.render("PAUSED",
                                                     1, (255, 255, 255))
            self.screen.blit(self.start_text, (400, 100))
            # start game tekst voor knop
            self.start_text = self.font1.render("Press 'C' to Continue or",
                                                1, (255, 255, 255))
            self.screen.blit(self.start_text, (550, 700))
            # exit game tekst voor knop
            self.start_textt = self.fontTitle.render("'CLICK HERE'",
                                                     1, (255, 255, 255))
            self.screen.blit(self.start_textt, (500, 800))

        pygame.display.flip()





    def game_loop(self):
        #game functionality loop
        while not process_events():
            self.update()
            self.draw()
            pos = pygame.mouse.get_pos()
            if self.turn_player == "player1":
                self.player1_turn()
            else:
                self.player2_turn()
            if self.Player1.Furgo.hp == 0 and self.Player1.Intensity.hp == 0 and self.Player1.Silver.hp == 0 and self.Player1.Merapi.hp == 0 or self.Player2.Furgo.hp == 0 and self.Player2.Intensity.hp == 0 and self.Player2.Silver.hp == 0 and self.Player2.Merapi.hp == 0:
                program_victory()
                insert_db(self.turn, "Game " + str(int(haalnummereruit()) + 1) + " ")
                update_dbx(str(int(haalnummereruit()) + 1))

            if self.game_quit == True:
                break

            if game_quit == True:
                break

        else:
            quit()

    def rules_loop(self):
        while not process_events():
            self.update_rules()
            self.draw_rules()
            if quit_check == True:
                break

class HighscoreScreen:
    def __init__(self):
        width = 1300
        height = 1000
        size = ( width , height )
        self.screen = pygame.display.set_mode(size)
        self.bg = pygame.image.load("rules_background.jpg")
        self.bg = self.bg.convert()
        self.font = pygame.font.Font("Capture_It.ttf",50)
        self.highscore_quit = True

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        self.defaultfont = pygame.font.get_default_font()
        self.fontrenderer = pygame.font.Font(self.defaultfont,30)
        self.highscorerender = pygame.font.Font(self.defaultfont,80)
        self.z=200
        self.b = 1
        self.a = show_scores()
        for x in self.a:
            g = self.fontrenderer.render(x,1,white)
            nummer = self.fontrenderer.render(str(self.b)+".",1,white)
            self.screen.blit(g,(500,self.z))
            self.screen.blit(nummer,(457,self.z))
            self.z+=50
            self.b+=1
        pygame.display.set_caption('HighScore')
        label3 = self.highscorerender.render("HighScore",1,white)
        self.screen.blit(label3,(483,50))

        self.start_text = self.font.render(
            "Main Menu",
            1, (255, 255, 255))
        self.screen.blit(self.start_text, (500, 750))


        pygame.display.flip()

    def update(self):
        button(500, 750, 275, 50, program)

    def highscore_loop(self):
        global highscore_quit
        while process_events() == False:
            self.update()
            self.draw()
            if self.highscore_quit == False:
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

        pygame.mixer.init()
        pygame.mixer.music.load("endscreen.ogg")
        pygame.mixer.music.play()


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
        button(800 ,700, 300 ,50, program_highscore)
        button(150, 700, 300, 50, program)
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

        self.Furgo = Boat(2, 3, 2, 1, 3)
        self.Intensity = Boat(3, 2, 3, 1, 4)
        self.Silver = Boat(3, 2, 3, 1, 4)
        self.Merapi = Boat(4, 1, 4, 1, 5)

class Boat:
    def __init__(self, hp, moves, atk_range, atk_damage, length):
        self.hp = hp
        self.moves = moves
        self.atk_range = atk_range
        self.atk_damage = atk_damage
        self.pos_off = True
        self.boat = ""
        self.pos_row = 0
        self.pos_column = 0
        self.length = length



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
    global Pause
    Pause = False

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

    game.Player1.Furgo = Boat(2, 3, 2, 1, 3)
    game.Player1.Intensity = Boat(3, 2, 3, 1, 4)
    game.Player1.Silver = Boat(3, 2, 3, 1, 4)
    game.Player1.Merapi = Boat(4, 1, 4, 1, 5)

    game.Player2.Furgo = Boat(2, 3, 2, 1, 3)
    game.Player2.Intensity = Boat(3, 2, 3, 1, 4)
    game.Player2.Silver = Boat(3, 2, 3, 1, 4)
    game.Player2.Merapi = Boat(4, 1, 4, 1, 5)

    game.Player1.score = 0

    game.Player2.score = 0

    game.turn = 1

    game.turn_player = "player1"

    game.game_quit = False

    game.game_loop()

def programAI():
    menu = Menu()
    menu.AI_troll()
    menu.AI_loop()

def program_highscore():
    game = Game()
    game.game_quit = True
    highscore = HighscoreScreen()
    highscore.highscore = True
    highscore.highscore_loop()

def back_game():
    global Pause
    Pause = True




#aanroepen van startup functie
program()

