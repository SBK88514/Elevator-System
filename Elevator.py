
import pygame.sprite
from settings import *


class Elevator(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = ELEVATOR_SCALE
        self.rect = self.image.get_rect(midbottom=position)


    def create(self):
        pass
