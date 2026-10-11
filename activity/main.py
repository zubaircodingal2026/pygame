#import important laibraies
import pygame

#initializing required modules
pygame.init()

#setup windows geometry
screen = pygame.display.set_mode((400,500))

#create a loop to run tillthe game is quit by the user
done = False

while not done:
    #clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    # make the changes visable
    pygame.display.flip()
        