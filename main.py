import pygame
from pygame.locals import KEYDOWN

def run():
    pygame.init()
    screen = pygame.display.set_mode([320, 320])
    background = pygame.Surface(screen.get_size())

    b = pygame.sprite.Sprite() # create sprite
    b.image = pygame.image.load("asteroid.png").convert() # load ball image
    b.rect = b.image.get_rect() # use image extent values
    b.rect.topleft = [0, 0] # put the ball in the top left corner
    screen.blit(b.image, b.rect)

    pygame.display.update()

    quit = False
    while quit == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            if event.type == pygame.QUIT:
                quit = True
    pygame.quit()


if __name__=='__main__':
    run()
