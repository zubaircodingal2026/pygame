import pygame
pygame.init()

#create the display surface objest of specific dimension
window = pygame.display.set_mode((400, 400))


#fell the screen with gray colour
BACKGROUND_COLOUR = (120,120,120)
window.fill(BACKGROUND_COLOUR)

#define colours
Green = (0,255,0)

#draw solid circle
pygame.draw.circle(window, Green,(300,300),50)

#draw outlined circle
pygame.draw.circle(window, Green,(100,100),50,3)

#draws the surface object to the screen
pygame.display.update()

#game loop
running = True
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Quit pygame
pygame.QUIT()

