import pygame
from utils import Location

class Player(object):
    def __init__(self):
        self.location = Location(50,440)

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("player.png").convert()
        self.sprite.rect = self.sprite.image.get_rect()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.sprite.image, self.location.get_loc())
