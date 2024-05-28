import pygame
from settings import BUTTON_WIDTH, BUTTON_HEIGHT, SCREEN


class Button(pygame.sprite.Group):
    def __init__(self, position, floor_num):
        super().__init__()
        self.image = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.image.fill((210, 210, 210))
        self.rect = self.image.get_rect(center=position)
        self.floor_num = floor_num
        if not pygame.font.get_init():
            pygame.font.init()
        self.font = pygame.font.SysFont(None, 24)

    def update(self):
        pass

    def draw(self, screen):
        SCREEN.blit(self.image, self.rect)
        text_surf = self.font.render(str(self.floor_num), True, (0, 0, 0))
        text_rect = text_surf.get_rect(center= self.rect.center)
        SCREEN.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
