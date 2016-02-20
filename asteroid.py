import pygame
from utils import Location

class Asteroid(object):
    def __init__(self):
        self.location = Location(100,0)

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("asteroid.png").convert()
        self.sprite.rect = self.sprite.image.get_rect()

    def update(self):
        self.location.y += 5
        if self.location.y > 500:
            self.location.y = 0

    def draw(self, screen):
        screen.blit(self.sprite.image, self.location.get_loc())
