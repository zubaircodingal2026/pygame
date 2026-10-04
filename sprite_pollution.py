import pygame
import random

##initializing
pygame.init()

#custom event IDs for colour changes events
SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT =pygame.USEREVENT+ 2

#DEFINE BASIC COLOUR USING PYGAME.COLOUR
#background colour
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

#sprite colours
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

#sprite representing the moving object
class sprite(pygame.sprite.Sprite):
    
    #constructor method
    def __init__(self,color,height,weidth):
        #call to the parents class (sprite) cunstructor
        super().__init__()
        #create the sprite surface and dimensions and color
        self.image = pygame.surface(weidth,height)
        self.image.fill(color)
        #get the sprite rect defining its position and size
        self.rect = self.image.get_rect()
        #set initial velocity with random direction
        self.velocity = [random.choice([-1,1])]
        
        #method to change the sprite position
        def update(self):
            #move the sprite with its velocity
            self.rect.move_ip(self.velocity)
            #flages to track if the sprite hits a boundary
            boundry_hit = False
            #cheack for collision with left  or rightboundaries and revcerse dirsction
            if self.rect <=  0 or self.rect.right.button >=  500:
                self.velocity[0] = -self.velocity[0]
                boundry_hit = True