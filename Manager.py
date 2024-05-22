import pygame

from Building import Building
from settings import *


class Manager(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.buildings = []
        self.create_buildings()

    def launch_screen(self):
        pygame.init()
        self.clock.tick(FPS)

    def check_click(self):
        pass

    def create_buildings(self):
        for building_num in range(NUMBER_OF_BUILDING):
            building = Building(position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            building_id = building_num
            self.buildings.append(building)
            self.add(building)

    def update(self):
        for building in self.buildings:
            building.update()
        for building in self.buildings:
            for floor in building.floors:
                SCREEN.blit(floor.image, floor.rect)
            for elevator in building.elevators:
                SCREEN.blit(elevator.image, elevator.rect)
