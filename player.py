import pygame
from utils import Location

class Player(object):
    def __init__(self):
        self.location = Location(50,440)

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("player.png").convert()
        self.sprite.rect = self.sprite.image.get_rect()

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.location.x -= 5

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.location.x += 5

        if self.location.x > 560:
            self.location.x = 560

        if self.location.x < 0:
            self.location.x = 0

    def draw(self, screen):
        screen.blit(self.sprite.image, self.location.get_loc())

    def move_left(self):
        pass

    def move_right(self):
        pass
