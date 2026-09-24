import pygame
import random

#constants for easier adjustments
SCREEN_WEIDTH,SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

#INITIALIZING
pygame.init()

#load and transforms the back ground image
background_image = pygame.transform.scale(pygame.image.load("bg.jpg")
                                          (SCREEN_WEIDTH,SCREEN_HEIGHT))

#load font once at beginning
font = pygame.font.SysFont("time new roman",FONT_SIZE)


class sprite(pygame.sprite.Sprite):
    
    def __init__(self,color,height,weidth):
        super().__init__()
        self.image = pygame.surface([weidth,height])
        self.image.fill(pygame.color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.rect(0,0,weidth,height))
        self.rect = self.image.get_rect()
        
        
    def __init__ (self,x_change,y_change):
        self.rect.x = max(
            min(self.rect.x + x_change,SCREEN_WEIDTH - self.rect.weidth),0)
        self.rect.y = max(
                    min(self.rect.y + y_change,SCREEN_HEIGHT - self.rect.height),0)
        