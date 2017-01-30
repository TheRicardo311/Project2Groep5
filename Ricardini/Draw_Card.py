


bgMusic = ['C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/Castlevania2-BloodyTears.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/Castlevania-SymphonyoftheNight-Dracula.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/FinalFantasyII-NFC--DeadMusic.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/FinalFantasyII-NFC--PandemoniumCastle.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/LeagueOfLegendsMusic-BitRush.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/LegendOfZeldaIntro.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/LegendOfZeldaTheme.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/MarioTheme.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/PokemonTheme.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusicSkyrimTheme.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/Undertale-Megalovania.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/Undertale-SpiderDanceExtended.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/Zelda2-TheAdventureOfLink-Palace.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/bgmusic1.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/bgmusic2.ogg', 'C:/Users/Ricardo/Documents/GitHub/Project2Groep5/Ricardini/8-bitMusic/bgmusic3.ogg']

def BgMusic(self, bgMusic):

    Random_bgMusic = random.choice(bgMusic)
    pygame.mixer.init()
    pygame.mixer.music.load(Random_bgMusic)
    pygame.mixer.music.play()


bgMusic(bgMusic)