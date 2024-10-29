import pygame

from Button import Button
from Timer import Timer
from settings import FLOOR_SCALE, NUMBER_OF_FLOORS, SCREEN, BUTTON_WIDTH, BUTTON_HEIGHT


class Floor(pygame.sprite.Group):

    def __init__(self, position=None, floor_number=None):
        super().__init__()
        self.time_remaining = 0
        self.image = FLOOR_SCALE
        self.rect = self.image.get_rect(midbottom=position)
        self.floor_num = floor_number

        button_position = (self.rect.centerx, self.rect.centery)
        self.button = Button(position=button_position, floor_num=self.floor_num)

        timer_position = (self.rect.left - 30, self.rect.centery)
        self.timer = Timer(position=timer_position, initial_time=self.time_remaining)

    def update(self):
        self.button.update()
        self.timer.update()
        # self.update_time()

    def draw(self, screen):
        SCREEN.blit(self.image, self.rect)
        self.button.draw(screen)
        self.timer.draw(screen)

    def handle_click(self, mouse_pos):
        if self.button.is_clicked(mouse_pos):
            return self.floor_num
        return None

    def update_time(self, time_remaining):
        self.time_remaining = time_remaining
        self.timer.time_remaining = self.time_remaining
