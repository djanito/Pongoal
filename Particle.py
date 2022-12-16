import pygame
from Spritesheet import Spritesheet

class Particle(pygame.sprite.Sprite):

    def __init__(self, x, y, color=None):
        super(Particle, self).__init__()
        self.x = x 
        self.y = y
        self.sprite = Spritesheet("png/ball_hit.png", 6, 1, 2, color)
        self.rect = pygame.Rect(x, y, self.sprite.rect.w, self.sprite.rect.h)
        self.image = self.sprite.image
        self.counter = 0

    def update(self):
        if self.sprite.index < len(self.sprite.cells) - 1:
            self.sprite.animate()
            self.image = self.sprite.image
        if self.sprite.index >= len(self.sprite.cells) - 1:
            self.kill()

    def draw(self, screen):
        self.sprite.draw(screen, self.rect.x, self.rect.y) # draw animated ball