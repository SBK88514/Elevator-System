import pygame
from settings import TIMER_FONT_SIZE, SCREEN


# from Floor import Floor


class Timer(pygame.sprite.Sprite):
    def __init__(self, position, initial_time):
        super().__init__()
        if not pygame.font.get_init():
            pygame.font.init()
        self.time_remaining = initial_time
        self.position = position
        self.font = pygame.font.SysFont(None, TIMER_FONT_SIZE)
        self.text = self.font.render(str(self.time_remaining), True, (255, 255, 255))

    def update(self):
        if self.time_remaining > 0:
            # print(self.position, self.time_remaining)
            self.font.render(str(self.time_remaining), True, (255, 255, 255))

    def draw(self, screen):
        SCREEN.blit(self.text, self.position)
