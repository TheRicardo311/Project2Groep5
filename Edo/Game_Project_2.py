import math
import pygame
class Player:

    def __init__(self, x, y, r):
        self.x = x

        self.y = y

        self.r = r

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            self.x -= 1

        elif keys[pygame.K_RIGHT]:

            self.x += 1



        if keys[pygame.K_UP]:

            self.y -= 1

        elif keys[pygame.K_DOWN]:

            self.y += 1

    
    def draw(self, screen):

        pygame.draw.circle(screen, (0, 255, 0),

                           (int(self.x), int(self.y)), int(self.r))

def process_events():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            # Give the signal to quit

            return True

    

    return False





# Main program logic

def program():

    width = 640

    height = 480

    size = (width, height)

    

    # Start PyGame

    pygame.init()

    

    # Set the resolution

    screen = pygame.display.set_mode(size)

    

    # Set up the default font

    font = pygame.font.Font(None, 30)

    



    

    # Create the player

    player = Player(width * 0.2, height * 0.5, width * 0.1)



    while not process_events():

        # Update entities

        player.update()
        screen.fill((255, 255, 255))

        # Draw the entities
        player.draw(screen)

     
    
        # Flip the screen
        pygame.display.flip()

# Start the program

program()