class Menu:
    def __init__(self):
        global color, color1, color2, color3, color4, color5, color6, color7, green, YELLOW, bgrandommusic
        # schermgrootte
        width = 1920
        heigth = 1080
        size = (width, heigth)

        self.screen = pygame.display.set_mode(size)
        # title font
        self.fontTitle = pygame.font.Font("Capture_it_2.ttf", 150)
        # start en exit font
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

        self.screen.blit(bg, (0, 0))
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
        # buttons aanmaken met button functie
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
        while not process_events():
            self.AI_screen()

    def menu_loop(self):
        global quit_checkmenu

        Menu.BgMusic(self)

        # menu functionality loop
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

        # schermgrootte
        width = 1920
        height = 1050
        size = (width, height)

        self.Player1 = Player("Henk", "Groen")
        self.Player2 = Player("Joost", "Geel")

        # font
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
        self.hehe = 2
        self.exdee = 0
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