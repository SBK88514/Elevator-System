import pygame
from settings import *


class Floor(pygame.sprite.Group):
    def __init__(self, position=None):
        super().__init__()
        self.image = FLOOR_SCALE
        self.rect = self.image.get_rect(midbottom=position)

    def create(self):
        pass
