import pygame
pygame.init()
import time

# define some colors
zwart    = (   0,   0,   0)
wit    = ( 255, 255, 255)
groen    = (   0, 255,   0)
rood      = ( 255,   0,   0)

# Zet de breedte en de hoogte van het scherm
size = (700,500)
screen = pygame.display.set_mode(size)

#plaats een titel voor je Window screen
pygame.display.set_caption("Battle port game rules")

#Blijf in de lus tot de user op close klikt.
done = False
  
# Wordt gebruikt om de refresh snelheid van het scherm te beheren
clock = pygame.time.Clock()
  
# -------- Lus Hoofdprogramma -----------
while not done:
    # ALLE EVENTS(ACTIES) WORDEN HIERONDER BEHANDELD
    for event in pygame.event.get(): # User heeft iets gedaan
        if event.type == pygame.QUIT: # Wanneer de user op close klikt
            done = True # Flag om uit de lus te kunnen springen
    # ALLE EVENTS (ACTIES) WORDEN HIERBOVEN BEHANDELD
    
  
  
    # ALLE SPEL LOGICA KOMT HIERONDER TE STAAN
 
    # ALLE SPEL LOGICA KOMT HIERBOVEN TE STAAN
 
 
    # ALLE CODE OM IETS OP HET SCHERM TE BRENGEN VOLGT HIERONDER
    # Wis het scherm en zet een achtergrond
    screen.fill(wit)
    font = pygame.font.SysFont('calibri', 25, True, False)
    text = font.render("Game Rules", True, zwart)
      
    # ALLE CODE OM IETS OP HET SCHERM TE BRENGEN STAAT HIERBOVEN     
    pygame.display.flip()
    pygame.display.flip()
    screen.blit(text, [250, 250])
    # De limiet is frames per seconde
    clock.tick(20)
